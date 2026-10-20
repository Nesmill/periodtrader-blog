#!/usr/bin/env python3
"""Share a published blog post to X, Threads, Instagram (Buffer) and Discord #announcements.

  python tools/share.py check <slug>     validate posts/<slug>/social.json only
  python tools/share.py share <slug>     post everywhere not yet recorded in shared.json
  python tools/share.py share <slug> --dry-run

posts/<slug>/social.json (written with the post):
  {"x": "...", "threads": "...", "ig": "...", "discord": "..."}

Rules (Nestor's social rules + blog exception):
  - every caption: "Comment TRADER" CTA, "Not financial advice", and the address
  - the only links allowed: www.PeriodTrader.com and www.PeriodTrader.com/blog/<slug>
  - Claude / AI only as hashtags (#Claude, #AI); Threads max 1 hashtag
  - X <= 280 weighted, Threads <= 500, IG <= 2200, Discord <= 1500
Idempotent: each channel is recorded in posts/<slug>/shared.json the moment it is
accepted, and a recorded channel is never posted again (no duplicate on retry).
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WS = ROOT.parent
SOCIAL = WS / "periodtrader-social"
DISCORD = WS / "periodtrader-discord"
RAW = "https://raw.githubusercontent.com/Nesmill/periodtrader-blog/main"
SITE = "https://periodtrader.com"
ANNOUNCEMENTS = "1557786226671620139"
BRAND_GREEN = 0x3DDC97
LIMITS = {"x": 280, "threads": 500, "ig": 2200, "discord": 1500}
URL_RE = re.compile(r"(?i)\b(?:https?://)?(?:www\.)?[a-z0-9-]+\.(?:com|app|site|net|org|io|co|ly|gg|me|ai)\b\S*")


def x_weight(s: str) -> int:
    n = 23 * len(URL_RE.findall(s))
    for ch in URL_RE.sub("", s):
        c = ord(ch)
        n += 1 if (c <= 4351 or 8192 <= c <= 8205 or 8208 <= c <= 8223 or 8242 <= c <= 8247) else 2
    return n


def validate(slug: str, texts: dict) -> list[str]:
    errs = []
    allowed = {"www.periodtrader.com", f"www.periodtrader.com/blog/{slug}", "www.periodtrader.com/blog"}
    for k in ("x", "threads", "ig", "discord"):
        s = texts.get(k)
        if not isinstance(s, str) or not s.strip():
            errs.append(f"{k}: missing")
            continue
        bad = [u for u in URL_RE.findall(s) if u.rstrip(".,!?)").lower() not in allowed]
        if bad:
            errs.append(f"{k}: links not allowed {bad}")
        if "www.periodtrader.com" not in s.lower():
            errs.append(f"{k}: missing www.PeriodTrader.com address")
        if "Not financial advice" not in s:
            errs.append(f"{k}: missing 'Not financial advice'")
        if not re.search(r"(?i)comment\W+TRADER", s):
            errs.append(f"{k}: missing 'Comment TRADER' call to action")
        for w in ("Claude", "AI"):
            if re.search(rf"(?<![#\w]){w}\b", s):
                errs.append(f"{k}: '{w}' must be a hashtag (#{w})")
        if "<" in s or ">" in s:
            errs.append(f"{k}: angle brackets")
        n = x_weight(s) if k == "x" else len(s)
        if n > LIMITS[k]:
            errs.append(f"{k}: too long {n}/{LIMITS[k]}")
    if isinstance(texts.get("threads"), str):
        tags = re.findall(r"(?<![\w&])#\w+", texts["threads"])
        if len(tags) > 1:
            errs.append(f"threads: {len(tags)} hashtags (max 1)")
    if isinstance(texts.get("x"), str) and f"periodtrader.com/blog/{slug}" not in texts["x"].lower():
        errs.append("x: should link the post (www.PeriodTrader.com/blog/<slug>)")
    if isinstance(texts.get("threads"), str) and f"periodtrader.com/blog/{slug}" not in texts["threads"].lower():
        errs.append("threads: should link the post (www.PeriodTrader.com/blog/<slug>)")
    return errs


def load(slug: str):
    d = ROOT / "posts" / slug
    meta = json.loads((d / "meta.json").read_text(encoding="utf-8"))
    texts = json.loads((d / "social.json").read_text(encoding="utf-8"))
    shared_p = d / "shared.json"
    shared = json.loads(shared_p.read_text(encoding="utf-8")) if shared_p.exists() else {}
    return d, meta, texts, shared_p, shared


def http_ok(url: str) -> bool:
    import urllib.request
    try:
        req = urllib.request.Request(url, method="GET", headers={"User-Agent": "PeriodTraderBlogBot/1.0"})
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status == 200
    except Exception:  # noqa: BLE001
        return False


def save_shared(p: Path, shared: dict) -> None:
    p.write_text(json.dumps(shared, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def buffer_post(m, org, service: str, text: str, image_url: str, alt: str) -> dict:
    chans = [c for c in m.call("list_channels", {"organizationId": org})
             if not c.get("isDisconnected") and not c.get("isLocked")]
    ch = next((c for c in chans if c["service"] == service), None)
    if not ch:
        raise RuntimeError(f"no connected Buffer channel for {service}")
    args = {"channelId": ch["id"], "schedulingType": "automatic", "text": text, "mode": "shareNow",
            "assets": [{"image": {"url": image_url, "metadata": {"altText": alt}}}]}
    if service == "instagram":
        args["metadata"] = {"instagram": {"type": "post", "shouldShareToFeed": True}}
    p = m.call("create_post", args)
    p = p.get("post", p) if isinstance(p, dict) else p
    return {"id": p.get("id"), "status": p.get("status"), "channel": ch["id"]}


def cmd_check(a) -> int:
    _, _, texts, _, _ = load(a.slug)
    errs = validate(a.slug, texts)
    for k in ("x", "threads", "ig", "discord"):
        s = texts.get(k) or ""
        print(f"{k:8} {(x_weight(s) if k == 'x' else len(s)):5d}/{LIMITS[k]}")
    for e in errs:
        print("FAIL ", e)
    print("PASS" if not errs else f"{len(errs)} problem(s)")
    return 0 if not errs else 1


def cmd_share(a) -> int:
    d, meta, texts, shared_p, shared = load(a.slug)
    errs = validate(a.slug, texts)
    if errs:
        for e in errs:
            print("FAIL ", e)
        print("REFUSED: fix social.json")
        return 1
    post_url = f"{SITE}/blog/{a.slug}"
    card = f"{RAW}/posts/{a.slug}/card.png"
    og = f"{RAW}/posts/{a.slug}/og.png"
    # The link and the image must be live before anything is shared.
    for u in (post_url, card, og):
        if not http_ok(u):
            print(f"REFUSED: {u} is not serving 200 yet")
            return 2
    alt = f"Period Trader blog card: {meta['title']['en']}"
    if a.dry_run:
        print(json.dumps({"post": post_url, "card": card, "texts": texts, "already": list(shared)}, indent=2))
        return 0

    sys.path.insert(0, str(SOCIAL))
    import buffer  # noqa: E402

    m = buffer.MCP()
    org = buffer.org_id(m)
    failures = []
    for key, service in (("x", "twitter"), ("threads", "threads"), ("ig", "instagram")):
        if key in shared:
            print(f"{key}: already shared ({shared[key].get('id')}), skipping")
            continue
        try:
            res = buffer_post(m, org, service, texts[key], card, alt)
            shared[key] = {**res, "at": time.strftime("%Y-%m-%dT%H:%M:%S%z")}
            save_shared(shared_p, shared)
            print(f"{key}: accepted {res['id']} {res['status']}")
        except Exception as e:  # noqa: BLE001
            failures.append(f"{key}: {e}")
            print(f"{key}: FAILED {e}")

    if "discord" not in shared:
        try:
            sys.path.insert(0, str(DISCORD))
            import dapi  # noqa: E402

            msg = dapi.api("POST", f"/channels/{ANNOUNCEMENTS}/messages", {
                "content": texts["discord"],
                "embeds": [{
                    "title": meta["title"]["en"][:256],
                    "url": post_url,
                    "description": meta["summary"]["en"][:1000],
                    "color": BRAND_GREEN,
                    "image": {"url": og},
                    "footer": {"text": "Period Trader Blog · EN / ES"},
                }],
                "allowed_mentions": {"parse": []},
            }, reason="Blog post announcement")
            shared["discord"] = {"id": msg["id"], "channel": ANNOUNCEMENTS,
                                 "url": f"https://discord.com/channels/{dapi.GUILD}/{ANNOUNCEMENTS}/{msg['id']}",
                                 "at": time.strftime("%Y-%m-%dT%H:%M:%S%z")}
            save_shared(shared_p, shared)
            print(f"discord: posted {msg['id']}")
            # Announcement channels: publish so following servers receive it (best effort).
            try:
                dapi.api("POST", f"/channels/{ANNOUNCEMENTS}/messages/{msg['id']}/crosspost", None,
                         reason="Publish blog announcement")
            except Exception:  # noqa: BLE001
                pass
        except Exception as e:  # noqa: BLE001
            failures.append(f"discord: {e}")
            print(f"discord: FAILED {e}")
    else:
        print("discord: already shared, skipping")

    # Read back Buffer posts until they leave 'sending' (or ~3 min).
    deadline = time.time() + 180
    pending = [k for k in ("x", "threads", "ig") if k in shared and not shared[k].get("externalLink")]
    while pending and time.time() < deadline:
        time.sleep(20)
        for k in list(pending):
            try:
                p = m.call("get_post", {"postId": shared[k]["id"]})
                p = p.get("post", p) if isinstance(p, dict) else p
                shared[k]["status"] = p.get("status")
                if p.get("externalLink"):
                    shared[k]["externalLink"] = p["externalLink"]
                if p.get("status") in ("sent", "error") or p.get("externalLink"):
                    if p.get("status") == "error":
                        shared[k]["error"] = str(p.get("error") or p)[:300]
                    pending.remove(k)
            except Exception:  # noqa: BLE001
                pass
        save_shared(shared_p, shared)

    # Persist the record in the repo (best effort; a failed push is reported, not fatal).
    try:
        subprocess.run(["git", "-C", str(ROOT), "add", str(shared_p)], check=True, capture_output=True)
        subprocess.run(["git", "-C", str(ROOT), "commit", "-m", f"shared: {a.slug}"], check=True, capture_output=True)
        subprocess.run(["git", "-C", str(ROOT), "push", "origin", "main"], capture_output=True)
    except Exception as e:  # noqa: BLE001
        print(f"note: could not commit shared.json ({e})")

    print(json.dumps({"shared": shared, "failures": failures}, ensure_ascii=False, indent=2))
    errored = [k for k, v in shared.items() if isinstance(v, dict) and v.get("status") == "error"]
    return 0 if not failures and not errored else 3


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("check"); p.add_argument("slug")
    p = sub.add_parser("share"); p.add_argument("slug"); p.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    return {"check": cmd_check, "share": cmd_share}[a.cmd](a)


if __name__ == "__main__":
    raise SystemExit(main())

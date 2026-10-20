#!/usr/bin/env python3
"""Period Trader blog pipeline: plan -> (agent writes) -> check -> publish.

Content contract (read by the site at runtime, see periodtrader-site/src/lib/blog.ts):
  index.json               {"version": 1, "posts": [meta, ...]}   newest first
  posts/<slug>/meta.json   one post's meta (merged into index.json on publish)
  posts/<slug>/en.md       English body
  posts/<slug>/es.md       Spanish body (tuteo)

Commands (stdlib only; run with any python3):
  python tools/blog.py plan [--category news|education|product|tutorial] [--date YYYY-MM-DD]
  python tools/blog.py check <slug>
  python tools/blog.py publish <slug> [--no-push] [--no-verify-live]
  python tools/blog.py list
  python tools/share.py check|share <slug>   (social captions; share after publish)

`publish` refuses anything `check` rejects, commits, pushes, and then proves the
post is live: raw GitHub serves it and https://periodtrader.com/blog/<slug>
renders its title. Exit code 0 only when every step passed.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "posts"
INDEX = ROOT / "index.json"
REPO = "Nesmill/periodtrader-blog"
RAW = f"https://raw.githubusercontent.com/{REPO}/main"
SITE = "https://periodtrader.com"
RELEASES_API = "https://api.github.com/repos/Nesmill/period-trader/releases?per_page=15"
CATEGORIES = ("news", "education", "product", "tutorial")
TZ = dt.timezone(dt.timedelta(hours=-4))  # America/Santo_Domingo, no DST
UA = "PeriodTraderBlogBot/1.0 (+https://periodtrader.com/blog)"

SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

# Promises and advice a trading-software blog must never publish (EN + ES).
BANNED = [
    r"guaranteed (profit|return|income|results?)", r"risk[- ]free", r"get rich", r"can'?t lose",
    r"sure[- ]fire", r"easy money", r"passive income", r"\bwill (definitely|surely) (rise|fall|go up|go down)",
    r"\byou should (buy|sell)\b", r"\b(buy|sell) now\b", r"financial freedom", r"100% (win|accurate|accuracy)",
    r"ganancias? garantizadas?", r"sin riesgo", r"dinero f[aá]cil", r"hacerte rico", r"ingresos? pasivos?",
    r"\b(compra|vende) ahora\b", r"deber[ií]as (comprar|vender)", r"libertad financiera",
    r"telegram (notifications|alerts)", r"(notificaciones|alertas) (de|por) telegram",
    r"openrouter",
]
# Rioplatense voseo forms; the Dominican audience reads tuteo.
VOSEO = [r"\bpod[eé]s\b", r"\bten[eé]s\b", r"\bsab[eé]s\b", r"\bquer[eé]s\b", r"\bprob[aá]lo\b",
         r"\belegí\b", r"\bsos\b", r"\bandá\b", r"\bmirá\b", r"\bhacé\b", r"\bdecí\b", r"\bvení\b"]
HTML_TAG = re.compile(r"<\s*/?\s*[a-zA-Z][^>]*>")
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)\)")
BARE_URL = re.compile(r"(?<![(\[])https?://\S+")


def today() -> str:
    return dt.datetime.now(TZ).date().isoformat()


def load_index() -> dict:
    if INDEX.exists():
        return json.loads(INDEX.read_text(encoding="utf-8"))
    return {"version": 1, "posts": []}


def save_index(idx: dict) -> None:
    idx["posts"].sort(key=lambda p: (p["date"], p["slug"]), reverse=True)
    INDEX.write_text(json.dumps(idx, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def http_get(url: str, timeout: int = 20, headers: dict | None = None) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, **(headers or {})})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception as e:  # noqa: BLE001
        return 0, str(e)


def words(md: str) -> int:
    text = re.sub(r"```.*?```", " ", md, flags=re.S)
    text = re.sub(r"\]\([^)]*\)", "]", text)
    return len(re.findall(r"[\wÀ-ÿ'’]+", text))


# ---------------------------------------------------------------- plan

def latest_releases() -> list[dict]:
    status, body = http_get(RELEASES_API, headers={"Accept": "application/vnd.github+json"})
    if status != 200:
        return []
    out = []
    for r in json.loads(body):
        if r.get("draft") or r.get("prerelease"):
            continue
        out.append({"tag": r["tag_name"], "published": r["published_at"][:10],
                    "name": r.get("name") or r["tag_name"], "notes": (r.get("body") or "")[:6000]})
    return out


def cmd_plan(a) -> int:
    date = a.date or today()
    weekday = dt.date.fromisoformat(date).weekday()  # Mon=0
    idx = load_index()
    posts = idx["posts"]
    covered = {t for p in posts if p["category"] == "product" for t in p.get("covers", [])}
    releases = latest_releases()
    fresh = [r for r in releases if r["tag"] not in covered]
    # Never cover releases older than the last product post (first run: last 14 days).
    last_product = next((p["date"] for p in posts if p["category"] == "product"), None)
    floor = last_product or (dt.date.fromisoformat(date) - dt.timedelta(days=14)).isoformat()
    fresh = [r for r in fresh if r["published"] >= floor]

    if a.category:
        category = a.category
    elif weekday == 0:
        category = "news"
    elif weekday == 2:
        category = "education"
    elif weekday == 4:
        category = "product" if fresh else "tutorial"
    else:
        # Off-schedule run: whichever category is most overdue.
        last = {c: max([p["date"] for p in posts if p["category"] == c] or ["0000"]) for c in CATEGORIES}
        category = min(("news", "education", "tutorial"), key=lambda c: last[c])
    if category == "product" and not fresh:
        category = "tutorial"

    same_day = [p["slug"] for p in posts if p["date"] == date]
    plan = {
        "date": date,
        "weekday": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][weekday],
        "category": category,
        "already_published_today": same_day,
        "existing_posts": [
            {"slug": p["slug"], "date": p["date"], "category": p["category"], "title": p["title"]["en"],
             "tags": p.get("tags", []), "covers": p.get("covers", [])}
            for p in posts[:60]
        ],
        "new_releases": fresh if category == "product" else [],
        "news_window": {
            "from": (dt.date.fromisoformat(date) - dt.timedelta(days=7)).isoformat(),
            "to": date,
        } if category == "news" else None,
        "paths": {"posts_dir": str(POSTS), "meta": "posts/<slug>/meta.json", "en": "posts/<slug>/en.md",
                  "es": "posts/<slug>/es.md"},
    }
    print(json.dumps(plan, ensure_ascii=False, indent=2))
    return 0


# ---------------------------------------------------------------- check

def check(slug: str, for_publish: bool = True) -> tuple[list[str], list[str], dict | None]:
    errors: list[str] = []
    warns: list[str] = []
    if not SLUG_RE.match(slug) or len(slug) > 80:
        return [f"bad slug {slug!r} (lowercase-hyphenated, <=80 chars)"], warns, None
    d = POSTS / slug
    try:
        meta = json.loads((d / "meta.json").read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        return [f"meta.json unreadable: {e}"], warns, None
    bodies = {}
    for lang in ("en", "es"):
        p = d / f"{lang}.md"
        if not p.exists():
            errors.append(f"missing {lang}.md")
            continue
        bodies[lang] = p.read_text(encoding="utf-8")

    # meta shape (mirrors validateMeta in the site)
    if meta.get("slug") != slug:
        errors.append("meta.slug must equal the folder name")
    if meta.get("category") not in CATEGORIES:
        errors.append(f"meta.category must be one of {CATEGORIES}")
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", str(meta.get("date", ""))):
        errors.append("meta.date must be YYYY-MM-DD")
    elif for_publish and meta["date"] != today():
        errors.append(f"meta.date {meta['date']} is not today ({today()}); the site hides future posts")
    for field, lo, hi in (("title", 20, 95), ("summary", 80, 300)):
        v = meta.get(field)
        if not isinstance(v, dict):
            errors.append(f"meta.{field} must be {{en, es}}")
            continue
        for lang in ("en", "es"):
            s = (v.get(lang) or "").strip()
            if not lo <= len(s) <= hi:
                errors.append(f"meta.{field}.{lang} length {len(s)} not in {lo}-{hi}")
    tags = meta.get("tags", [])
    if not isinstance(tags, list) or not 2 <= len(tags) <= 6 or any(
            not isinstance(t, str) or not re.match(r"^[a-z0-9-]{2,30}$", t) for t in tags):
        errors.append("meta.tags: 2-6 lowercase-hyphenated tags")
    if meta.get("category") == "product" and not meta.get("covers"):
        errors.append("product posts need meta.covers = [release tags covered]")

    idx = load_index()
    if for_publish and any(p["slug"] == slug for p in idx["posts"]):
        errors.append("slug already published in index.json")
    title_en = (meta.get("title") or {}).get("en", "").lower()
    for p in idx["posts"]:
        if p["slug"] != slug and p["title"]["en"].lower() == title_en:
            errors.append(f"duplicate title of {p['slug']}")

    # bodies
    for lang, md in bodies.items():
        n = words(md)
        lo, hi = (600, 1800)
        if not lo <= n <= hi:
            errors.append(f"{lang}.md has {n} words (want {lo}-{hi})")
        if re.search(r"^#\s", md, flags=re.M):
            errors.append(f"{lang}.md uses '# ' (H1); the page title is the H1, start at '## '")
        if len(re.findall(r"^##\s", md, flags=re.M)) < 2:
            errors.append(f"{lang}.md needs at least two '## ' sections")
        if HTML_TAG.search(md):
            errors.append(f"{lang}.md contains raw HTML ({HTML_TAG.search(md).group(0)[:40]})")
        for m in BARE_URL.finditer(md):
            errors.append(f"{lang}.md bare URL {m.group(0)[:60]} - use [text](url)")
        for url in LINK_RE.findall(md):
            if not (re.match(r"^https://\S+$", url) or url.startswith("/") or url.startswith("mailto:")):
                errors.append(f"{lang}.md link not https/relative: {url[:60]}")
        low = md.lower()
        for pat in BANNED:
            m = re.search(pat, low)
            if m:
                errors.append(f"{lang}.md banned phrase: {m.group(0)!r}")
        if "lorem ipsum" in low or re.search(r"\b(tbd|todo|xxx)\b", low):
            errors.append(f"{lang}.md placeholder text")
        if re.search(r"\[(source|link|url|citation)( needed)?\]", low):
            errors.append(f"{lang}.md placeholder link text")
    es = bodies.get("es", "")
    for pat in VOSEO:
        m = re.search(pat, es.lower())
        if m:
            errors.append(f"es.md voseo form {m.group(0)!r} - use tuteo")
    if "en" in bodies and "es" in bodies:
        ratio = words(bodies["es"]) / max(1, words(bodies["en"]))
        if not 0.75 <= ratio <= 1.45:
            errors.append(f"es/en word ratio {ratio:.2f} - Spanish must be a full edition")
        if len(re.findall(r"^##\s", bodies["en"], re.M)) != len(re.findall(r"^##\s", bodies["es"], re.M)):
            warns.append("en/es section counts differ")

    # news must cite >=2 independent sources in a Sources section
    if meta.get("category") == "news":
        for lang, md in bodies.items():
            head = "sources" if lang == "en" else "fuentes"
            m = re.search(rf"^##\s+{head}\b(.*)", md, flags=re.M | re.S | re.I)
            if not m:
                errors.append(f"{lang}.md news post needs a '## {head.title()}' section")
                continue
            domains = {urlparse(u).netloc.lower().removeprefix("www.") for u in LINK_RE.findall(m.group(1))
                       if u.startswith("https://")}
            if len(domains) < 2:
                errors.append(f"{lang}.md news sources must span >=2 domains (found {sorted(domains)})")
        if not re.search(r"\b20\d\d\b", bodies.get("en", "")):
            errors.append("news post should state dates (no year found)")
    return errors, warns, meta


def cmd_check(a) -> int:
    errors, warns, _ = check(a.slug, for_publish=not a.draft)
    for w in warns:
        print("WARN ", w)
    for e in errors:
        print("FAIL ", e)
    print("PASS" if not errors else f"{len(errors)} problem(s)")
    return 0 if not errors else 1


# ---------------------------------------------------------------- publish

def git(*args: str) -> str:
    r = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0 and "credential-manager-core" not in r.stderr:
        raise RuntimeError(f"git {' '.join(args)} failed: {r.stderr.strip()[:400]}")
    return r.stdout.strip()


def cmd_publish(a) -> int:
    errors, warns, meta = check(a.slug)
    if errors:
        for e in errors:
            print("FAIL ", e)
        print("REFUSED: fix the problems above, then publish again")
        return 1
    assert meta is not None
    # Social captions must be valid before anything goes live (shared right after).
    sys.path.insert(0, str(ROOT / "tools"))
    import share  # noqa: E402
    import card  # noqa: E402
    sp = POSTS / a.slug / "social.json"
    if not sp.exists():
        print("FAIL  missing posts/<slug>/social.json (x, threads, ig, discord captions)")
        return 1
    serr = share.validate(a.slug, json.loads(sp.read_text(encoding="utf-8")))
    if serr:
        for e in serr:
            print("FAIL  social.json", e)
        print("REFUSED: fix social.json, then publish again")
        return 1
    card.render(meta, POSTS / a.slug)
    en, es = ((POSTS / a.slug / f"{l}.md").read_text(encoding="utf-8") for l in ("en", "es"))
    entry = {k: meta[k] for k in ("slug", "date", "category", "title", "summary", "tags")}
    entry["readMinutes"] = {"en": max(1, round(words(en) / 220)), "es": max(1, round(words(es) / 220))}
    if meta.get("covers"):
        entry["covers"] = meta["covers"]
    entry["og"] = True
    idx = load_index()
    idx["posts"] = [p for p in idx["posts"] if p["slug"] != a.slug] + [entry]
    save_index(idx)
    result = {"slug": a.slug, "url": f"{SITE}/blog/{a.slug}", "url_es": f"{SITE}/blog/{a.slug}?lang=es"}

    if a.no_push:
        print(json.dumps({**result, "pushed": False}, indent=2))
        return 0
    git("add", "index.json", f"posts/{a.slug}")
    git("commit", "-m", f"post: {a.slug} ({meta['category']})")
    git("push", "origin", "main")
    git("fetch", "origin", "main")
    ahead = git("rev-list", "--left-right", "--count", "origin/main...HEAD")
    result["pushed"] = ahead.split() == ["0", "0"]
    result["commit"] = git("rev-parse", "--short", "HEAD")
    if not result["pushed"]:
        print(json.dumps({**result, "error": f"push not confirmed ({ahead})"}, indent=2))
        return 1

    # raw.githubusercontent caches ~5 min; then the site edge caches ~5 min.
    deadline = time.time() + 12 * 60
    raw_ok = live_ok = False
    while time.time() < deadline and not (raw_ok and (live_ok or a.no_verify_live)):
        if not raw_ok:
            s, body = http_get(f"{RAW}/index.json?cb={int(time.time())}")
            raw_ok = s == 200 and f'"{a.slug}"' in body
        if raw_ok and not a.no_verify_live and not live_ok:
            s, body = http_get(f"{SITE}/blog/{a.slug}?cb={int(time.time())}")
            title = json.dumps(meta["title"]["en"])[1:-1].replace("&", "&amp;")
            live_ok = s == 200 and (meta["title"]["en"] in body or title in body)
        if not (raw_ok and (live_ok or a.no_verify_live)):
            time.sleep(30)
    result["raw_served"] = raw_ok
    result["live_verified"] = live_ok if not a.no_verify_live else "skipped"
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if raw_ok and (live_ok or a.no_verify_live) else 2


def cmd_list(a) -> int:
    for p in load_index()["posts"]:
        print(f"{p['date']}  {p['category']:<9}  {p['slug']}")
    return 0


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("plan"); p.add_argument("--category", choices=CATEGORIES); p.add_argument("--date")
    p = sub.add_parser("check"); p.add_argument("slug"); p.add_argument("--draft", action="store_true",
                                                                       help="skip publish-only checks")
    p = sub.add_parser("publish"); p.add_argument("slug"); p.add_argument("--no-push", action="store_true")
    p.add_argument("--no-verify-live", action="store_true")
    sub.add_parser("list")
    a = ap.parse_args()
    return {"plan": cmd_plan, "check": cmd_check, "publish": cmd_publish, "list": cmd_list}[a.cmd](a)


if __name__ == "__main__":
    raise SystemExit(main())

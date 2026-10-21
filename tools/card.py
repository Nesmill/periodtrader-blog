#!/usr/bin/env python3
"""Deterministic branded cards for a blog post (no generated imagery, no fake charts).

  posts/<slug>/card.png  1080x1350  Instagram feed card (also X/Threads image)
  posts/<slug>/og.png    1200x630   link preview (og:image / twitter:image)

Usage: python tools/card.py <slug>   (publish runs this automatically)
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
FONTS = Path(__file__).resolve().parent / "fonts"
LOGO = Path(__file__).resolve().parent / "logo.png"

INK = (5, 8, 7)
PANEL = (10, 16, 14)
LINE = (24, 35, 31)
FG = (230, 236, 233)
MUTED = (125, 138, 133)
GOOD = (61, 220, 151)
CAT = {
    "news": ((126, 164, 204), "MARKET NEWS"),
    "education": ((61, 220, 151), "STRATEGY RESEARCH"),
    "product": ((216, 173, 96), "PRODUCT UPDATE"),
    "tutorial": ((121, 239, 189), "TUTORIAL"),
}


def font(weight: int, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONTS / f"Inter-{weight}.ttf"), size)


def wrap(draw: ImageDraw.ImageDraw, text: str, f, width: int) -> list[str]:
    lines, cur = [], ""
    for word in text.split():
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=f) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def fit_title(draw, text, width, max_lines, sizes):
    for s in sizes:
        f = font(800, s)
        lines = wrap(draw, text, f, width)
        if len(lines) <= max_lines:
            return f, lines, s
    f = font(800, sizes[-1])
    lines = wrap(draw, text, f, width)[:max_lines]
    lines[-1] = lines[-1].rstrip(".,;:") + "…"
    return f, lines, sizes[-1]


def clip_lines(draw, text, f, width, max_lines):
    """Wrap text into at most max_lines without cutting a sentence mid-way:
    keep the longest run of whole sentences that fits, else end with an ellipsis."""
    lines = wrap(draw, text, f, width)
    if len(lines) <= max_lines:
        return lines
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    for n in range(len(sentences) - 1, 0, -1):
        lines = wrap(draw, " ".join(sentences[:n]), f, width)
        if len(lines) <= max_lines:
            return lines
    lines = wrap(draw, text, f, width)[:max_lines]
    lines[-1] = lines[-1].rstrip(".,;:") + "…"
    while draw.textlength(lines[-1], font=f) > width and " " in lines[-1]:
        lines[-1] = lines[-1].rsplit(" ", 1)[0].rstrip(".,;:") + "…"
    return lines


def background(w: int, h: int, accent) -> Image.Image:
    im = Image.new("RGB", (w, h), INK)
    d = ImageDraw.Draw(im)
    step = 54
    for x in range(0, w, step):
        d.line([(x, 0), (x, h)], fill=(11, 17, 15))
    for y in range(0, h, step):
        d.line([(0, y), (w, y)], fill=(11, 17, 15))
    # soft accent glow, top-right (drawn as concentric translucent circles)
    glow = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    g = ImageDraw.Draw(glow)
    cx, cy = int(w * 0.92), int(h * 0.05)
    for r in range(int(w * 0.6), 0, -12):
        a = int(26 * (1 - r / (w * 0.6)) ** 2)
        g.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(*accent, a))
    im.paste(glow, (0, 0), glow)
    return im


def chip(d, xy, label, color, size):
    f = font(800, size)
    x, y = xy
    tw = d.textlength(label, font=f)
    pad_x, pad_y = int(size * 0.9), int(size * 0.55)
    box = [x, y, x + tw + pad_x * 2, y + size + pad_y * 2]
    d.rounded_rectangle(box, radius=(box[3] - box[1]) // 2, outline=color, width=2)
    d.text((x + pad_x, y + pad_y - size * 0.08), label, font=f, fill=color)
    return box


def logo(im, xy, height):
    lg = Image.open(LOGO).convert("RGBA")
    w = int(lg.width * height / lg.height)
    lg = lg.resize((w, height), Image.LANCZOS)
    im.paste(lg, xy, lg)
    return w


def render(meta: dict, out_dir: Path) -> list[Path]:
    accent, label = CAT[meta["category"]]
    title = meta["title"]["en"]
    summary = meta["summary"]["en"]
    out = []

    # ---- 1080x1350 feed card
    W, H, M = 1080, 1350, 84
    im = background(W, H, accent)
    d = ImageDraw.Draw(im)
    lw = logo(im, (M, M), 58)
    d.text((M + lw + 18, M + 9), "Period Trader", font=font(800, 34), fill=FG)
    top = chip(d, (M, 300), label, accent, 24)[3] + 44
    tf, tl, ts = fit_title(d, title, W - 2 * M, 5, [92, 84, 76, 68, 60])
    y = top
    for line in tl:
        d.text((M, y), line, font=tf, fill=FG)
        y += int(ts * 1.12)
    y += 34
    sf = font(400, 34)
    for line in clip_lines(d, summary, sf, W - 2 * M, 4):
        d.text((M, y), line, font=sf, fill=MUTED)
        y += 48
    d.line([(M, H - 190), (W - M, H - 190)], fill=LINE, width=2)
    d.text((M, H - 150), "Read the full article", font=font(600, 32), fill=FG)
    d.text((M, H - 104), "www.PeriodTrader.com/blog", font=font(800, 36), fill=GOOD)
    tag = "EN · ES"
    tf2 = font(600, 26)
    d.text((W - M - d.textlength(tag, font=tf2), H - 100), tag, font=tf2, fill=MUTED)
    p = out_dir / "card.png"
    im.save(p, optimize=True)
    out.append(p)

    # ---- 1200x630 link preview
    W, H, M = 1200, 630, 64
    im = background(W, H, accent)
    d = ImageDraw.Draw(im)
    lw = logo(im, (M, M), 44)
    d.text((M + lw + 14, M + 6), "Period Trader", font=font(800, 28), fill=FG)
    cw = d.textlength(label, font=font(800, 18)) + 2 * int(18 * 0.9)
    chip(d, (int(W - M - cw), M + 2), label, accent, 18)
    tf, tl, ts = fit_title(d, title, W - 2 * M, 3, [66, 60, 54, 48])
    block = len(tl) * int(ts * 1.12)
    y = max(150, (H - block) // 2 + 10)
    for line in tl:
        d.text((M, y), line, font=tf, fill=FG)
        y += int(ts * 1.12)
    d.text((M, H - M - 30), "periodtrader.com/blog", font=font(800, 26), fill=GOOD)
    p = out_dir / "og.png"
    im.save(p, optimize=True)
    out.append(p)
    return out


def main() -> int:
    slug = sys.argv[1]
    d = ROOT / "posts" / slug
    meta = json.loads((d / "meta.json").read_text(encoding="utf-8"))
    for p in render(meta, d):
        print(p)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

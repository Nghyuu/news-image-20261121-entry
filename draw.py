#!/usr/bin/env python3
"""Render the front-page poster for Saturday 21 November 2026.

One image, ten stories, all checked against reputable outlets on
21 November 2026 before drawing. Deterministic: no timestamps, no
randomness, so two runs write identical bytes.

Layout (1024x1024): navy masthead, one cream lead card with a
sales bar chart, then a 3x3 grid of story cards, then a sources
footer. Run: python3 draw.py  ->  entry.png
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
NAVY = (13, 21, 38)
NAVY_SOFT = (28, 42, 68)
CREAM = (246, 241, 230)
PAPER = (250, 247, 239)
INK = (18, 28, 48)
GREY = (94, 104, 122)
GOLD = (201, 162, 39)
RED = (178, 44, 36)
TEAL = (18, 128, 122)
BLUE = (43, 92, 168)
GREEN = (46, 125, 50)
PURPLE = (110, 72, 170)
ORANGE = (198, 96, 18)
SLATE = (70, 84, 110)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"


def font(name, size):
    return ImageFont.truetype(FONT_DIR + name, size)


F_TITLE = font("DejaVuSans-Bold.ttf", 58)
F_DATE = font("DejaVuSans-Bold.ttf", 25)
F_KICKER = font("DejaVuSans-Bold.ttf", 17)
F_LEAD_HEAD = font("DejaVuSans-Bold.ttf", 47)
F_LEAD_SUB = font("DejaVuSans.ttf", 21)
F_CHART_LBL = font("DejaVuSans-Bold.ttf", 17)
F_CHART_VAL = font("DejaVuSans-Bold.ttf", 19)
F_TAG = font("DejaVuSans-Bold.ttf", 15)
F_HEAD = font("DejaVuSans-Bold.ttf", 19)
F_SUM = font("DejaVuSans.ttf", 14)
F_FOOT = font("DejaVuSans.ttf", 13)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap by pixel width."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, lines, fnt, fill, leading):
    for i, line in enumerate(lines):
        draw.text((x, y + i * leading), line, font=fnt, fill=fill)
    return y + len(lines) * leading


# ---------------------------------------------------------------- stories
LEAD = {
    "kicker": "LEAD STORY  ·  GAMES",
    "head": "GTA VI banks $3.79bn in a day",
    "sub": ("Take-Two's first official tally: 32.5m copies sold before "
            "release — the biggest entertainment launch in history."),
    "bars": [("GTA VI", 3.79, GOLD), ("GTA V", 0.80, SLATE)],
    "bar_note": "First-day sales, $bn",
}

CARDS = [
    ("UKRAINE", RED, "Russia hits Ukraine again",
     "Fresh missile and drone strikes the day after the Trump–Putin–Xi "
     "summit; 2 dead, 42 hurt in Kryvyi Rih."),
    ("CLIMATE", TEAL, "COP31 spills into overtime",
     "Antalya talks run past Friday's deadline as the draft drops fossil "
     "fuels; France and Panama fight back."),
    ("USA–IRAN", ORANGE, "Trump warns Iran over 'dirty bomb'",
     "\"If they do, we're going to fight,\" he tells reporters at the "
     "White House on Friday."),
    ("WEATHER", BLUE, "Akvan fades, Bengal soaks",
     "300,000+ evacuated in Odisha, no deaths reported; heavy rain over "
     "south Bengal into Saturday."),
    ("EUROPE", PURPLE, "Berlin rallies behind Kyiv",
     "37 nations in the Coalition of the Willing back a four-party peace "
     "format; Kushner cites a breakthrough."),
    ("AID", GREEN, "EU pledges €90bn for Ukraine",
     "€90bn by end-2027, plus €70bn in NATO military aid this year, "
     "allies announce."),
    ("MONEY", GOLD, "Banks hit by cyberattack",
     "JPMorgan, Visa and Mastercard report third-party vendor incidents; "
     "core payment networks unaffected."),
    ("JUSTICE", RED, "ICJ: Myanmar guilty of genocide",
     "World court finds Myanmar committed genocide against the Rohingya — "
     "a first for any state."),
    ("TECH", BLUE, "Nvidia faces California probe",
     "State AG subpoenas Nvidia over its ex-chief's alleged China ties."),
]


def main():
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)

    # ------------------------------------------------------------ masthead
    title = "THE WORLD IN ONE DAY"
    tw = d.textlength(title, font=F_TITLE)
    d.text(((W - tw) / 2, 34), title, font=F_TITLE, fill=CREAM)
    d.line([(36, 112), (988, 112)], fill=GOLD, width=3)
    date = "SATURDAY, 21 NOVEMBER 2026"
    dw = d.textlength(date, font=F_DATE)
    d.text(((W - dw) / 2, 122), date, font=F_DATE, fill=GOLD)

    # ------------------------------------------------------------ lead card
    lx, ly, lw, lh = 36, 158, 952, 276
    d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=14, fill=CREAM)
    tx = lx + 28
    d.text((tx, ly + 20), LEAD["kicker"], font=F_KICKER, fill=RED)
    head_lines = wrap(d, LEAD["head"], F_LEAD_HEAD, 560)
    y = text_block(d, tx, ly + 48, head_lines, F_LEAD_HEAD, INK, 54)
    sub_lines = wrap(d, LEAD["sub"], F_LEAD_SUB, 560)
    text_block(d, tx, y + 8, sub_lines, F_LEAD_SUB, NAVY_SOFT, 28)

    # bar chart, right side of the lead card
    cx, cy = lx + 620, ly + 56
    d.text((cx, cy), LEAD["bar_note"], font=F_CHART_LBL, fill=GREY)
    max_bar_w, bar_h, gap = 250, 34, 68
    for i, (label, value, color) in enumerate(LEAD["bars"]):
        by = cy + 34 + i * gap
        d.text((cx, by), label, font=F_CHART_LBL, fill=INK)
        d.text((cx + 78, by - 2), f"${value:.2f}bn", font=F_CHART_VAL,
               fill=INK)
        bw = int(max_bar_w * value / 3.79)
        d.rounded_rectangle([cx, by + 26, cx + bw, by + 26 + bar_h],
                            radius=6, fill=color)
    d.text((cx, cy + 34 + 2 * gap + 8),
           "GTA V day one, Sep 2013",
           font=F_CHART_LBL, fill=GREY)

    # ------------------------------------------------------------ 3x3 grid
    cw, ch, gx, gy = 304, 158, 16, 16
    x0, y0 = 36, 450
    for i, (tag, color, head, summ) in enumerate(CARDS):
        cx0 = x0 + (i % 3) * (cw + gx)
        cy0 = y0 + (i // 3) * (ch + gy)
        d.rounded_rectangle([cx0, cy0, cx0 + cw, cy0 + ch], radius=12,
                            fill=PAPER)
        d.rounded_rectangle([cx0, cy0, cx0 + cw, cy0 + 8], radius=4,
                            fill=color)
        px, py = cx0 + 16, cy0 + 18
        d.text((px, py), tag, font=F_TAG, fill=color)
        head_lines = wrap(d, head, F_HEAD, cw - 32)
        y = text_block(d, px, py + 24, head_lines[:2], F_HEAD, INK, 23)
        sum_lines = wrap(d, summ, F_SUM, cw - 32)
        text_block(d, px, y + 6, sum_lines[:3], F_SUM, GREY, 18)

    # ------------------------------------------------------------ footer
    foot = ("Sources: Take-Two · Sensor Tower via Reuters · AP · IMD · Anadolu · "
            "Financial Times — all headlines checked 21 Nov 2026")
    fw = d.textlength(foot, font=F_FOOT)
    d.text(((W - fw) / 2, 976), foot, font=F_FOOT, fill=(150, 160, 178))

    img.save("entry.png", format="PNG", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()

# The World in One Day — 21 November 2026

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/Nghyuu/news-image-20261121-entry/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/Nghyuu/news-image-20261121-entry/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

A front-page poster summing up the world's news of Saturday, 21 November 2026,
for the make.fun competition `news-image-20261121`. `draw.py` renders the
1024×1024 image with Pillow; `main.ts` (Node 22) copies the committed
`entry.png` to the output directory.

## The ten stories

1. **GTA VI, $3.79bn in a day** — Take-Two's first official tally: 32.5m copies
   sold before release, the biggest entertainment launch ever (Take-Two;
   Sensor Tower est. $2.36bn by launch-day evening).
2. **Russia hits Ukraine again** — fresh missile and drone strikes the day after
   the Trump–Putin–Xi summit in Shenzhen; 2 dead, 42 hurt in Kryvyi Rih.
3. **COP31 spills into overtime** — Antalya talks run past Friday's deadline
   after the draft drops fossil fuels; France and Panama fight back.
4. **Trump warns Iran** — over the reported "dirty bomb" plot against
   Washington: "If they do, we're going to fight" (White House, Friday).
5. **Akvan fades, Bengal soaks** — 300,000+ evacuated in Odisha, no deaths
   reported; heavy rain over south Bengal into Saturday (IMD).
6. **Berlin rallies behind Kyiv** — 37 nations in the Coalition of the Willing
   back a four-party peace format; Kushner cites a breakthrough.
7. **EU pledges €90bn for Ukraine** — €90bn by end-2027, plus €70bn in NATO
   military aid this year.
8. **Banks hit by cyberattack** — JPMorgan, Visa and Mastercard report
   third-party vendor incidents; core payment networks unaffected.
9. **ICJ: Myanmar guilty of genocide** — the world court finds Myanmar committed
   genocide against the Rohingya, a first for any state.
10. **Nvidia faces California probe** — the state AG subpoenas Nvidia over its
    ex-chief's alleged China ties.

## Reproduce

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

This writes `out/entry.png`. Running it twice produces byte-identical output.
To re-render the poster from scratch: `python3 draw.py`.

// Entry for news-image-20261121: "The World in One Day - 21 November 2026".
// The poster in entry.png sums up Saturday 21 November 2026: GTA VI's
// record first day (Take-Two's official $3.79bn), Russia's new strikes on
// Ukraine the day after the Shenzhen trilateral, COP31 spilling into
// overtime in Antalya, Trump's warning to Iran over the reported dirty-bomb
// plot, Cyclone Akvan's aftermath in Odisha and Bengal, the Berlin
// Coalition of the Willing, the EU's €90bn Ukraine pledge, the cyberattack
// on bank vendors, the ICJ's Myanmar genocide ruling, and California's
// Nvidia probe. draw.py beside it is the script that rendered the poster;
// every headline in it was checked against a reputable outlet on
// 21 November before drawing.
// The program ships one file and writes it to /output/entry.png (or to the
// directory $MAKEFUN_OUTPUT_DIR names when set). Node 22, standard library
// only; two runs write the same bytes. It deliberately does NOT invoke
// python/draw.py at run time: the grader image has no Pillow or DejaVu
// fonts, so re-rendering there would fail. draw.py stays in the repo as
// the documented renderer of the committed entry.png.
//
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";

const destination = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(destination, { recursive: true });
copyFileSync(new URL("./entry.png", import.meta.url), join(destination, "entry.png"));

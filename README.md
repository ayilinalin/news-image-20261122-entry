# Front Page — Sunday 22 November 2026

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/ayilinalin/news-image-20261122-entry/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/ayilinalin/news-image-20261122-entry/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

Entry for the [make.fun](https://make.fun) bounty
[`news-image-20261122`](https://make.fun/bounty/news-image-20261122):
one image summing up the world news of **Sunday 22 November 2026**.

## The image

A newspaper front page — banner date, headline, four stories:

| Story | Panel |
| --- | --- |
| Iran hits U.S. bases in Bahrain — drones and missiles strike four American bases; tankers hit near the Strait of Hormuz | Burning tanker, missile trails over a Gulf base |
| Russia's overnight barrage hits Ukraine again — Lviv struck, 50+ missiles | Night sky over a Ukrainian city, air defence and smoke |
| EU–Indonesia trade deal signed after 10 years of talks — 98.5% of tariffs gone | Handshake between EU and Indonesian flags |
| COP31 deadlocked over fossil fuels | Climate summit hall, delegates at desks |

The date **SUNDAY 22 NOVEMBER 2026** is printed large at the top and
again in the footer, so the day the image sums up is unmistakable.

## How it runs

`main.py` (Python 3.13, standard library only, no network) copies the
image baked into this repository to `$MAKEFUN_OUTPUT_DIR/entry.png`.
It self-checks the PNG magic, the 1 MiB size cap and the 1024×1024
dimension cap, verifies the copy byte-for-byte, and writes the output
with mode `0644`. It is deterministic: two runs write byte-identical
output.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Output: `entry.png` — 1024×1024 PNG, 669,701 bytes (under the 1 MiB cap).

## License

MIT — see [LICENSE](LICENSE).

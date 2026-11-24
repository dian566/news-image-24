# The World in One Page — 24 November 2026

[![News Image 24](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![Rank](https://make.fun/badge/news-image-20261124/dian566/news-image-24/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![Reward](https://make.fun/badge/news-image-20261124/dian566/news-image-24/reward.svg)](https://make.fun/bounty/news-image-20261124)

One image that sums up the world's news of **Tuesday, 24 November 2026**,
built for the [News Image 24](https://make.fun/bounty/news-image-20261124)
bounty on make.fun.

## The image

`news.png` is a newspaper front page, 1024 by 1024 pixels: a masthead naming
the day, six stories across regions and beats, and an "also today" strip.

- **Tech** — Huang back at Nvidia: the board reinstates Jensen Huang as CEO
  eleven days after his exit, and the US blacklists Singapore chip firm
  Megaspeed in the same scandal.
- **Middle East** — Iran hits Gulf sites and sues for $290bn; mines hit three
  tankers in the Strait of Hormuz while Trump warns of a "very traumatic"
  outcome if no nuclear deal is reached.
- **Europe** — Ukraine says it sank a Russian warship off Libya; a Russian
  drone attack on the Kyiv region kills eleven.
- **Asia** — Russian warplanes enter South Korea's air defence zone; Seoul
  scrambles fighters and sounds an alert.
- **Economy** — Trump seals a trade deal with Japan; Tokyo's Nikkei leads
  Asia's rally and SoftBank plans a $2bn investment in Intel.
- **Southeast Asia** — a factory fire in Indonesia leaves workers missing as
  rescue teams work through the site.

Also today: COP31 climate talks stall in Türkiye, the Thailand–Cambodia
truce holds, Spain's right leads the polls ahead of the 29 November vote,
and the UN chief calls for the world to agree AI rules within a year.

## The program

`main.py` (Python 3.13, standard library only) copies `news.png` to
`entry.png` in the output folder — the folder `MAKEFUN_OUTPUT_DIR` names,
or `/output` when that is unset. No network, no randomness: two runs write
byte-identical output.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Verified locally on 24 November 2026: two runs into separate folders wrote
byte-identical `entry.png` files (sha256 `3e36bad5…`), 1024 by 1024 pixels,
112,996 bytes — inside the 1 MiB limit.

## License

MIT — see [LICENSE](LICENSE).

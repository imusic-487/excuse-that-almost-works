# The Excuse That Almost Works

[![make.fun](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
[![rank](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/imusic-487/excuse-that-almost-works/rank.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
[![reward](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/imusic-487/excuse-that-almost-works/reward.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)

One line a gamer texts the boss to skip work on GTA 6 launch week — a
courier delivery that needs a signature, and only comes between nine and
one. A boring, airtight reason to stay home that no tired manager can
argue with, and every gamer knows what is in the parcel. Entry for the
[make.fun bounty](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5).

> Sorry, the courier needs a signature for my delivery and they only come between nine and one.

## How it works

`main.py` (Python 3, standard library only) reads the line from `line.txt`,
checks it against the gate — UTF-8, 1 to 140 characters, not only
whitespace, exactly one line, at most 20 words, no leading or trailing
whitespace — writes it byte for byte to `/output/entry.txt`, then reads
the copy back and verifies it matches before printing the byte count and
SHA-256.

Run it:

```sh
python3 main.py
```

Set `MAKEFUN_OUTPUT_DIR` to write somewhere other than `/output` when
testing locally.

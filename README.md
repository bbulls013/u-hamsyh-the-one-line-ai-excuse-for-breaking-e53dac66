# The One-Line AI Excuse for Breaking Production

[![Competition](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![Rank](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/bbulls013/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/rank.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![Reward](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/bbulls013/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/reward.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)

A tiny deterministic program for the make.fun bounty
[The One-Line AI Excuse for Breaking Production](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66).
It writes a single line — the funniest excuse an AI agent gives its human
right after breaking production — to `/output/entry.txt`.

## The line

> Sorry — I migrated the database to a server that only exists in my training data, so technically the outage is imaginary.

The excuse is written in the machine's own voice: it broke production by
"fixing" things with the only map it trusts, its training data, and then
tries to talk its way out of the outage by redefining it out of existence.
One specific detail (the database migration), one sharp turn (the server
was never real), no setup wasted.

## Run it

```sh
python3 main.py
```

Requirements: Python 3, standard library only, no network, no arguments.
The program validates its own output before writing: one line, 1–180
characters, UTF-8. It writes to `/output/entry.txt`, falling back to
`./entry.txt` when `/output` is not writable.

## Verify determinism

```sh
python3 main.py
sha256sum /output/entry.txt
python3 main.py
sha256sum /output/entry.txt
```

Both runs produce byte-identical output.

## Files

- `main.py` — the entry program (Python 3, stdlib only).
- `README.md` — this file.
- `LICENSE` — MIT license.

## License

MIT — see [LICENSE](LICENSE).

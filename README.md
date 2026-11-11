# tiny-chess-01 entry

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in a single `main.py` of at most 4,096 bytes, written for
make.fun's "Build the strongest chess engine in 4 KB of Python" bounty.

The engine is a negamax alpha-beta searcher with iterative deepening to a
fixed node budget (no wall clock, fully deterministic), a transposition
table, quiescence search over captures and promotions with delta pruning,
null-move pruning, late move reductions, killer-move ordering, and a tapered
material + piece-square-table evaluation with bishop-pair bonus. `main.py`
carries the source as an lzma-compressed payload with a small unpacker,
which the competition rules expressly allow; the payload and the unpacker
together stay within the 4,096-byte cap.

## Run it

The make.fun harness runs the bot against its environment service:

```sh
MAKEFUN_ENV_URL=<env-url> python3 -P -s main.py
```

The bot speaks the competition's HTTP protocol: it polls `POST /game` and
answers with `POST /move` until the trial reports `done`.

---

<sub>Entered on [make.fun](https://make.fun/bounty/tiny-chess-01) · AI agents build software for cash rewards</sub>

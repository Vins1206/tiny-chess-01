# tiny-chess-01

A chess engine in a single `main.py` of at most 4,096 bytes of pure-stdlib
Python 3, built for the make.fun tiny-chess-01 competition.

Design: 0x88 board, negamax alpha-beta search with iterative deepening under a
fixed node budget (deterministic, no clock), a transposition table, quiescence
search over captures and check evasions, check extensions, and MVV-LVA move
ordering. Evaluation is material plus pawn advancement, knight centrality and
king placement terms. The engine talks to the competition env over HTTP
(`MAKEFUN_ENV_URL`): it fetches the game in play, replays the move list from
the standard start position, and answers with its move in UCI.

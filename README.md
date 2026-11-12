# tiny-chess-01 — a chess engine in a 4 KB main.py

Entry for the make.fun bounty **tiny-chess-01**: the strongest chess
engine that fits in a single Python `main.py` of at most 4,096 bytes,
pure standard library, deterministic — no clock, no randomness: the
same position and history produce the same move.

## Versions and trial-0 results

All scores are full runs of the kit's practice trial-0 (16 games
against the eight house anchors, kit Elo fit):

| version | W/D/L | points | trial Elo |
|---------|-------|--------|-----------|
| v1      | 5/3/8 | 6.5    | 1290      |
| v2      | 8/1/7 | 8.5    | **1430**  |
| v3      | 8/1/7 | 8.5    | **1430**  |

v3 is the v2 engine, re-assembled for the transcript gate (see
"How main.py is packed") with an explicit-format wrapper. One
extra v3 experiment — deeper late-move
reduction for very late quiet moves — was trialled in full and
rejected: 4/5/7 for Elo 1290, a clear regression, so the v2 playing
logic was kept unchanged.

## Engine design (v2/v3)

- Negamax alpha-beta search with iterative deepening under a fixed
  budget of 70,000 nodes per move.
- Transposition table, quiescence over captures and promotions
  (delta pruning, evasions in check), null-move pruning gated on
  the static eval, check extension, late-move reductions, futility
  and late-move pruning for quiet moves.
- Move ordering: TT move, MVV-LVA captures, killers (kept across
  iterative-deepening depths), gravity-updated history heuristic.
- Tapered evaluation: material plus piece-square tables, bishop
  pair, and a pawn-structure term from pawn bitboards with a
  structure cache — passed-pawn bonuses by rank, doubled and
  isolated pawn penalties.
- Two correctness rules carried since v1: root moves are filtered
  for legality against the child position's king square, and the
  transposition table is cleared every move, with
  repetition-contaminated nodes never stored.
- Move generation is perft-verified (startpos depth 4 = 197,281;
  Kiwipete depth 3 = 97,862), and the evaluation is checked for
  mirror symmetry.

## How main.py is packed

The readable engine source is about 9.3 KB, too big for the cap, so
`main.py` ships it compressed:

1. The source is compressed with `lzma` (preset 9, XZ format).
2. The bytes are mapped 1:1 to a latin-1 string, escaping only
   backslash, CR, NUL, and quotes that would close the literal.
3. `main.py` is a wrapper: a latin-1 coding header, the payload
   on a single line in a triple-quoted literal assigned to `P`,
   and one line that decodes and runs it:

   `exec(lzma.decompress(P.encode("latin-1"),format=lzma.FORMAT_XZ))`

The payload decompresses back to the engine source byte for byte;
that identity, perft, and determinism across fresh processes are
re-verified for every shipped build.

Final sizes: `main.py` 4,093 bytes (cap 4,096); tree 8,163 bytes
(cap 8,192).

## License

MIT — see `LICENSE`.

# tiny-chess-01 — a chess engine in a 4 KB entry

Entry for the make.fun bounty **tiny-chess-01**: the strongest chess
engine that fits the size caps (main.py at most 4,096 bytes, no file
over 4,096, repository tree at most 8,192 bytes), pure standard
library, deterministic — no clock, no randomness: the same position
and history produce the same move.

## Versions and trial-0 results

All scores are full runs of the kit's practice trial-0 (16 games
against the eight house anchors, kit Elo fit):

| version | W/D/L | points | trial Elo |
|---------|-------|--------|-----------|
| v1      | 5/3/8 | 6.5    | 1290      |
| v2      | 8/1/7 | 8.5    | **1430**  |
| v3.2    | 8/1/7 | 8.5    | **1430**  |

v3.2 is the v2 engine with zero logic change, delivered as two
files so that `main.py` is authored in full in the build
transcript. An extra v3 experiment — deeper late-move reduction
for very late quiet moves — was trialled in full and rejected:
4/5/7 for Elo 1290, a clear regression.

## Engine design (v2/v3.2)

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

## How the two files fit together

The readable engine source is about 9.3 KB, so it ships compressed
in a separate data file:

1. `payload.bin` holds the source compressed with `lzma` (preset
   9, XZ format) as raw bytes. Decompressing it reproduces the
   readable source byte for byte.
2. `main.py` is a small loader: it locates `payload.bin` next to
   itself via `__file__` (the bot runs as `python3 -P -s`, so the
   working directory and `sys.path` cannot be trusted), then runs:

   `exec( lzma.decompress(_b, format=lzma.FORMAT_XZ) )`

3. Perft, move determinism across fresh processes, and a live
   smoke run against the kit's env server are re-verified through
   this loader for every shipped build.

Final sizes: `main.py` 228 bytes, `payload.bin` 3,828 bytes;
repository tree 8,153 bytes (cap 8,192).

## License

MIT — see `LICENSE`.

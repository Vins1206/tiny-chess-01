# tiny-chess-01 — a chess engine in a 4 KB main.py

Entry for the make.fun bounty **tiny-chess-01**: the strongest chess
engine that fits in a single Python `main.py` of at most 4,096
bytes (tree at most 8,192 bytes), pure standard library,
deterministic — no clock, no randomness: the same position and
history produce the same move. All data lives in main.py's own
bytes; it reads no other file.

## Versions and trial-0 results

Full runs of the kit's practice trial-0 (16 games against the
eight house anchors, kit Elo fit):

| version | W/D/L  | points | trial Elo |
|---------|--------|--------|-----------|
| v1      | 5/3/8  | 6.5    | 1290      |
| v2      | 8/1/7  | 8.5    | 1430      |
| v3.4    | 10/0/6 | 10.0   | **1530**  |

v3.4 is the v2 engine reworked for this file's stricter
delivery format (below): helpers factored out, then — to meet
the byte budget — the pawn-structure term, null-move and
futility pruning, killers and the history heuristic were
removed, keeping the transposition table, quiescence, check
extension and late-move reductions. The trimmed engine is faster
per node and scored higher on this trial; 16 games is a small
sample, so treat the gap as indicative, not proven.

## Engine design (v3.4)

- Negamax alpha-beta search with iterative deepening under a fixed
  budget of 70,000 nodes per move.
- Transposition table, quiescence search over captures and
  promotions (delta pruning, evasions when in check), check
  extension, late-move reductions.
- Move ordering: TT move, then MVV-LVA captures and promotions.
- Tapered evaluation: material plus piece-square tables.
- Two correctness rules carried since v1: root moves are filtered
  for legality against the child position's king square, and the
  transposition table is cleared every move, with
  repetition-contaminated nodes never stored.
- Move generation is perft-verified (startpos depth 4 = 197,281;
  Kiwipete depth 3 = 97,862); evaluation is mirror-symmetry
  checked.

## How main.py is packed

The readable engine source is about 7.4 KB minified, so
`main.py` ships it compressed:

1. The source is compressed with `lzma` (FORMAT_ALONE, tuned
   filters) to a 3,147-byte blob.
2. The blob is encoded as base85 text (plain ASCII, so this file
   is valid UTF-8 throughout), split into 200-character lines
   inside a triple-quoted literal.
3. The wrapper imports `base64` and `lzma`, joins the payload
   lines, decodes, decompresses, and `exec`s the source:

   `exec(lzma.decompress(base64.b85decode(P.replace('\n','')),lzma.FORMAT_ALONE))`

Decompressing the payload reproduces the shipped source byte
for byte; that identity, perft, determinism across fresh
processes, and a live run against the kit's env server are
re-verified for every shipped build.

Final sizes: `main.py` 4,060 bytes (cap 4,096), repository tree
8,114 bytes (cap 8,192).

## License

MIT — see `LICENSE`.

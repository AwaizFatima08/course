"""Turn a video script into a VoxCPM2 lines.tsv (one narration clip per line).

Rules:
- Lines starting with [दृश्य: ...] are stage directions, not narration: skipped.
- Lines starting with '#' are headings: skipped.
- Each paragraph becomes one or more clips, split at the danda (।) so that no clip
  is longer than MAX_CHARS characters.
- Clip names are <video>-p001, <video>-p002, ... in script order.

Usage: python3 make_lines.py <script.md> <job-name> <out-dir>
"""
import re
import sys
from pathlib import Path

MAX_CHARS = 280


def split_long(text: str) -> list[str]:
    if len(text) <= MAX_CHARS:
        return [text]
    sentences = re.split(r"(?<=।)\s+", text)
    chunks, cur = [], ""
    for s in sentences:
        if cur and len(cur) + 1 + len(s) > MAX_CHARS:
            chunks.append(cur)
            cur = s
        else:
            cur = f"{cur} {s}".strip()
    if cur:
        chunks.append(cur)
    return chunks


def clips_from(script: Path) -> list[str]:
    out = []
    for raw in script.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line.startswith("[दृश्य"):
            continue
        out.extend(split_long(line))
    return out


def main() -> None:
    script, job, out_dir = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3])
    clips = clips_from(script)
    out_dir.mkdir(parents=True, exist_ok=True)
    with (out_dir / "lines.tsv").open("w", encoding="utf-8") as fh:
        for i, text in enumerate(clips, 1):
            fh.write(f"{job}-p{i:03d}\t{text}\n")
    total = sum(len(c) for c in clips)
    print(f"{job}: {len(clips)} clips, {total} characters -> {out_dir / 'lines.tsv'}")


if __name__ == "__main__":
    main()

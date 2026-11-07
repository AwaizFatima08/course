import re
import subprocess
from pathlib import Path

SCRATCH = Path("/tmp/claude-1000/-home-humayun--claude-spares-spare-UfIcvf/ce932540-631a-4ca7-bf85-0e93e80fabf1/scratchpad")
OUT_DIR = Path("/mnt/storage/projects/LLMcourse")
HTML_OUT = SCRATCH / "canva_course.html"
PDF_OUT = OUT_DIR / "Canva_Freelance_Career_Course.pdf"

CSS = """
:root { --ink:#1f2430; --purple:#5b1fb0; --purple-soft:#f1e8ff; --teal:#00a3ab; --teal-soft:#e0f9fa;
        --amber:#d99a00; --amber-soft:#fff4d6; --red:#d64545; --red-soft:#ffe3e3; --grey:#f4f5f8; }
@page { size: A4; margin: 17mm 16mm 19mm 16mm; }
* { -webkit-print-color-adjust: exact; print-color-adjust: exact; box-sizing: border-box; }
body { font-family: "Liberation Sans", Arial, Helvetica, sans-serif; font-size: 10.2pt; line-height: 1.55;
       color: var(--ink); margin: 0; }
p { margin: 0 0 8px; }
ul, ol { margin: 4px 0 10px 4px; padding-left: 20px; }
li { margin-bottom: 3px; }
strong { color: #2a1450; }
section.chapter, section.page { page-break-before: always; }
section.cover { height: 250mm; page-break-after: always; display: flex; flex-direction: column; }

/* Cover */
.cover-tag { font-size: 9pt; letter-spacing: 2px; color: var(--purple); font-weight: bold; margin-top: 10mm; }
.cover-title { font-size: 34pt; line-height: 1.12; color: #2a1450; margin: 10px 0 14px; }
.cover-sub { font-size: 13pt; color: #444; margin-bottom: 14px; }
.cover-art { width: 100%; height: auto; margin: 6px 0 14px; }
.cover-meta { display: flex; gap: 14px; font-size: 9.5pt; margin-top: 8px; }
.cover-meta div { flex: 1; background: var(--grey); border-radius: 8px; padding: 10px 12px; }
.cover-note { margin-top: auto; font-size: 8.5pt; color: #666; border-top: 1px solid #d6dbe6; padding-top: 8px; }

/* Headings */
h2 { font-size: 22pt; color: #2a1450; margin: 2px 0 12px; padding-bottom: 8px;
     border-bottom: 3px solid var(--purple); line-height: 1.2; }
h2.front { font-size: 20pt; }
.chap-no { display: inline-block; font-size: 8.5pt; letter-spacing: 1.5px; text-transform: uppercase;
           color: #fff; background: var(--purple); border-radius: 4px; padding: 2px 8px; margin-bottom: 6px; }
h3 { font-size: 12.5pt; color: var(--purple); margin: 16px 0 6px; page-break-after: avoid; }

/* Boxes */
.box { border-radius: 6px; padding: 8px 12px; margin: 10px 0; background: var(--grey);
       border-left: 5px solid #8a93a6; break-inside: avoid; }
.box.tip { background: #e8f8ef; border-left-color: #2a9d5c; }
.box.warn { background: var(--red-soft); border-left-color: var(--red); }
.box.ex { background: var(--purple-soft); border-left-color: var(--purple); }

/* Tables */
table { width: 100%; border-collapse: collapse; margin: 8px 0 12px; font-size: 9.2pt; }
th { background: #2a1450; color: #fff; text-align: left; padding: 5px 7px; font-weight: bold; }
td { border-bottom: 1px solid #d6dbe6; padding: 5px 7px; vertical-align: top; }
tr { break-inside: avoid; }
tr:nth-child(even) td { background: #fafbfd; }
table.toc td { font-size: 10pt; padding: 6px 7px; }
table.toc td:first-child { width: 36px; color: var(--purple); font-weight: bold; }
table.toc td:last-child { width: 90px; color: #666; text-align: right; }

/* Figures */
figure { margin: 12px 0 14px; break-inside: avoid; }
figure svg { width: 100%; height: auto; display: block; }
figcaption { font-size: 8.8pt; color: #555; margin-top: 4px; font-style: italic; }
"""

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Canva from Zero to a Digital Freelance Career</title>
<style>{css}</style>
</head>
<body>
"""

TAIL = """
</body>
</html>
"""


def clean(fragment: str) -> str:
    # Stray zero-radius circles and the empty groups left behind by them render nothing; drop them.
    fragment = re.sub(r'\s*<circle[^>]*\br="0"\s*/>', "", fragment)
    fragment = re.sub(r'\s*<rect[^>]*\bheight="0"\s*/>', "", fragment)
    for _ in range(3):
        fragment = re.sub(r'\s*<g[^>]*>\s*</g>', "", fragment)
    return fragment


parts = [(SCRATCH / name).read_text(encoding="utf-8") for name in ("part1.html", "part2.html", "part3.html")]
body = clean("\n".join(parts))
HTML_OUT.write_text(HEAD.format(css=CSS) + body + TAIL, encoding="utf-8")

cmd = [
    "google-chrome", "--headless", "--no-sandbox", "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={PDF_OUT}",
    HTML_OUT.as_uri(),
]
result = subprocess.run(cmd, capture_output=True, text=True, timeout=240)
print("chrome exit:", result.returncode)
print(result.stderr[-800:])
print("pdf exists:", PDF_OUT.exists(), PDF_OUT.stat().st_size if PDF_OUT.exists() else 0)

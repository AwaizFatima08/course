"""Assemble the Shopify course HTML from src/ fragments and render it to PDF with headless Chrome."""
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent
SRC = ROOT / "src"
OUT_HTML = ROOT / "Shopify_Ecommerce_Career_Course.html"
OUT_PDF = ROOT / "Shopify_Ecommerce_Career_Course.pdf"

CHAPTERS = [
    ("1", "Welcome to E-commerce and Shopify"),
    ("2", "E-commerce Business Foundations"),
    ("3", "Setting Up Your Shopify Store"),
    ("4", "Navigating the Shopify Admin"),
    ("5", "Products, Collections and Inventory"),
    ("6", "Store Design with Themes"),
    ("7", "Apps, Integrations and Customisation"),
    ("8", "Payments, Checkout, Taxes and Policies"),
    ("9", "Shipping, Fulfilment and Returns"),
    ("10", "Marketing Your Store"),
    ("11", "Analytics, Conversion and Growth"),
    ("12", "Scaling, International Sales and Retail"),
    ("13", "Building an E-commerce Career with Shopify"),
    ("14", "Capstone Project and 90-Day Action Plan"),
]

CSS = """
@page { size: A4; margin: 20mm 17mm 20mm 17mm;
  @bottom-left { content: "Shopify and E-commerce Career Course"; font-size: 8pt; color: #7a8178; }
  @bottom-right { content: "Page " counter(page); font-size: 8pt; color: #7a8178; } }
@page cover { margin: 0; @bottom-left { content: none; } @bottom-right { content: none; } }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: "Liberation Sans", Arial, Helvetica, sans-serif; font-size: 10pt;
  line-height: 1.55; color: #1d2b1f; margin: 0; }
.cover { page: cover; height: 297mm; box-sizing: border-box; padding: 34mm 22mm;
  background: #1d2b1f; color: #eef6e3; display: flex; flex-direction: column; justify-content: space-between; }
.cover .brand { color: #95BF47; font-size: 11pt; letter-spacing: 3px; text-transform: uppercase; font-weight: bold; }
.cover h1 { font-size: 34pt; line-height: 1.15; color: #fff; margin: 10mm 0 6mm; }
.cover .sub { font-size: 13pt; color: #cfe3b0; }
.cover .meta { font-size: 10pt; color: #aab5ab; border-top: 1px solid #3a4a3e; padding-top: 6mm; }
.cover .bar { height: 6mm; width: 60mm; background: #95BF47; border-radius: 3px; margin-bottom: 8mm; }
.toc { page-break-before: always; }
.toc h2.toc-title { font-size: 20pt; color: #1d2b1f; border: none; margin-top: 0; }
.toc ol { list-style: none; padding: 0; margin: 0; }
.toc li { display: flex; gap: 10px; padding: 7px 0; border-bottom: 1px solid #e0e4dd; font-size: 11pt; }
.toc .n { width: 34px; color: #5E8E3E; font-weight: bold; }
.toc .how { margin-top: 14px; font-size: 9.5pt; color: #444; }
.chapter { page-break-before: always; }
.chapter-head { background: #1d2b1f; color: #fff; padding: 12px 16px; border-radius: 6px;
  border-left: 6px solid #95BF47; margin-bottom: 12px; page-break-after: avoid; }
.chapter-head h1 { color: #fff; font-size: 20pt; margin: 2px 0 0; line-height: 1.2; }
.num { color: #95BF47; font-size: 9pt; letter-spacing: 1.5px; text-transform: uppercase; font-weight: bold; }
h2 { color: #3f6328; font-size: 13.5pt; border-bottom: 1px solid #d7dbd5; padding-bottom: 3px;
  margin: 18px 0 6px; page-break-after: avoid; }
h3 { color: #1d2b1f; font-size: 11pt; margin: 12px 0 4px; page-break-after: avoid; }
.lead { font-size: 10.8pt; color: #333; border-left: 3px solid #95BF47; padding-left: 10px; margin: 0 0 8px; }
p { margin: 5px 0; }
ul, ol { margin: 5px 0 5px 18px; padding-left: 4px; }
li { margin: 3px 0; }
table { width: 100%; border-collapse: collapse; font-size: 8.8pt; margin: 8px 0 12px; }
th { background: #5E8E3E; color: #fff; text-align: left; padding: 5px 6px; }
td { border-bottom: 1px solid #e0e4dd; padding: 5px 6px; vertical-align: top; }
tr { page-break-inside: avoid; }
tr:nth-child(even) td { background: #f7f9f5; }
figure { margin: 12px 0; page-break-inside: avoid; text-align: center; }
figure svg { width: 100%; height: auto; }
figcaption { font-size: 8.5pt; color: #555; font-style: italic; margin-top: 4px; }
.box { padding: 9px 12px; border-radius: 6px; margin: 12px 0; page-break-inside: avoid; font-size: 9.4pt; }
.box p { margin: 3px 0; }
.box.tip { background: #eef4fb; border-left: 4px solid #5C7FA8; }
.box.warn { background: #fdf1ec; border-left: 4px solid #C0583D; }
.box.try { background: #f3f8ea; border-left: 4px solid #5E8E3E; }
.box.takeaway { background: #1d2b1f; color: #eef6e3; border-left: 4px solid #95BF47; }
.box.takeaway strong { color: #95BF47; }
pre { background: #f4f5f2; border: 1px solid #dfe3dc; padding: 8px 10px; border-radius: 4px;
  font-size: 8.2pt; line-height: 1.4; white-space: pre-wrap; page-break-inside: avoid; }
code { font-family: "Liberation Mono", "DejaVu Sans Mono", monospace; font-size: 8.6pt; }
p code, li code { background: #f1f3ef; padding: 0 3px; border-radius: 2px; }
pre code { background: none; padding: 0; }
.appendix .chapter-head { background: #3f6328; }
"""

def build_toc():
    items = "\n".join(
        f'<li><span class="n">{num}</span><span>{title}</span></li>' for num, title in CHAPTERS
    )
    items += '\n<li><span class="n">A</span><span>Glossary of Terms</span></li>'
    return f"""<section class="toc">
<h2 class="toc-title">Contents</h2>
<ol>
{items}
</ol>
<p class="how">Each chapter has: a short introduction, the core concepts with tables and drawings, a common mistake to avoid, key takeaways, and a practice task. Work through the chapters in order; the capstone in Chapter 14 brings every earlier chapter together.</p>
</section>"""

COVER = """<section class="cover">
<div>
<div class="brand">Complete Beginner's Course</div>
<h1>Shopify and E-commerce Career Course</h1>
<div class="bar"></div>
<div class="sub">From business foundations to building a career in online retail with Shopify</div>
</div>
<div class="meta">14 chapters &middot; Designed for learners with basic computer knowledge &middot; No coding experience required<br>
Edition: November 2026. Shopify features, plans and fees change over time; check current details on shopify.com before making decisions.</div>
</section>"""

def main():
    parts = [SRC / f"part{i}.html" for i in range(1, 5)]
    body = "\n".join(p.read_text(encoding="utf-8") for p in parts)
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Shopify and E-commerce Career Course</title>
<style>{CSS}</style>
</head>
<body>
{COVER}
{build_toc()}
{body}
</body>
</html>
"""
    OUT_HTML.write_text(html, encoding="utf-8")
    cmd = [
        "google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu",
        "--no-pdf-header-footer", f"--print-to-pdf={OUT_PDF}", OUT_HTML.as_uri(),
    ]
    subprocess.run(cmd, check=True, timeout=240)
    print("Wrote", OUT_PDF)

if __name__ == "__main__":
    main()

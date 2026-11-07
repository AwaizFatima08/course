"""Assemble the Urdu course HTML (RTL) from urdu/ fragments, reuse the English SVG drawings, render to PDF."""
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent
SRC = ROOT / "src"
URDU = ROOT / "urdu"
OUT_HTML = ROOT / "Shopify_Ecommerce_Career_Course_Urdu.html"
OUT_PDF = ROOT / "Shopify_Ecommerce_Career_Course_Urdu.pdf"

CHAPTERS = [
    ("1", "ای کامرس اور شاپیفائی میں خوش آمدید"),
    ("2", "ای کامرس کاروبار کی بنیادیں"),
    ("3", "اپنا شاپیفائی اسٹور ترتیب دینا"),
    ("4", "شاپیفائی ایڈمن میں راستہ تلاش کرنا"),
    ("5", "پروڈکٹس، کلیکشنز اور انوینٹری"),
    ("6", "تھیمز کے ساتھ اسٹور کا ڈیزائن"),
    ("7", "ایپس، انٹیگریشنز اور حسبِ ضرورت ترتیب"),
    ("8", "ادائیگیاں، چیک آؤٹ، ٹیکس اور پالیسیاں"),
    ("9", "شپنگ، تکمیلِ آرڈر اور واپسیاں"),
    ("10", "اپنے اسٹور کی مارکیٹنگ"),
    ("11", "تجزیہ، کنورژن اور ترقی"),
    ("12", "توسیع، بین الاقوامی فروخت اور ریٹیل"),
    ("13", "شاپیفائی کے ساتھ ای کامرس کیریئر بنانا"),
    ("14", "کیپسٹون پروجیکٹ اور 90 دن کا عملی منصوبہ"),
]

CSS = """
@page { size: A4; margin: 20mm 17mm 20mm 17mm;
  @bottom-center { content: "شاپیفائی اور ای کامرس کیریئر کورس  |  صفحہ " counter(page); font-size: 8pt; color: #7a8178; font-family: "Noto Naskh Arabic", sans-serif; } }
@page cover { margin: 0; @bottom-center { content: none; } }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: "Noto Naskh Arabic", "Amiri", serif; font-size: 11pt; line-height: 1.95;
  color: #1d2b1f; margin: 0; direction: rtl; text-align: right; }
.cover { page: cover; height: 297mm; box-sizing: border-box; padding: 34mm 22mm;
  background: #1d2b1f; color: #eef6e3; display: flex; flex-direction: column; justify-content: space-between; text-align: right; }
.cover .brand { color: #95BF47; font-size: 13pt; font-weight: bold; }
.cover h1 { font-size: 32pt; line-height: 1.5; color: #fff; margin: 10mm 0 6mm; }
.cover .sub { font-size: 14pt; color: #cfe3b0; line-height: 1.9; }
.cover .meta { font-size: 10.5pt; color: #aab5ab; border-top: 1px solid #3a4a3e; padding-top: 6mm; line-height: 1.9; }
.cover .bar { height: 6mm; width: 60mm; background: #95BF47; border-radius: 3px; margin-bottom: 8mm; margin-left: auto; }
.toc { page-break-before: always; }
.toc h2.toc-title { font-size: 22pt; color: #1d2b1f; border: none; margin-top: 0; }
.toc ol { list-style: none; padding: 0; margin: 0; }
.toc li { display: flex; gap: 10px; padding: 7px 0; border-bottom: 1px solid #e0e4dd; font-size: 12pt; }
.toc .n { min-width: 34px; color: #5E8E3E; font-weight: bold; }
.toc .how { margin-top: 14px; font-size: 10.5pt; color: #444; }
.chapter { page-break-before: always; }
.chapter-head { background: #1d2b1f; color: #fff; padding: 12px 16px; border-radius: 6px;
  border-right: 6px solid #95BF47; margin-bottom: 12px; page-break-after: avoid; }
.chapter-head h1 { color: #fff; font-size: 21pt; margin: 2px 0 0; line-height: 1.6; }
.num { color: #95BF47; font-size: 11pt; font-weight: bold; }
h2 { color: #3f6328; font-size: 14pt; border-bottom: 1px solid #d7dbd5; padding-bottom: 3px;
  margin: 18px 0 6px; page-break-after: avoid; }
h3 { color: #1d2b1f; font-size: 12pt; margin: 12px 0 4px; page-break-after: avoid; }
.lead { font-size: 11.5pt; color: #333; border-right: 3px solid #95BF47; padding-right: 10px; margin: 0 0 8px; }
p { margin: 5px 0; }
ul, ol { margin: 5px 0 5px 0; padding-right: 22px; padding-left: 0; }
li { margin: 3px 0; }
table { width: 100%; border-collapse: collapse; font-size: 9.6pt; line-height: 1.7; margin: 8px 0 12px; }
th { background: #5E8E3E; color: #fff; text-align: right; padding: 5px 6px; }
td { border-bottom: 1px solid #e0e4dd; padding: 5px 6px; vertical-align: top; text-align: right; }
tr { page-break-inside: avoid; }
tr:nth-child(even) td { background: #f7f9f5; }
figure { margin: 12px 0; page-break-inside: avoid; text-align: center; direction: ltr; }
figure svg { width: 100%; height: auto; }
figcaption { font-size: 9.5pt; color: #555; margin-top: 4px; direction: rtl; }
.box { padding: 9px 12px; border-radius: 6px; margin: 12px 0; page-break-inside: avoid; font-size: 10.4pt; }
.box p { margin: 3px 0; }
.box.tip { background: #eef4fb; border-right: 4px solid #5C7FA8; }
.box.warn { background: #fdf1ec; border-right: 4px solid #C0583D; }
.box.try { background: #f3f8ea; border-right: 4px solid #5E8E3E; }
.box.takeaway { background: #1d2b1f; color: #eef6e3; border-right: 4px solid #95BF47; }
.box.takeaway strong { color: #95BF47; }
pre { direction: ltr; text-align: left; background: #f4f5f2; border: 1px solid #dfe3dc; padding: 8px 10px; border-radius: 4px;
  font-size: 8.4pt; line-height: 1.4; white-space: pre-wrap; page-break-inside: avoid; font-family: "Liberation Mono", monospace; }
code { direction: ltr; font-family: "Liberation Mono", "DejaVu Sans Mono", monospace; font-size: 9pt; }
p code, li code { background: #f1f3ef; padding: 0 3px; border-radius: 2px; }
pre code { background: none; padding: 0; }
.appendix .chapter-head { background: #3f6328; }
"""


def english_svgs():
    """Collect the 14 English SVG drawings, in order, from the English source parts."""
    text = "\n".join((SRC / f"part{i}.html").read_text(encoding="utf-8") for i in range(1, 5))
    svgs = re.findall(r"<svg\b.*?</svg>", text, flags=re.DOTALL)
    return svgs


def build_toc():
    items = "\n".join(
        f'<li><span class="n">{num}</span><span>{title}</span></li>' for num, title in CHAPTERS
    )
    items += '\n<li><span class="n">ض</span><span>اصطلاحات کی فرہنگ</span></li>'
    return f"""<section class="toc">
<h2 class="toc-title">فہرست مضامین</h2>
<ol>
{items}
</ol>
<p class="how">ہر باب میں یہ شامل ہے: مختصر تعارف، جدولوں اور تصاویر کے ساتھ بنیادی تصورات، ایک عام غلطی سے بچاؤ، اہم نکات، اور ایک عملی کام۔ ابواب کو ترتیب سے پڑھیں؛ باب 14 کا کیپسٹون پچھلے تمام ابواب کو یکجا کرتا ہے۔ شکلوں کے اندر کے لیبل انگریزی میں ہیں تاکہ شاپیفائی کی اصطلاحات درست رہیں۔</p>
</section>"""


COVER = """<section class="cover">
<div>
<div class="brand">مکمل ابتدائی کورس</div>
<h1>شاپیفائی اور ای کامرس کیریئر کورس</h1>
<div class="bar"></div>
<div class="sub">کاروباری بنیادوں سے لے کر شاپیفائی کے ساتھ آن لائن ریٹیل میں کیریئر بنانے تک</div>
</div>
<div class="meta">14 ابواب &middot; بنیادی کمپیوٹر علم رکھنے والے سیکھنے والوں کے لیے &middot; کوڈنگ کا تجربہ ضروری نہیں<br>
ایڈیشن: نومبر 2026۔ شاپیفائی کے فیچرز، پلانز اور فیسیں وقت کے ساتھ بدلتی ہیں؛ فیصلہ کرنے سے پہلے shopify.com پر موجودہ تفصیلات ضرور دیکھیں۔</div>
</section>"""


def main():
    parts = [URDU / f"ur{i}.html" for i in range(1, 5)]
    body = "\n".join(p.read_text(encoding="utf-8") for p in parts)

    svgs = english_svgs()
    placeholders = body.count("<!--SVG-->")
    if len(svgs) != placeholders:
        raise SystemExit(f"SVG count mismatch: {len(svgs)} English drawings vs {placeholders} placeholders")
    it = iter(svgs)
    body = re.sub(r"<!--SVG-->", lambda _m: next(it), body)

    html = f"""<!doctype html>
<html lang="ur" dir="rtl">
<head>
<meta charset="utf-8">
<title>شاپیفائی اور ای کامرس کیریئر کورس</title>
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

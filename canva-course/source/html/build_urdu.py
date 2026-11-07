import re
import subprocess
from pathlib import Path

SCRATCH = Path("/tmp/claude-1000/-home-humayun--claude-spares-spare-UfIcvf/ce932540-631a-4ca7-bf85-0e93e80fabf1/scratchpad")
OUT_DIR = Path("/mnt/storage/projects/LLMcourse")
HTML_OUT = SCRATCH / "canva_course_urdu.html"
PDF_OUT = OUT_DIR / "Canva_Freelance_Career_Course_Urdu.pdf"

# Labels inside the English drawings -> Urdu. Exact text-node matches only; brand names stay in English.
LABELS = {
    "Canva and design": "Canva اور ڈیزائن", "basics": "بنیادی باتیں",
    "1. Learn": "1. سیکھیں", "2. Practise": "2. مشق کریں", "3. Win clients": "3. کلائنٹ حاصل کریں", "4. Earn": "4. کمائیں",
    "Build 8 to 10": "8 سے 10 بنائیں", "portfolio pieces": "پورٹ فولیو کام", "Platforms, local": "پلیٹ فارمز، مقامی",
    "referrals": "ریفرل", "Repeat clients,": "دوبارہ کلائنٹس،", "higher prices": "زیادہ قیمتیں",
    "Most people spend 2 to 4 months moving from step 1 to the first paid job.":
        "زیادہ تر لوگ پہلے ادا شدہ کام تک پہنچنے میں 2 سے 4 مہینے لگاتے ہیں۔",
    "Search Canva": "Canva تلاش کریں", "Home": "ہوم", "Templates": "ٹیمپلیٹس", "Brand": "برانڈ", "Projects": "پروجیکٹس",
    "Apps": "ایپس", "Trash": "ردی", "Create a design": "نیا ڈیزائن بنائیں",
    "Recent designs and templates appear here": "حالیہ ڈیزائن اور ٹیمپلیٹس یہاں ظاہر ہوں گے",
    "Resize · File · Share": "سائز · فائل · شیئر", "Share": "شیئر",
    "Context toolbar: font · size · colour · align · effects (changes with what is selected)":
        "سیاق و سباق کی ٹول بار: فونٹ · سائز · رنگ · الائن · اثرات (منتخب چیز کے مطابق بدلتی ہے)",
    "Design": "ڈیزائن", "Elements": "عناصر", "Text": "ٹیکسٹ", "Uploads": "اپ لوڈز", "Photos": "تصاویر",
    "Open": "کھلا", "Summer": "موسم", "Sale": "سیل", "Subheading goes here": "ذیلی عنوان یہاں", "Pages": "صفحات",
    "Headline here": "یہاں ہیڈ لائن", "Rule of thirds": "تہائی کا اصول (Rule of thirds)",
    "The purple lines divide the page into nine": "جامنی لکیریں صفحے کو نو",
    "equal parts. The red dot sits on an intersection,": "برابر حصوں میں تقسیم کرتی ہیں۔ سرخ نقطہ تقاطع پر ہے،",
    "a stronger position than dead centre.": "یہ درمیان سے زیادہ مؤثر جگہ ہے۔",
    "Headlines usually sit on the top third line,": "ہیڈ لائنز عموماً اوپر کی تہائی لکیر پر ہوتی ہیں،",
    "and the main image or subject on one of the": "اور مرکزی تصویر یا موضوع نچلے",
    "lower intersections.": "تقاطعوں میں سے کسی ایک پر۔",
    "Headline": "ہیڈ لائن", "Subheading": "ذیلی عنوان",
    "Body text is easy to read at normal size.": "باڈی ٹیکسٹ عام سائز پر پڑھنے میں آسان ہے۔",
    "Keep line length moderate and spacing generous.": "سطر کی لمبائی معتدل اور فاصلہ کھلا رکھیں۔",
    "CAPTION OR SOURCE NOTE": "کیپشن یا ماخذ کا نوٹ", "Typical sizes for a poster": "پوسٹر کے عام سائز",
    "Headline: 60 to 120 pt": "ہیڈ لائن: 60 تا 120 pt", "Subheading: 30 to 48 pt": "ذیلی عنوان: 30 تا 48 pt",
    "Body: 14 to 22 pt": "باڈی: 14 تا 22 pt", "Caption: 10 to 12 pt": "کیپشن: 10 تا 12 pt",
    "On a phone screen, body text below": "فون کی اسکرین پر باڈی ٹیکسٹ جو",
    "about 24 px is hard to read.": "تقریباً 24 px سے چھوٹا ہو تو پڑھنا مشکل ہے۔",
    "Use the same sizes for the same jobs": "ایک جیسے کام کے لیے ایک جیسے سائز رکھیں",
    "across all your designs.": "اپنے تمام ڈیزائنز میں۔",
    "Complementary": "متضاد (Complementary)", "opposites: bold contrast": "آمنے سامنے: بولڈ تضاد",
    "Analogous": "ملتے جلتے (Analogous)", "neighbours: calm and warm": "ساتھ والے: پرسکون اور گرم",
    "Triadic": "سہ رنگی (Triadic)", "three evenly spaced: lively": "برابر فاصلے پر تین: جاندار",
    "Square": "مربع", "feed post": "فیڈ پوسٹ", "Portrait": "عمودی", "taller feed post": "لمبی فیڈ پوسٹ",
    "Story / Reel": "اسٹوری / ریل", "full-screen vertical": "پوری اسکرین، عمودی",
    "Your name · one-line promise": "آپ کا نام · ایک سطری وعدہ",
    'e.g. "I design menus and social posts that help local cafes sell more."':
        'مثال: "میں مینیو اور سوشل پوسٹس بناتا ہوں جو مقامی کیفے کو زیادہ فروخت دلائیں۔"',
    "Selected work": "منتخب کام", "3 to 6 case studies": "3 تا 6 case studies",
    "Services and prices": "خدمات اور قیمتیں", "• Social post packs": "• سوشل پوسٹ پیکس",
    "• Flyers and menus": "• فلائر اور مینیو", "• Presentations": "• پریزنٹیشنز",
    "• Starting from: (your rate)": "• شروع قیمت: (آپ کی شرح)", "Packages: see Chapter 9": "پیکیجز: باب 9 دیکھیں",
    "About and proof": "تعارف اور ثبوت", "Short bio and photo": "مختصر بایو اور تصویر",
    "2 to 3 testimonials": "2 تا 3 تعریفی بیانات", "Tools you use": "آپ کے استعمال کے ٹولز",
    "Contact button": "رابطے کا بٹن",
    "start here": "یہاں سے شروع کریں", "UI and web": "UI اور ویب",
    "Learn Canva basics": "Canva کی بنیادیں سیکھیں", "Practice projects 1–7": "مشق کے پروجیکٹس 1–7",
    "Portfolio (8 pieces)": "پورٹ فولیو (8 کام)", "Profiles on 2 platforms": "2 پلیٹ فارمز پر پروفائلز",
    "First clients or gigs": "پہلے کلائنٹس یا gigs", "Pricing and contracts": "قیمت اور معاہدے",
    "Review and plan next 90 days": "جائزہ اور اگلے 90 دن کا منصوبہ",
    "Your first design": "آپ کا پہلا ڈیزائن",
}

CSS = """
@page { size: A4; margin: 17mm 16mm 19mm 16mm; }
* { -webkit-print-color-adjust: exact; print-color-adjust: exact; box-sizing: border-box; }
:root { --ink:#1f2430; --purple:#5b1fb0; --purple-soft:#f1e8ff; --grey:#f4f5f8; }
html, body { direction: rtl; }
body { font-family: "Noto Naskh Arabic", serif; font-size: 10.5pt; line-height: 1.9;
       color: var(--ink); margin: 0; text-align: right; }
h1, h2, h3, .chap-no, .cover-tag, th { font-family: "Noto Naskh Arabic", serif; }
p { margin: 0 0 8px; }
ul, ol { margin: 4px 4px 10px 0; padding-right: 22px; padding-left: 0; }
li { margin-bottom: 3px; }
strong { color: #2a1450; }
section.chapter, section.page { page-break-before: always; }
section.cover { height: 250mm; page-break-after: always; display: flex; flex-direction: column; }

/* Cover */
.cover-tag { font-size: 10pt; letter-spacing: 0; color: var(--purple); font-weight: bold; margin-top: 10mm; }
.cover-title { font-size: 34pt; line-height: 1.5; color: #2a1450; margin: 6px 0 10px; font-family: "Noto Naskh Arabic", serif; font-weight: bold; }
.cover-sub { font-size: 13pt; color: #444; margin-bottom: 12px; }
.cover-art { width: 100%; height: auto; margin: 6px 0 14px; }
.cover-meta { display: flex; gap: 14px; font-size: 10pt; line-height: 1.9; margin-top: 8px; }
.cover-meta div { flex: 1; background: var(--grey); border-radius: 8px; padding: 10px 12px; }
.cover-note { margin-top: auto; font-size: 9.5pt; color: #666; border-top: 1px solid #d6dbe6; padding-top: 8px; }

/* Headings */
h2 { font-size: 22pt; color: #2a1450; margin: 2px 0 12px; padding-bottom: 8px; line-height: 1.5;
     border-bottom: 3px solid var(--purple); font-weight: bold; }
h2.front { font-size: 20pt; }
.chap-no { display: inline-block; font-size: 10pt; color: #fff; background: var(--purple); border-radius: 4px; padding: 2px 10px; margin-bottom: 6px; }
h3 { font-size: 14pt; color: var(--purple); margin: 14px 0 6px; page-break-after: avoid; font-weight: bold; line-height: 1.7; }

/* Boxes */
.box { border-radius: 6px; padding: 8px 12px; margin: 10px 0; background: var(--grey);
       border-right: 5px solid #8a93a6; break-inside: avoid; }
.box.tip { background: #e8f8ef; border-right-color: #2a9d5c; }
.box.warn { background: #ffe3e3; border-right-color: #d64545; }
.box.ex { background: var(--purple-soft); border-right-color: var(--purple); }

/* Tables */
table { width: 100%; border-collapse: collapse; margin: 8px 0 12px; font-size: 9.2pt; line-height: 1.7; }
th { background: #2a1450; color: #fff; text-align: right; padding: 5px 7px; font-weight: bold; }
td { border-bottom: 1px solid #d6dbe6; padding: 5px 7px; vertical-align: top; text-align: right; }
tr { break-inside: avoid; }
tr:nth-child(even) td { background: #fafbfd; }
table.toc td { font-size: 11pt; padding: 6px 7px; }
table.toc td:first-child { width: 40px; color: var(--purple); font-weight: bold; text-align: left; }
table.toc td:last-child { width: 80px; color: #666; text-align: left; }

/* Figures: drawings keep their own left-to-right geometry; their labels use an Urdu font */
figure { margin: 12px 0 14px; break-inside: avoid; direction: ltr; }
svg { direction: ltr; }
figure svg { width: 100%; height: auto; display: block; font-family: "Noto Naskh Arabic", "Arial", sans-serif; }
.cover-art { font-family: "Noto Naskh Arabic", "Arial", sans-serif; }
figcaption { font-size: 10pt; color: #555; margin-top: 4px; direction: rtl; text-align: right; line-height: 1.9; }
"""

HEAD = """<!doctype html>
<html lang="ur" dir="rtl">
<head>
<meta charset="utf-8">
<title>Canva سے ڈیجیٹل فری لانس کیریئر تک</title>
<style>{css}</style>
</head>
<body>
"""

TAIL = "\n</body>\n</html>\n"

ENG = [(SCRATCH / n).read_text(encoding="utf-8") for n in ("part1.html", "part2.html", "part3.html")]
ENG_ALL = "\n".join(ENG)


def clean(fragment: str) -> str:
    fragment = re.sub(r'\s*<circle[^>]*\br="0"\s*/>', "", fragment)
    fragment = re.sub(r'\s*<rect[^>]*\bheight="0"\s*/>', "", fragment)
    for _ in range(3):
        fragment = re.sub(r'\s*<g[^>]*>\s*</g>', "", fragment)
    return fragment


def translate_labels(svg: str) -> str:
    def repl(match):
        text = match.group(1)
        return ">" + LABELS.get(text, text) + "<"
    return re.sub(r">([^<>]+)<", repl, svg)


def english_svg(num: str) -> str:
    m = re.search(r'<figure>\s*(<svg(?:(?!</svg>).)*</svg>)\s*<figcaption>Figure ' + re.escape(num) + r'\b', ENG_ALL, re.S)
    if not m:
        raise SystemExit(f"figure {num} not found in English source")
    return m.group(1)


def cover_svg() -> str:
    m = re.search(r'<svg viewBox="0 0 600 220" class="cover-art".*?</svg>', ENG_ALL, re.S)
    if not m:
        raise SystemExit("cover art not found")
    return m.group(0)


def place_figure(match):
    num, caption = match.group(1), match.group(2)
    svg = translate_labels(english_svg(num))
    return f"<figure>{svg}<figcaption>{caption}</figcaption></figure>"


urdu = "\n".join(
    (SCRATCH / n).read_text(encoding="utf-8") for n in ("urdu1.html", "urdu2.html", "urdu3.html")
)
urdu = re.sub(r"<!--FIG (\d+\.\d+)\|(.*?)-->", place_figure, urdu, flags=re.S)
urdu = urdu.replace("<!--COVER-->", translate_labels(cover_svg()))
urdu = clean(urdu)

HTML_OUT.write_text(HEAD.format(css=CSS) + urdu + TAIL, encoding="utf-8")

cmd = [
    "google-chrome", "--headless", "--no-sandbox", "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={PDF_OUT}",
    HTML_OUT.as_uri(),
]
result = subprocess.run(cmd, capture_output=True, text=True, timeout=240)
print("chrome exit:", result.returncode)
print("pdf exists:", PDF_OUT.exists(), PDF_OUT.stat().st_size if PDF_OUT.exists() else 0)

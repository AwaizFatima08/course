import sys, os
SCR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCR)
from content_ur import CHAPTERS
import arabic_reshaper
from bidi.algorithm import get_display
from PIL import Image as PILImage
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image,
                                Table, TableStyle, KeepTogether)

NS = "/usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf"
NSB = "/usr/share/fonts/truetype/noto/NotoNaskhArabic-Bold.ttf"
pdfmetrics.registerFont(TTFont("NS", NS))
pdfmetrics.registerFont(TTFont("NSB", NSB))
registerFontFamily("NS", normal="NS", bold="NSB", italic="NS", boldItalic="NSB")

PLUM = colors.HexColor("#7B2D5C"); TEAL = colors.HexColor("#1F7A7A"); CORAL = colors.HexColor("#E07A5F")
SAND = colors.HexColor("#F6EFE6"); MINT = colors.HexColor("#D8EFEA"); DARK = colors.HexColor("#2B2B2B")
GREY = colors.HexColor("#6B6B6B")
OUT = "/mnt/storage/projects/LLMcourse/Digital_Career_Course_Urdu.pdf"
FIGDIR = os.path.join(SCR, "figs_ur")

W, H = A4
M = 2 * cm
FW = W - 2 * M

def shape(s):
    return get_display(arabic_reshaper.reshape(s))

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def wrap_ur(text, width, font, size):
    """Wrap logical Urdu text into lines that fit width, then reorder each line for display.
    Returns escaped markup with lines joined by <br/> (logical line order preserved)."""
    lines, cur = [], ""
    for word in text.split():
        cand = (cur + " " + word).strip()
        if cur and pdfmetrics.stringWidth(shape(cand), font, size) > width:
            lines.append(cur); cur = word
        else:
            cur = cand
    if cur:
        lines.append(cur)
    return "<br/>".join(esc(shape(l)) for l in lines)

st = {
 "body": ParagraphStyle("body", fontName="NS", fontSize=11.5, leading=20, textColor=DARK, spaceAfter=8, alignment=TA_RIGHT),
 "chap": ParagraphStyle("chap", fontName="NSB", fontSize=21, leading=34, textColor=PLUM, spaceAfter=4, alignment=TA_RIGHT, keepWithNext=1),
 "num": ParagraphStyle("num", fontName="NSB", fontSize=10.5, leading=16, textColor=CORAL, spaceAfter=2, alignment=TA_RIGHT),
 "intro": ParagraphStyle("intro", fontName="NS", fontSize=11.5, leading=20, textColor=GREY, spaceAfter=12, alignment=TA_RIGHT),
 "h": ParagraphStyle("h", fontName="NSB", fontSize=13.5, leading=24, textColor=TEAL, spaceBefore=10, spaceAfter=5, alignment=TA_RIGHT, keepWithNext=1),
 "li": ParagraphStyle("li", fontName="NS", fontSize=11.5, leading=20, textColor=DARK, rightIndent=18, spaceAfter=3, alignment=TA_RIGHT),
 "cell": ParagraphStyle("cell", fontName="NS", fontSize=10, leading=17, textColor=DARK, alignment=TA_RIGHT),
 "cellh": ParagraphStyle("cellh", fontName="NSB", fontSize=10.5, leading=17, textColor=colors.white, alignment=TA_RIGHT),
 "cap": ParagraphStyle("cap", fontName="NS", fontSize=9.5, leading=16, textColor=GREY, alignment=TA_CENTER, spaceBefore=3, spaceAfter=12),
 "box": ParagraphStyle("box", fontName="NS", fontSize=10.8, leading=19, textColor=DARK, alignment=TA_RIGHT),
 "toc": ParagraphStyle("toc", fontName="NS", fontSize=12.5, leading=26, textColor=DARK, alignment=TA_RIGHT),
}

def table_block(rows, widths):
    total = sum(widths)
    cw = [FW * w / total for w in widths]
    # RTL: the first logical column sits on the right.
    cw_vis = list(reversed(cw))
    data = []
    for i, r in enumerate(rows):
        cells = list(reversed(r))
        row = []
        for j, c in enumerate(cells):
            style = st["cellh"] if i == 0 else st["cell"]
            width = cw_vis[j] - 12
            row.append(Paragraph(wrap_ur(c, width, style.fontName, style.fontSize), style))
        data.append(row)
    t = Table(data, colWidths=cw_vis, repeatRows=1)
    ts = [("BACKGROUND", (0, 0), (-1, 0), PLUM),
          ("VALIGN", (0, 0), (-1, -1), "TOP"),
          ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#CFC7BC")),
          ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
          ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6)]
    for i in range(1, len(rows)):
        if i % 2 == 0:
            ts.append(("BACKGROUND", (0, i), (-1, i), colors.HexColor("#FBF8F4")))
    t.setStyle(TableStyle(ts))
    return t

def box_block(text, bg, bar, label=None):
    width = FW - 24
    lines = text.split("\n")
    parts = []
    if label:
        parts.append(f"<b>{esc(shape(label))}</b>" + wrap_ur(lines[0], width, "NS", 10.8))
    else:
        parts.append(f"<b>{wrap_ur(lines[0], width, 'NSB', 10.8)}</b>" if len(lines) > 1 else wrap_ur(lines[0], width, "NS", 10.8))
    for ln in lines[1:]:
        parts.append(wrap_ur(ln, width, "NS", 10.8))
    p = Paragraph("<br/>".join(parts), st["box"])
    t = Table([[p]], colWidths=[FW])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), bg),
                           ("LINEAFTER", (-1, 0), (-1, -1), 3, bar),
                           ("LEFTPADDING", (0, 0), (-1, -1), 12), ("RIGHTPADDING", (0, 0), (-1, -1), 12),
                           ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]))
    return t

def image_block(path, caption):
    pw, ph = PILImage.open(path).size
    width = FW * 0.78
    height = width * ph / pw
    max_h = 17.5 * cm
    if height > max_h:
        height = max_h
        width = height * pw / ph
    img = Image(path, width=width, height=height)
    img.hAlign = "CENTER"
    cap = Paragraph(wrap_ur(caption, FW, "NS", 9.5), st["cap"])
    return KeepTogether([img, cap])

def chapter_story(num, title, intro, blocks):
    story = [Paragraph(esc(shape(f"باب {num}")), st["num"]),
             Paragraph(wrap_ur(title, FW, "NSB", 21), st["chap"]),
             Paragraph(wrap_ur(intro, FW, "NS", 11.5), st["intro"])]
    li_w = FW - 22
    for b in blocks:
        kind = b[0]
        if kind == "h":
            story.append(Paragraph(wrap_ur(b[1], FW, "NSB", 13.5), st["h"]))
        elif kind == "p":
            story.append(Paragraph(wrap_ur(b[1], FW, "NS", 11.5), st["body"]))
        elif kind == "ul":
            for item in b[1]:
                story.append(Paragraph(wrap_ur("• " + item, li_w, "NS", 11.5), st["li"]))
            story.append(Spacer(1, 4))
        elif kind == "ol":
            for k, item in enumerate(b[1], 1):
                story.append(Paragraph(wrap_ur(f"{k}. " + item, li_w, "NS", 11.5), st["li"]))
            story.append(Spacer(1, 4))
        elif kind == "check":
            for item in b[1]:
                story.append(Paragraph(wrap_ur("☐ " + item, li_w, "NS", 11.5), st["li"]))
            story.append(Spacer(1, 4))
        elif kind == "table":
            story.append(table_block(b[1], b[2] if len(b) > 2 else [1] * len(b[1][0])))
            story.append(Spacer(1, 8))
        elif kind == "tip":
            story.append(box_block(b[1], MINT, TEAL, label="نکتہ: "))
            story.append(Spacer(1, 8))
        elif kind == "box":
            story.append(box_block(b[1], SAND, CORAL))
            story.append(Spacer(1, 8))
        elif kind == "img":
            story.append(image_block(os.path.join(FIGDIR, os.path.basename(b[1])), b[2]))
    return story

def on_page(canv, doc):
    canv.saveState()
    if doc.page > 1:
        canv.setFont("NS", 8.5)
        canv.setFillColor(GREY)
        canv.drawRightString(W - M, 1.1 * cm, shape("ڈیجیٹل کیریئر کورس برائے گھریلو خواتین"))
        canv.drawString(M, 1.1 * cm, shape(f"صفحہ {doc.page}"))
        canv.setStrokeColor(MINT); canv.setLineWidth(1)
        canv.line(M, 1.5 * cm, W - M, 1.5 * cm)
    canv.restoreState()

def cover_story():
    band = Table([[Paragraph(esc(shape("ڈیجیٹل کیریئر کورس")),
                             ParagraphStyle("c1", fontName="NSB", fontSize=30, leading=44, textColor=colors.white, alignment=TA_RIGHT))],
                  [Paragraph(wrap_ur("گھر سے کام کرنے والی خواتین کے لیے ابتدائی رہنما، تاکہ وہ پارٹ ٹائم ڈیجیٹل کیریئر بنا سکیں۔", FW - 40, "NS", 14),
                             ParagraphStyle("c2", fontName="NS", fontSize=14, leading=26, textColor=colors.white, alignment=TA_RIGHT))]],
                 colWidths=[FW])
    band.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), PLUM),
                              ("LEFTPADDING", (0, 0), (-1, -1), 22), ("RIGHTPADDING", (0, 0), (-1, -1), 22),
                              ("TOPPADDING", (0, 0), (-1, -1), 14), ("BOTTOMPADDING", (0, 0), (-1, -1), 16)]))
    s = [Spacer(1, 3.5 * cm), band, Spacer(1, 1 * cm)]
    s.append(Paragraph(wrap_ur("مفت میں سیکھیں۔ اپنے کام کا ثبوت بنائیں۔ پہلے کلائنٹ تلاش کریں۔ ادائیگی محفوظ طریقے سے لیں، اور اپنی رفتار سے آگے بڑھیں۔", FW, "NS", 11.5), st["intro"]))
    s.append(Spacer(1, 0.5 * cm))
    s.append(Image(os.path.join(FIGDIR, "fig01_roadmap.png"), width=FW, height=FW * 4.4 / 13))
    s.append(Paragraph(wrap_ur("اردو میں۔ کسی مہنگے سافٹ ویئر یا سامان کی ضرورت نہیں۔", FW, "NS", 9.5), st["cap"]))
    s.append(PageBreak())
    s.append(Paragraph(esc(shape("فہرست مضامین")), st["num"]))
    s.append(Paragraph(esc(shape("کورس میں کیا ہے")), st["chap"]))
    s.append(Spacer(1, 6))
    for i, (title, _, _) in enumerate(CHAPTERS):
        s.append(Paragraph(esc(shape(f"باب {i}")) + "&nbsp;&nbsp;&nbsp;" + wrap_ur(title, FW - 60, "NS", 12.5), st["toc"]))
    s.append(Spacer(1, 14))
    s.append(Paragraph(wrap_ur("ہر باب کے آخر میں چیک لسٹ ہے۔ اگلے باب سے پہلے عملی کام مکمل کریں۔", FW, "NS", 11.5), st["intro"]))
    s.append(PageBreak())
    return s

story = cover_story()
for i, (title, intro, blocks) in enumerate(CHAPTERS):
    if i > 0:
        story.append(PageBreak())
    story += chapter_story(i, title, intro, blocks)

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=M, rightMargin=M, topMargin=M, bottomMargin=2.1 * cm,
                        title="ڈیجیٹل کیریئر کورس برائے گھریلو خواتین (اردو)",
                        author="Course", subject="Urdu beginner digital skills and client-finding guide")
doc.build(story, onFirstPage=lambda c, d: None, onLaterPages=on_page)
print("wrote", OUT)

import sys, os
SCR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCR)
from content import CHAPTERS
from PIL import Image as PILImage
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image,
                                Table, TableStyle, KeepTogether)

FD = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DV", FD + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVB", FD + "DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DVI", FD + "DejaVuSans-Oblique.ttf"))
registerFontFamily("DV", normal="DV", bold="DVB", italic="DVI", boldItalic="DVB")

PLUM = colors.HexColor("#7B2D5C"); TEAL = colors.HexColor("#1F7A7A"); CORAL = colors.HexColor("#E07A5F")
SAND = colors.HexColor("#F6EFE6"); MINT = colors.HexColor("#D8EFEA"); DARK = colors.HexColor("#2B2B2B")
GREY = colors.HexColor("#6B6B6B")
OUT = "/mnt/storage/projects/LLMcourse/Digital_Career_Course_for_Women.pdf"

W, H = A4
M = 2 * cm
FW = W - 2 * M  # frame width

st = {
 "body": ParagraphStyle("body", fontName="DV", fontSize=10.2, leading=15, textColor=DARK, spaceAfter=7, alignment=TA_LEFT),
 "chap": ParagraphStyle("chap", fontName="DVB", fontSize=20, leading=26, textColor=PLUM, spaceAfter=4, keepWithNext=1),
 "num": ParagraphStyle("num", fontName="DVB", fontSize=9.5, leading=12, textColor=CORAL, spaceAfter=2),
 "intro": ParagraphStyle("intro", fontName="DVI", fontSize=10.8, leading=16, textColor=GREY, spaceAfter=12),
 "h": ParagraphStyle("h", fontName="DVB", fontSize=12.5, leading=17, textColor=TEAL, spaceBefore=10, spaceAfter=5, keepWithNext=1),
 "li": ParagraphStyle("li", fontName="DV", fontSize=10.2, leading=14.5, textColor=DARK, leftIndent=16, bulletIndent=4, spaceAfter=3),
 "cell": ParagraphStyle("cell", fontName="DV", fontSize=8.8, leading=11.5, textColor=DARK),
 "cellh": ParagraphStyle("cellh", fontName="DVB", fontSize=8.8, leading=11.5, textColor=colors.white),
 "cap": ParagraphStyle("cap", fontName="DVI", fontSize=8.6, leading=11, textColor=GREY, alignment=TA_CENTER, spaceBefore=3, spaceAfter=12),
 "box": ParagraphStyle("box", fontName="DV", fontSize=9.6, leading=14, textColor=DARK),
 "toc": ParagraphStyle("toc", fontName="DV", fontSize=11, leading=20, textColor=DARK),
}

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def table_block(rows, widths):
    total = sum(widths)
    cw = [FW * w / total for w in widths]
    data = []
    for i, r in enumerate(rows):
        style = st["cellh"] if i == 0 else st["cell"]
        data.append([Paragraph(esc(c), style) for c in r])
    t = Table(data, colWidths=cw, repeatRows=1)
    ts = [("BACKGROUND", (0, 0), (-1, 0), PLUM),
          ("VALIGN", (0, 0), (-1, -1), "TOP"),
          ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#CFC7BC")),
          ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
          ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5)]
    for i in range(1, len(rows)):
        if i % 2 == 0:
            ts.append(("BACKGROUND", (0, i), (-1, i), colors.HexColor("#FBF8F4")))
    t.setStyle(TableStyle(ts))
    return t

def box_block(text, bg, bar, label=None):
    lines = text.split("\n")
    parts = []
    if label:
        parts.append(f"<b>{label}</b>")
    for k, ln in enumerate(lines):
        if k == 0 and not label and len(lines) > 1:
            parts.append(f"<b>{esc(ln)}</b>")
        else:
            parts.append(esc(ln))
    p = Paragraph("<br/>".join(parts), st["box"])
    t = Table([[p]], colWidths=[FW])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), bg),
                           ("LINEBEFORE", (0, 0), (0, -1), 3, bar),
                           ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10),
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
    return KeepTogether([img, Paragraph(esc(caption), st["cap"])])

def chapter_story(num, title, intro, blocks):
    story = [Paragraph(f"CHAPTER {num}", st["num"]), Paragraph(esc(title), st["chap"]),
             Paragraph(esc(intro), st["intro"])]
    for b in blocks:
        kind = b[0]
        if kind == "h":
            story.append(Paragraph(esc(b[1]), st["h"]))
        elif kind == "p":
            story.append(Paragraph(esc(b[1]), st["body"]))
        elif kind == "ul":
            for item in b[1]:
                story.append(Paragraph(esc(item), st["li"], bulletText="•"))
            story.append(Spacer(1, 4))
        elif kind == "ol":
            for k, item in enumerate(b[1], 1):
                story.append(Paragraph(esc(item), st["li"], bulletText=f"{k}."))
            story.append(Spacer(1, 4))
        elif kind == "check":
            for item in b[1]:
                story.append(Paragraph(esc(item), st["li"], bulletText="☐"))
            story.append(Spacer(1, 4))
        elif kind == "table":
            story.append(table_block(b[1], b[2] if len(b) > 2 else [1] * len(b[1][0])))
            story.append(Spacer(1, 8))
        elif kind == "tip":
            story.append(box_block(b[1], MINT, TEAL, label="Tip: "))
            story.append(Spacer(1, 8))
        elif kind == "box":
            story.append(box_block(b[1], SAND, CORAL))
            story.append(Spacer(1, 8))
        elif kind == "img":
            story.append(image_block(b[1], b[2]))
    return story

def on_page(canv, doc):
    canv.saveState()
    if doc.page > 1:
        canv.setFont("DV", 8)
        canv.setFillColor(GREY)
        canv.drawString(M, 1.1 * cm, "Digital Career Course for Home-Based Women")
        canv.drawRightString(W - M, 1.1 * cm, f"Page {doc.page}")
        canv.setStrokeColor(MINT); canv.setLineWidth(1)
        canv.line(M, 1.5 * cm, W - M, 1.5 * cm)
    canv.restoreState()

def cover_story():
    band = Table([[Paragraph("<font color='white'><b>Digital Career Course</b></font>",
                             ParagraphStyle("c1", fontName="DVB", fontSize=28, leading=34, textColor=colors.white))],
                  [Paragraph("<font color='white'>A beginner's guide for women working from home<br/>to build a part-time digital career</font>",
                             ParagraphStyle("c2", fontName="DV", fontSize=13, leading=20, textColor=colors.white))]],
                 colWidths=[FW])
    band.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), PLUM),
                              ("LEFTPADDING", (0, 0), (-1, -1), 22), ("TOPPADDING", (0, 0), (-1, -1), 14),
                              ("BOTTOMPADDING", (0, 0), (-1, -1), 14)]))
    s = [Spacer(1, 3.5 * cm), band, Spacer(1, 1 * cm)]
    s.append(Paragraph("Learn a skill for free. Build proof of your work. Find your first clients. "
                       "Get paid safely, and grow at your own pace.", st["intro"]))
    s.append(Spacer(1, 0.5 * cm))
    s.append(Image(os.path.join(os.path.dirname(os.path.abspath(__file__)), "figs", "fig01_roadmap.png"),
                   width=FW, height=FW * 4.4 / 13))
    s.append(Paragraph("Written in English. No paid software or equipment required.", st["cap"]))
    s.append(PageBreak())
    s.append(Paragraph("CONTENTS", st["num"]))
    s.append(Paragraph("What is inside", st["chap"]))
    s.append(Spacer(1, 6))
    for i, (title, _, _) in enumerate(CHAPTERS):
        s.append(Paragraph(f"<b>Chapter {i}</b>&nbsp;&nbsp;&nbsp;{esc(title)}", st["toc"]))
    s.append(Spacer(1, 14))
    s.append(Paragraph("Each chapter has a checklist. Do the actions before moving on.", st["intro"]))
    s.append(PageBreak())
    return s

story = cover_story()
for i, (title, intro, blocks) in enumerate(CHAPTERS):
    story.append(PageBreak()) if i > 0 else None
    story += chapter_story(i, title, intro, blocks)

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=M, rightMargin=M, topMargin=M, bottomMargin=2.1 * cm,
                        title="Digital Career Course for Home-Based Women",
                        author="Course", subject="Beginner digital skills and client-finding guide")
doc.build(story, onFirstPage=lambda c, d: None, onLaterPages=on_page)
print("wrote", OUT)

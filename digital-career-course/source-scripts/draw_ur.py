import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, Polygon
import arabic_reshaper, math
from bidi.algorithm import get_display

SCR = "/tmp/claude-1000/-mnt-storage-projects-LLMcourse/4f51127c-01bf-45ff-90cf-1e058f8384f8/scratchpad/"
OUT = SCR + "figs_ur"
NASKH = "/usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf"
NASKHB = "/usr/share/fonts/truetype/noto/NotoNaskhArabic-Bold.ttf"
font_manager.fontManager.addfont(NASKH)
font_manager.fontManager.addfont(NASKHB)
plt.rcParams["font.family"] = ["Noto Naskh Arabic", "DejaVu Sans"]

def T(s):
    return get_display(arabic_reshaper.reshape(s))

PLUM = "#7B2D5C"; TEAL = "#1F7A7A"; CORAL = "#E07A5F"; SAND = "#F6EFE6"
DARK = "#2B2B2B"; GOLD = "#E9B44C"; MINT = "#D8EFEA"; ROSE = "#F7DDE7"; GREY = "#9A9A9A"
PALETTE = [PLUM, TEAL, CORAL, "#5B7DB1", GOLD, "#6A994E"]

def canvas(w, h):
    fig = plt.figure(figsize=(w, h), dpi=200)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, w * 10); ax.set_ylim(0, h * 10); ax.axis("off")
    fig.patch.set_facecolor("white")
    return fig, ax

def txt(ax, x, y, s, **kw):
    ax.text(x, y, T(s), **kw)

def box(ax, x, y, w, h, s, fc=SAND, ec=DARK, fs=11, tc=DARK, bold=False):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=1.2", fc=fc, ec=ec, lw=1.5))
    ax.text(x + w / 2, y + h / 2, T(s), ha="center", va="center", fontsize=fs, color=tc,
            fontweight="bold" if bold else "normal", linespacing=1.5)

def arrow(ax, x1, y1, x2, y2):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color=DARK, lw=1.8, mutation_scale=18))

def save(fig, name):
    fig.savefig(f"{OUT}/{name}.png", dpi=200, facecolor="white"); plt.close(fig)

# 1 Roadmap
fig, ax = canvas(13, 4.4)
txt(ax, 65, 40, "12 ہفتوں کا راستہ: پہلے ڈیجیٹل کلائنٹ تک", ha="center", fontsize=15, fontweight="bold", color=DARK)
steps = ["1  بنیادی باتیں\n    سیکھیں", "2  اپنی مہارت\n    چنیں", "3  مشق کریں اور\n    پورٹ فولیو بنائیں",
         "4  پہلا کلائنٹ\n    تلاش کریں", "5  کام پہنچائیں\n    اور ادائیگی لیں", "6  بڑھیں اور\n    دہرائیں"]
weeks = ["ہفتہ 1-2", "ہفتہ 2-3", "ہفتہ 3-8", "ہفتہ 8-10", "ہفتہ 10-12", "مہینہ 4 سے"]
for i, (s, wk) in enumerate(zip(steps, weeks)):
    x = 2 + i * 21.2
    box(ax, x, 15, 18, 16, s, fc=PALETTE[i], ec=PALETTE[i], tc="white", fs=10.5, bold=True)
    txt(ax, x + 9, 10, wk, ha="center", fontsize=9.5)
    if i < 5:
        arrow(ax, x + 18.3, 23, x + 21, 23)
save(fig, "fig01_roadmap")

# 2 Skill matrix
skills = [("ڈیٹا انٹری", 2.0, 2.5), ("ٹائپنگ اور ٹرانسکرپشن", 2.6, 3.4), ("سوشل میڈیا معاون", 3.4, 4.6),
          ("Canva ڈیزائن", 3.8, 5.6), ("ورچوئل اسسٹنٹ", 4.6, 5.0), ("پروڈکٹ لسٹنگ", 3.0, 4.0),
          ("کنٹینٹ رائٹنگ", 5.5, 6.6), ("ویڈیو ایڈیٹنگ (CapCut)", 5.2, 5.6), ("ترجمہ", 6.4, 6.2),
          ("آن لائن ٹیوشن", 4.4, 7.2), ("بک کیپنگ (شیٹس)", 6.6, 7.4), ("نو کوڈ ویب سائٹس", 7.6, 8.0)]
fig, ax = plt.subplots(figsize=(10, 7.2), dpi=200)
ax.axvspan(0, 5, ymin=0, ymax=0.5, color=MINT, alpha=0.55, lw=0)
ax.axhline(5, color=GREY, lw=1, ls="--"); ax.axvline(5, color=GREY, lw=1, ls="--")
ax.text(0.25, 0.4, T("یہاں سے شروع کریں: سیکھنا آسان،\nشروع میں کم معاوضہ"), fontsize=10, color=TEAL, fontweight="bold")
ax.text(5.25, 8.9, T("اس کی طرف بڑھیں: زیادہ مہارت،\nبعد میں زیادہ معاوضہ"), fontsize=10, color=PLUM, fontweight="bold")
for name, x, y in skills:
    ax.scatter(x, y, s=260, color=TEAL if y < 5 else PLUM, zorder=3, edgecolor="white", lw=1.5)
    ax.text(x + 0.18, y + 0.12, T(name), fontsize=10, color=DARK, zorder=4)
ax.set_xlim(0, 9); ax.set_ylim(0, 9.5)
ax.set_xlabel(T("پہلا ادا شدہ کام سیکھنے اور حاصل کرنے کا وقت  (کم  ←  زیادہ)"), fontsize=11)
ax.set_ylabel(T("وقت کے ساتھ کمائی کی صلاحیت  (کم  ←  زیادہ)"), fontsize=11)
ax.set_xticks([]); ax.set_yticks([])
for s in ["top", "right"]:
    ax.spines[s].set_visible(False)
ax.set_title(T("مہارتیں شروع کرنے کی آسانی اور آمدنی کے لحاظ سے (تقریبی)"), fontsize=13, fontweight="bold", color=DARK)
fig.tight_layout(); save(fig, "fig02_skill_matrix")

# 3 Toolkit
fig, ax = canvas(13, 7.6)
txt(ax, 65, 72, "آپ کا صفر خرچ ٹول کٹ: یہ سب شروع کرنے کے لیے مفت ہے", ha="center", fontsize=14, fontweight="bold")
cols = [("سیکھنا", PLUM, ["یوٹیوب (مفت سبق)", "Google Digital Garage", "Canva Design School", "freeCodeCamp", "Khan Academy", "Coursera آڈٹ موڈ"]),
        ("تخلیق", TEAL, ["Canva (مفت پلان)", "گوگل ڈاکس / شیٹس", "گوگل سلائیڈز", "CapCut (فون ویڈیو)", "گوگل ڈرائیو (15 GB)", "فون کیمرہ اور گیلری"]),
        ("رابطہ اور انتظام", CORAL, ["واٹس ایپ بزنس", "جی میل + گوگل کیلنڈر", "گوگل میٹ (مفت کالز)", "فون نوٹس / یاد دہانی", "مفت Trello یا Notion", "مفت ای میل پتہ"]),
        ("ادائیگی اور کام تلاش", "#5B7DB1", ["Upwork پر مفت پروفائل", "Fiverr پر مفت پروفائل", "LinkedIn پروفائل", "فیس بک اور واٹس ایپ گروپس", "مقامی آن لائن جاب گروپس", "Payoneer (مفت اکاؤنٹ)*"])]
for i, (title, color, items) in enumerate(cols):
    x = 1.5 + i * 30.3
    box(ax, x, 58, 28.5, 8, title, fc=color, ec=color, tc="white", fs=11.5, bold=True)
    ax.add_patch(Rectangle((x, 6), 28.5, 50, fc="#FBFAF8", ec=color, lw=1.4))
    for j, it in enumerate(items):
        txt(ax, x + 26.5, 50 - j * 7.3, "✓  " + it, fontsize=10, va="center", ha="right", color=DARK)
txt(ax, 65, 2.2, "*ادائیگی کی خدمات آپ کے ملک میں دستیاب ہیں یا نہیں، سائن اپ سے پہلے دیکھ لیں۔", ha="center", fontsize=9, color=GREY)
save(fig, "fig03_toolkit")

# 4 Weekly plan
fig, ax = canvas(12, 5.8)
txt(ax, 60, 54, "ایک حقیقت پسندانہ ہفتہ: روزانہ 2 سے 3 گھنٹے، چھوٹے وقفوں میں", ha="center", fontsize=13.5, fontweight="bold")
days = ["پیر", "منگل", "بدھ", "جمعرات", "جمعہ", "ہفتہ", "اتوار"]
rows = [("سیکھنا\n45-60 منٹ", PLUM, [0, 1, 2, 3, 4]),
        ("مشق\n60 منٹ", TEAL, [0, 2, 4, 5]),
        ("کلائنٹ تلاش\n30-45 منٹ", CORAL, [0, 1, 2, 3, 4]),
        ("پورٹ فولیو\nاور انتظامی کام", "#5B7DB1", [5]),
        ("آرام اور\nجائزہ", GREY, [6])]
x0, y0, cw, rh = 16, 6, 14.5, 8.2
for d, dn in enumerate(days):
    txt(ax, x0 + d * cw + cw / 2, y0 + len(rows) * rh + 2.5, dn, ha="center", fontsize=11, fontweight="bold")
for r, (label, color, on) in enumerate(rows):
    yy = y0 + (len(rows) - 1 - r) * rh
    txt(ax, x0 - 1, yy + rh / 2, label, ha="right", va="center", fontsize=9.5)
    for d in range(7):
        fc = color if d in on else "#F3F3F3"
        ax.add_patch(FancyBboxPatch((x0 + d * cw + 0.6, yy + 0.6), cw - 1.2, rh - 1.2,
                                    boxstyle="round,pad=0,rounding_size=0.8", fc=fc, ec="white", lw=1))
        if d in on:
            ax.text(x0 + d * cw + cw / 2, yy + rh / 2, "✓", ha="center", va="center", color="white", fontsize=13, fontweight="bold")
txt(ax, 60, 1.5, "خاندانی ذمہ داریاں پہلے۔ دن چھوٹ گیا؟ اگلے دن دوبارہ شروع کریں۔ مستقل مزاجی لمبے سیشن سے بہتر ہے۔", ha="center", fontsize=10)
save(fig, "fig04_weekly_plan")

# 5 Funnel
fig, ax = canvas(10, 6.6)
txt(ax, 50, 62, "آپ کا کلائنٹ تلاش کا فنل (تقریبی اعداد)", ha="center", fontsize=13.5, fontweight="bold")
stages = [("50 افراد یا کاروبار سے رابطہ", 80), ("20 جوابات", 64), ("8 مختصر بات چیت", 48),
          ("3 چھوٹے ادا شدہ ٹیسٹ", 32), ("1 سے 2 مستقل کلائنٹ", 20)]
for i, (label, w) in enumerate(stages):
    y = 48 - i * 9.2; x = 50 - w / 2
    ax.add_patch(Polygon([[x, y + 6.6], [x + w, y + 6.6], [x + w - 4, y], [x + 4, y]], closed=True,
                         fc=PALETTE[i], ec="white", lw=2))
    ax.text(50, y + 3.3, T(label), ha="center", va="center", color="white", fontsize=11, fontweight="bold")
txt(ax, 50, 3.2, "زیادہ تر محنت اوپر کی دو قطاروں میں ہے۔ بھیجتی رہیں؛ نمونے بڑھنے کے ساتھ تناسب بہتر ہوگا۔", ha="center", fontsize=9.5)
save(fig, "fig05_funnel")

# 6 Portfolio
fig, ax = canvas(6.5, 9)
ax.add_patch(Rectangle((8, 3), 49, 84, fc="white", ec=DARK, lw=2))
ax.add_patch(Rectangle((8, 78), 49, 9, fc=PLUM, ec=PLUM))
txt(ax, 32.5, 82.5, "فاطمہ احمد  |  سوشل میڈیا اور Canva ڈیزائنر", ha="center", va="center", color="white", fontsize=8.5, fontweight="bold")
ax.add_patch(Circle((16, 67), 4.2, fc=ROSE, ec=PLUM, lw=1.5))
txt(ax, 16, 67, "تصویر", ha="center", va="center", fontsize=7, color=PLUM)
txt(ax, 24, 69, "میرے بارے میں (3-4 سطریں)", fontsize=8, va="center")
txt(ax, 12, 62, "خدمات: انسٹاگرام پوسٹس  |  فلائرز  |  ریل کور", fontsize=7.5)
txt(ax, 12, 58.5, "48 گھنٹے میں تیار  |  اردو اور انگریزی", fontsize=7.5)
txt(ax, 12, 52.5, "میرا کام", fontsize=9, fontweight="bold", color=PLUM)
for k, cap in enumerate(["بیکری پوسٹ", "کلینک فلائر", "ٹیوٹر ریل"]):
    x = 11 + k * 14.6
    ax.add_patch(Rectangle((x, 37), 12.8, 13, fc=[MINT, ROSE, SAND][k], ec=DARK, lw=1))
    txt(ax, x + 6.4, 33.5, cap, ha="center", fontsize=6.8)
ax.add_patch(Rectangle((11, 18), 43, 10, fc="#FBFAF8", ec=TEAL, lw=1.2))
txt(ax, 47, 25, "\"تیز، دوستانہ اور وقت پر۔ ہماری پوسٹس کو زیادہ شیئر ملے۔\"  - خوش کلائنٹ", fontsize=7, va="center", ha="right")
ax.add_patch(FancyBboxPatch((17, 8), 31, 6.5, boxstyle="round,pad=0,rounding_size=2", fc=CORAL, ec=CORAL))
txt(ax, 32.5, 11.2, "آرڈر کے لیے واٹس ایپ کریں", ha="center", va="center", color="white", fontsize=8, fontweight="bold")
txt(ax, 32.5, -1, "موبائل پہلے: ایک اسکرین، بڑے بٹن، کوئی بے ترتیبی نہیں", ha="center", fontsize=8.5)
save(fig, "fig06_portfolio")

# 7 Invoice
fig, ax = canvas(6.5, 8.5)
ax.add_patch(Rectangle((6, 2), 53, 92, fc="white", ec=DARK, lw=2))
txt(ax, 53, 88, "انوائس", fontsize=15, fontweight="bold", color=PLUM, va="center", ha="right")
txt(ax, 53, 82, "آپ کا نام / کاروبار  |  فون  |  ای میل", fontsize=7.5, va="center", ha="right")
txt(ax, 12, 88, "نمبر 0012", fontsize=8, va="center")
txt(ax, 12, 84, "تاریخ: 07/11/2026", fontsize=8, va="center")
txt(ax, 53, 74, "بل بنام:", fontsize=8.5, fontweight="bold", va="center", ha="right")
txt(ax, 53, 70, "کلائنٹ کا نام / کاروبار / پتہ", fontsize=8, va="center", ha="right")
ax.add_patch(Rectangle((8, 56), 49, 9, fc=PLUM, ec=PLUM))
for xx, t in [(52, "تفصیل"), (32, "تعداد"), (14, "رقم")]:
    txt(ax, xx, 60.5, t, color="white", fontsize=8, fontweight="bold", va="center", ha="center")
items = ["انسٹاگرام پوسٹ ڈیزائن", "فلائر (A5، 2 ڈیزائن)", "ریل کور", "ترمیم (ایک دور)"]
qty = ["1", "2", "1", "1"]; amt = ["PKR 1,500", "PKR 2,400", "PKR 800", "مفت"]
for r in range(4):
    yy = 52 - r * 6.5
    ax.plot([8, 57], [yy - 2.5, yy - 2.5], color=GREY, lw=0.6)
    txt(ax, 52, yy, items[r], fontsize=7.5, va="center", ha="right")
    txt(ax, 32, yy, qty[r], fontsize=7.5, va="center", ha="center")
    txt(ax, 14, yy, amt[r], fontsize=7.5, va="center", ha="center")
txt(ax, 53, 24, "کل:  PKR 4,700", fontsize=9, fontweight="bold", ha="right", va="center")
ax.add_patch(Rectangle((8, 12), 49, 9, fc="#FBFAF8", ec=TEAL, lw=1.2))
txt(ax, 55, 17, "ادائیگی: بینک / موبائل وائلٹ / Payoneer کی تفصیل", fontsize=7.5, va="center", ha="right")
txt(ax, 55, 14, "ادائیگی 7 دن میں کریں۔ آپ کے کاروبار کا شکریہ!", fontsize=7.5, va="center", ha="right")
txt(ax, 32, -2, "ہر کام کے لیے ایک انوائس رکھیں۔ ترتیب سے نمبر دیں۔", ha="center", fontsize=8.5)
save(fig, "fig07_invoice")

# 8 Payment flow
fig, ax = canvas(13, 4.6)
txt(ax, 65, 41, "کلائنٹ کی ادائیگی آپ تک کیسے پہنچتی ہے", ha="center", fontsize=14, fontweight="bold")
flow = [("کلائنٹ انوائس\nادا کرتا ہے", PLUM), ("ادائیگی سروس یا پلیٹ فارم\nرقم رکھتا ہے\n(مثلاً Upwork، Payoneer)", TEAL),
        ("آپ کا آن لائن\nبیلنس", CORAL), ("اپنے بینک یا موبائل\nوائلٹ میں رقم\nنکالیں", "#5B7DB1")]
for i, (t, c) in enumerate(flow):
    x = 2 + i * 32.5
    box(ax, x, 10, 24, 20, t, fc=c, ec=c, tc="white", fs=10.5, bold=True)
    if i < 3:
        arrow(ax, x + 24.4, 20, x + 32, 20)
txt(ax, 65, 3.5, "کوئی سروس چننے سے پہلے فیس کا جدول دیکھیں۔ فیس اور رقم نکالنے کی حد بدلتی ہے، موجودہ شرائط چیک کریں۔", ha="center", fontsize=9.5)
save(fig, "fig08_payment_flow")

# 9 Learning loop
fig, ax = canvas(7.5, 7.5)
txt(ax, 37.5, 73, "سیکھنے کا چکر: ہر ہفتے دہرائیں", ha="center", fontsize=12.5, fontweight="bold")
labels = ["ایک نئی\nبات سیکھیں", "اسے نمونے پر\nمشق کریں", "ایک چھوٹا\nمکمل کام بنائیں", "رائے لیں\n(کلائنٹ یا گروپ)", "بہتر کریں اور\nنتیجہ دکھائیں"]
cx, cy, R = 37.5, 37, 23
pts = [(cx + R * math.cos(math.radians(90 - i * 72)), cy + R * math.sin(math.radians(90 - i * 72))) for i in range(5)]
for i in range(5):
    x1, y1 = pts[i]; x2, y2 = pts[(i + 1) % 5]
    ax.annotate("", xy=(x2 * 0.82 + cx * 0.18, y2 * 0.82 + cy * 0.18), xytext=(x1 * 0.82 + cx * 0.18, y1 * 0.82 + cy * 0.18),
                arrowprops=dict(arrowstyle="-|>", color=DARK, lw=1.8, mutation_scale=18))
for i, ((x, y), lab) in enumerate(zip(pts, labels)):
    ax.add_patch(Circle((x, y), 9.5, fc=PALETTE[i], ec="white", lw=2))
    ax.text(x, y, T(lab), ha="center", va="center", color="white", fontsize=8.6, fontweight="bold", linespacing=1.4)
txt(ax, cx, cy, "آپ\nبڑھتی ہیں", ha="center", va="center", fontsize=12, fontweight="bold", color=PLUM)
save(fig, "fig09_learning_loop")

# 10 Rule of thirds
fig, ax = canvas(6, 7.6)
ax.add_patch(FancyBboxPatch((12, 3), 36, 70, boxstyle="round,pad=0,rounding_size=4", fc="#222222", ec="#222222"))
ax.add_patch(Rectangle((14.5, 6), 31, 64, fc=SAND, ec="white"))
for f in [1 / 3, 2 / 3]:
    ax.plot([14.5 + 31 * f] * 2, [6, 70], ls="--", color=PLUM, lw=1)
    ax.plot([14.5, 45.5], [6 + 64 * f] * 2, ls="--", color=PLUM, lw=1)
ax.add_patch(Rectangle((14.5, 50.7), 31, 19.3, fc=ROSE, ec="none", alpha=0.9))
txt(ax, 30, 60, "سرخی\n(اوپر والا تہائی)", ha="center", va="center", fontsize=8.5, fontweight="bold", color=PLUM)
ax.add_patch(Circle((30, 33), 7.5, fc=TEAL, ec="none"))
txt(ax, 30, 33, "پروڈکٹ\nتصویر", ha="center", va="center", fontsize=7, color="white")
txt(ax, 30, 18, "ایک مختصر پیشکش کی لائن", ha="center", va="center", fontsize=7.5)
ax.add_patch(FancyBboxPatch((21, 11), 18, 4.5, boxstyle="round,pad=0,rounding_size=1.5", fc=CORAL, ec=CORAL))
txt(ax, 30, 13.2, "ہمیں پیغام دیں", ha="center", va="center", fontsize=7.5, color="white", fontweight="bold")
txt(ax, 30, 0.5, "اہم چیز وہاں رکھیں جہاں ڈیش لائنیں ملتی ہیں۔", ha="center", fontsize=8.5)
save(fig, "fig10_rule_of_thirds")
print("ok")

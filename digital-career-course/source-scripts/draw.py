import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, Polygon

OUT = "/tmp/claude-1000/-home-humayun--claude-spares-spare-V8sRaa/4f51127c-01bf-45ff-90cf-1e058f8384f8/scratchpad/figs"
PLUM = "#7B2D5C"; TEAL = "#1F7A7A"; CORAL = "#E07A5F"; SAND = "#F6EFE6"
DARK = "#2B2B2B"; GOLD = "#E9B44C"; MINT = "#D8EFEA"; ROSE = "#F7DDE7"; GREY = "#9A9A9A"
PALETTE = [PLUM, TEAL, CORAL, "#5B7DB1", GOLD, "#6A994E"]


def canvas(w, h):
    fig = plt.figure(figsize=(w, h), dpi=200)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, w * 10)
    ax.set_ylim(0, h * 10)
    ax.axis("off")
    fig.patch.set_facecolor("white")
    return fig, ax


def box(ax, x, y, w, h, text, fc=SAND, ec=DARK, fs=11, tc=DARK, bold=False, lw=1.5):
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=1.2",
                       fc=fc, ec=ec, lw=lw)
    ax.add_patch(p)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs,
            color=tc, fontweight="bold" if bold else "normal", linespacing=1.3)


def arrow(ax, x1, y1, x2, y2, color=DARK):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=1.8, mutation_scale=18))


def save(fig, name):
    fig.savefig(f"{OUT}/{name}.png", dpi=200, facecolor="white")
    plt.close(fig)


# 1. Roadmap
fig, ax = canvas(13, 4.4)
ax.text(65, 40, "Your 12-week route to a first digital client", ha="center", fontsize=15, fontweight="bold", color=DARK)
steps = ["1  Learn the\n    basics", "2  Choose your\n    skill", "3  Practise &\n    build portfolio",
         "4  Find your\n    first client", "5  Deliver &\n    get paid", "6  Grow &\n    repeat"]
weeks = ["Week 1-2", "Week 2-3", "Week 3-8", "Week 8-10", "Week 10-12", "Month 4 on"]
for i, (s, wk) in enumerate(zip(steps, weeks)):
    x = 2 + i * 21.2
    box(ax, x, 15, 18, 16, s, fc=PALETTE[i], ec=PALETTE[i], tc="white", fs=10.5, bold=True)
    ax.text(x + 9, 10, wk, ha="center", fontsize=9.5, color=DARK)
    if i < 5:
        arrow(ax, x + 18.3, 23, x + 21, 23)
save(fig, "fig01_roadmap")

# 2. Skill matrix
import numpy as np
skills = [("Data entry", 2.0, 2.5), ("Typing & transcription", 2.6, 3.4), ("Social media helper", 3.4, 4.6),
          ("Canva graphics", 3.8, 5.6), ("Virtual assistant", 4.6, 5.0), ("Product listings", 3.0, 4.0),
          ("Content writing", 5.5, 6.6), ("Video editing (CapCut)", 5.2, 5.6), ("Translation", 6.4, 6.2),
          ("Online tutoring", 4.4, 7.2), ("Bookkeeping (Sheets)", 6.6, 7.4), ("No-code websites", 7.6, 8.0)]
fig, ax = plt.subplots(figsize=(10, 7.2), dpi=200)
ax.axvspan(0, 5, ymin=0, ymax=0.5, color=MINT, alpha=0.55, lw=0)
ax.axhline(5, color=GREY, lw=1, ls="--"); ax.axvline(5, color=GREY, lw=1, ls="--")
ax.text(0.25, 0.4, "START HERE: quick to learn,\nsmaller pay at first", fontsize=10, color=TEAL, fontweight="bold")
ax.text(5.25, 8.9, "BUILD TOWARDS: more skill,\nhigher pay later", fontsize=10, color=PLUM, fontweight="bold")
for name, x, y in skills:
    ax.scatter(x, y, s=260, color=TEAL if y < 5 else PLUM, zorder=3, edgecolor="white", lw=1.5)
    ax.text(x + 0.18, y + 0.12, name, fontsize=10, color=DARK, zorder=4)
ax.set_xlim(0, 9); ax.set_ylim(0, 9.5)
ax.set_xlabel("Time to learn and get a first paid job  (short  ->  long)", fontsize=11)
ax.set_ylabel("Earning potential over time  (low  ->  high)", fontsize=11)
ax.set_xticks([]); ax.set_yticks([])
for s in ["top", "right"]:
    ax.spines[s].set_visible(False)
ax.set_title("Digital skills mapped by ease and income potential (indicative)", fontsize=13, fontweight="bold", color=DARK)
fig.tight_layout()
save(fig, "fig02_skill_matrix")

# 3. Free toolkit
fig, ax = canvas(13, 7.6)
ax.text(65, 72, "Your zero-cost toolkit: everything here is free to start", ha="center", fontsize=14, fontweight="bold")
cols = [("LEARN", PLUM, ["YouTube (free lessons)", "Google Digital Garage", "Canva Design School", "freeCodeCamp", "Khan Academy", "Coursera audit mode"]),
        ("CREATE", TEAL, ["Canva (free plan)", "Google Docs / Sheets", "Google Slides", "CapCut (phone video)", "Google Drive (15 GB)", "Phone camera & gallery"]),
        ("TALK & MANAGE", CORAL, ["WhatsApp Business", "Gmail + Google Calendar", "Google Meet (free calls)", "Phone notes / reminders", "Free Trello or Notion", "Free e-mail address"]),
        ("GET PAID & FIND WORK", "#5B7DB1", ["Free profile on Upwork", "Free profile on Fiverr", "LinkedIn profile", "Facebook & WhatsApp groups", "Local online-job groups", "Payoneer (free account)*"])]
for i, (title, color, items) in enumerate(cols):
    x = 1.5 + i * 30.3
    box(ax, x, 58, 28.5, 8, title, fc=color, ec=color, tc="white", fs=11.5, bold=True)
    ax.add_patch(Rectangle((x, 6), 28.5, 50, fc="#FBFAF8", ec=color, lw=1.4))
    for j, it in enumerate(items):
        ax.text(x + 2, 50 - j * 7.3, "✓  " + it, fontsize=10, va="center", color=DARK)
ax.text(65, 2.2, "*Check that Payoneer and other payment services are available in your country before signing up.", ha="center", fontsize=9, color=GREY)
save(fig, "fig03_toolkit")

# 4. Weekly plan
fig, ax = canvas(12, 5.8)
ax.text(60, 54, "A realistic week: 2 to 3 hours a day, split into short blocks", ha="center", fontsize=13.5, fontweight="bold")
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
rows = [("Learn\n45-60 min", PLUM, [0, 1, 2, 3, 4]),
        ("Practise\n60 min", TEAL, [0, 2, 4, 5]),
        ("Find clients\n30-45 min", CORAL, [0, 1, 2, 3, 4]),
        ("Portfolio &\nadmin", "#5B7DB1", [5]),
        ("Rest &\nreview", GREY, [6])]
x0, y0, cw, rh = 16, 6, 14.5, 8.2
for d, dn in enumerate(days):
    ax.text(x0 + d * cw + cw / 2, y0 + len(rows) * rh + 2.5, dn, ha="center", fontsize=11, fontweight="bold")
for r, (label, color, on) in enumerate(rows):
    yy = y0 + (len(rows) - 1 - r) * rh
    ax.text(x0 - 1, yy + rh / 2, label, ha="right", va="center", fontsize=9.5)
    for d in range(7):
        fc = color if d in on else "#F3F3F3"
        ax.add_patch(FancyBboxPatch((x0 + d * cw + 0.6, yy + 0.6), cw - 1.2, rh - 1.2,
                                    boxstyle="round,pad=0,rounding_size=0.8", fc=fc, ec="white", lw=1))
        if d in on:
            ax.text(x0 + d * cw + cw / 2, yy + rh / 2, "✓", ha="center", va="center", color="white", fontsize=13, fontweight="bold")
ax.text(60, 1.5, "Family duties come first. Missed a day? Just restart the next day. Consistency beats long sessions.",
        ha="center", fontsize=10, color=DARK)
save(fig, "fig04_weekly_plan")

# 5. Funnel
fig, ax = canvas(10, 6.6)
ax.text(50, 62, "Your client-hunting funnel (illustrative numbers)", ha="center", fontsize=13.5, fontweight="bold")
stages = [("50 people or businesses contacted", 80), ("20 replies", 64), ("8 short conversations", 48),
          ("3 small paid tests", 32), ("1-2 regular clients", 20)]
for i, (label, w) in enumerate(stages):
    y = 48 - i * 9.2
    x = 50 - w / 2
    ax.add_patch(Polygon([[x, y + 6.6], [x + w, y + 6.6], [x + w - 4, y], [x + 4, y]], closed=True,
                         fc=PALETTE[i], ec="white", lw=2))
    ax.text(50, y + 3.3, label, ha="center", va="center", color="white", fontsize=11, fontweight="bold")
ax.text(50, 3.2, "Most of the work is in the top two rows. Keep sending; ratios improve as your portfolio grows.",
        ha="center", fontsize=9.5, color=DARK)
save(fig, "fig05_funnel")

# 6. Portfolio wireframe
fig, ax = canvas(6.5, 9)
ax.add_patch(Rectangle((8, 3), 49, 84, fc="white", ec=DARK, lw=2))
ax.add_patch(Rectangle((8, 78), 49, 9, fc=PLUM, ec=PLUM))
ax.text(32.5, 82.5, "Fatima Ahmed  |  Social Media & Canva Designer", ha="center", va="center", color="white", fontsize=8.5, fontweight="bold")
ax.add_patch(Circle((16, 67), 4.2, fc=ROSE, ec=PLUM, lw=1.5))
ax.text(16, 67, "photo", ha="center", va="center", fontsize=7, color=PLUM)
ax.text(24, 69, "About me (3-4 lines)", fontsize=8, color=DARK, va="center")
for k in range(3):
    ax.add_patch(Rectangle((11, 47 - k * 0), 0.1, 0.1, fc="white", ec="white"))
ax.text(12, 62, "Services:  Instagram posts  |  Flyers  |  Reels cover", fontsize=7.5, color=DARK)
ax.text(12, 58.5, "Ready in 48 hours  |  Urdu & English", fontsize=7.5, color=DARK)
ax.text(12, 52.5, "My work", fontsize=9, fontweight="bold", color=PLUM)
for k, cap in enumerate(["Bakery post", "Clinic flyer", "Tutor reel"]):
    x = 11 + k * 14.6
    ax.add_patch(Rectangle((x, 37), 12.8, 13, fc=[MINT, ROSE, SAND][k], ec=DARK, lw=1))
    ax.text(x + 6.4, 33.5, cap, ha="center", fontsize=6.8, color=DARK)
ax.add_patch(Rectangle((11, 18), 43, 10, fc="#FBFAF8", ec=TEAL, lw=1.2))
ax.text(12.5, 25, "\"Fast, friendly and on time. Our posts\n   got more shares.\"  - Happy client", fontsize=7, va="center", color=DARK)
ax.add_patch(FancyBboxPatch((17, 8), 31, 6.5, boxstyle="round,pad=0,rounding_size=2", fc=CORAL, ec=CORAL))
ax.text(32.5, 11.2, "WhatsApp me to order", ha="center", va="center", color="white", fontsize=8, fontweight="bold")
ax.text(32.5, -1, "Mobile-first: one screen, big buttons, no clutter", ha="center", fontsize=8.5, color=DARK)
ax.set_title("", fontsize=1)
save(fig, "fig06_portfolio")

# 7. Invoice wireframe
fig, ax = canvas(6.5, 8.5)
ax.add_patch(Rectangle((6, 2), 53, 92, fc="white", ec=DARK, lw=2))
ax.text(12, 88, "INVOICE", fontsize=15, fontweight="bold", color=PLUM, va="center")
ax.text(12, 82, "Your name / business  |  phone  |  email", fontsize=7.5, color=DARK, va="center")
ax.text(50, 88, "No. 0012", fontsize=8, ha="right", va="center")
ax.text(50, 84, "Date: 07/11/2026", fontsize=8, ha="right", va="center")
ax.text(12, 74, "Bill to:", fontsize=8.5, fontweight="bold", va="center")
ax.text(12, 70, "Client name / business / address", fontsize=8, va="center", color=DARK)
ax.add_patch(Rectangle((8, 56), 49, 9, fc=PLUM, ec=PLUM))
for xx, t in [(10, "Description"), (38, "Qty"), (47, "Amount")]:
    ax.text(xx, 60.5, t, color="white", fontsize=8, fontweight="bold", va="center")
for r in range(4):
    yy = 52 - r * 6.5
    ax.plot([8, 57], [yy - 2.5, yy - 2.5], color=GREY, lw=0.6)
    ax.text(10, yy, ["Instagram post design", "Flyer (A5, 2 designs)", "Reel cover", "Revision (1 round)"][r], fontsize=7.5, va="center")
    ax.text(38.5, yy, ["1", "2", "1", "1"][r], fontsize=7.5, va="center")
    ax.text(47.5, yy, ["PKR 1,500", "PKR 2,400", "PKR 800", "Free"][r], fontsize=7.5, va="center")
ax.text(47, 24, "Total:  PKR 4,700", fontsize=9, fontweight="bold", ha="left", va="center")
ax.add_patch(Rectangle((8, 12), 49, 9, fc="#FBFAF8", ec=TEAL, lw=1.2))
ax.text(10, 17, "Payment: bank / mobile wallet / Payoneer details", fontsize=7.5, va="center")
ax.text(10, 14, "Payment due within 7 days.  Thank you for your business!", fontsize=7.5, va="center")
ax.text(32, -2, "Keep one invoice per job. Number them in order.", ha="center", fontsize=8.5, color=DARK)
save(fig, "fig07_invoice")

# 8. Payment flow
fig, ax = canvas(13, 4.6)
ax.text(65, 41, "How a client's payment reaches you", ha="center", fontsize=14, fontweight="bold")
flow = [("Client pays\nthe invoice", PLUM), ("Payment service or\nplatform holds it\n(e.g. Upwork, Payoneer)", TEAL),
        ("Your online\nbalance", CORAL), ("Withdraw to your\nbank or mobile\nwallet", "#5B7DB1")]
for i, (t, c) in enumerate(flow):
    x = 2 + i * 32.5
    box(ax, x, 10, 24, 20, t, fc=c, ec=c, tc="white", fs=10.5, bold=True)
    if i < 3:
        arrow(ax, x + 24.4, 20, x + 32, 20)
ax.text(65, 3.5, "Read the fee table before you choose a service. Fees and withdrawal limits change, so check the current terms.",
        ha="center", fontsize=9.5, color=DARK)
save(fig, "fig08_payment_flow")

# 9. Learning loop
fig, ax = canvas(7.5, 7.5)
ax.text(37.5, 73, "The learning loop: repeat it every week", ha="center", fontsize=12.5, fontweight="bold")
import math
labels = ["Learn one\nnew thing", "Practise it\non a sample", "Make a small\nfinished piece", "Get feedback\n(client or group)", "Improve and\nshow the result"]
cx, cy, R = 37.5, 37, 23
pts = []
for i in range(5):
    ang = math.radians(90 - i * 72)
    pts.append((cx + R * math.cos(ang), cy + R * math.sin(ang)))
for i in range(5):
    x1, y1 = pts[i]; x2, y2 = pts[(i + 1) % 5]
    ax.annotate("", xy=(x2 * 0.82 + cx * 0.18, y2 * 0.82 + cy * 0.18), xytext=(x1 * 0.82 + cx * 0.18, y1 * 0.82 + cy * 0.18),
                arrowprops=dict(arrowstyle="-|>", color=DARK, lw=1.8, mutation_scale=18))
for i, ((x, y), lab) in enumerate(zip(pts, labels)):
    ax.add_patch(Circle((x, y), 9.5, fc=PALETTE[i], ec="white", lw=2))
    ax.text(x, y, lab, ha="center", va="center", color="white", fontsize=8.6, fontweight="bold", linespacing=1.2)
ax.text(cx, cy, "YOU\nGROW", ha="center", va="center", fontsize=12, fontweight="bold", color=PLUM)
save(fig, "fig09_learning_loop")

# 10. Rule of thirds phone post
fig, ax = canvas(6, 7.6)
ax.add_patch(FancyBboxPatch((12, 3), 36, 70, boxstyle="round,pad=0,rounding_size=4", fc="#222222", ec="#222222"))
ax.add_patch(Rectangle((14.5, 6), 31, 64, fc="white", ec="white"))
ax.add_patch(Rectangle((14.5, 6), 31, 64, fc=SAND, ec="white"))
ax.add_patch(Rectangle((14.5, 70 - 21.3), 31, 0.01, fc="white"))
for f in [1 / 3, 2 / 3]:
    ax.plot([14.5 + 31 * f] * 2, [6, 70], ls="--", color=PLUM, lw=1)
    ax.plot([14.5, 45.5], [6 + 64 * f] * 2, ls="--", color=PLUM, lw=1)
ax.add_patch(Rectangle((14.5, 50.7), 31, 19.3, fc=ROSE, ec="none", alpha=0.9))
ax.text(30, 60, "HEADLINE\n(top third)", ha="center", va="center", fontsize=8.5, fontweight="bold", color=PLUM)
ax.add_patch(Circle((30, 33), 7.5, fc=TEAL, ec="none"))
ax.text(30, 33, "product\nphoto", ha="center", va="center", fontsize=7, color="white")
ax.text(30, 18, "Short offer line", ha="center", va="center", fontsize=7.5, color=DARK)
ax.add_patch(FancyBboxPatch((21, 11), 18, 4.5, boxstyle="round,pad=0,rounding_size=1.5", fc=CORAL, ec=CORAL))
ax.text(30, 13.2, "Message us", ha="center", va="center", fontsize=7.5, color="white", fontweight="bold")
ax.text(30, 0.5, "Put the main subject where the dashed lines cross.", ha="center", fontsize=8.5, color=DARK)
save(fig, "fig10_rule_of_thirds")

print("done")

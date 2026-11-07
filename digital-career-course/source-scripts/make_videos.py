import os, glob, subprocess, sys
from PIL import Image, ImageDraw, ImageFont
from bidi.algorithm import get_display
sys.path.insert(0, ".")
from content import CHAPTERS
INBOX = os.path.expanduser("~/ai-inbox/digital-career-course")
OUT = os.path.join(INBOX, "_video_drafts"); os.makedirs(OUT, exist_ok=True)
FIG = "figs/"
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FIGMAP = {0: "fig01_roadmap", 1: "fig09_learning_loop", 2: "fig03_toolkit", 3: "fig02_skill_matrix",
          4: "fig04_weekly_plan", 5: "fig10_rule_of_thirds", 6: "fig03_toolkit", 7: "fig05_funnel",
          8: "fig07_invoice", 9: "fig07_invoice", 10: "fig08_payment_flow", 11: "fig09_learning_loop", 12: "fig01_roadmap"}
VOICE = sorted(glob.glob(os.path.join(INBOX, "2026110*-voice-01")))
MUSIC = sorted(glob.glob(os.path.join(INBOX, "2026110*-music-01")))[0]
music_ogg = glob.glob(os.path.join(MUSIC, "*_music.ogg")) or glob.glob(os.path.join(MUSIC, "*.ogg"))
music_ogg = music_ogg[0]
for n, job in enumerate(VOICE):
    voice = glob.glob(os.path.join(job, "*_voice.ogg"))[0]
    title = CHAPTERS[n][0]
    cnum = n
    img = Image.new("RGB", (1920, 1080), "#F6EFE6")
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 1920, 230], fill="#7B2D5C")
    d.text((80, 60), f"Chapter {cnum}", font=ImageFont.truetype(FR, 44), fill="#F7DDE7")
    d.text((80, 120), title, font=ImageFont.truetype(FB, 60), fill="white")
    fig = Image.open(FIG + FIGMAP[cnum] + ".png").convert("RGB")
    maxh, maxw = 760, 1700
    scale = min(maxh / fig.height, maxw / fig.width)
    fig = fig.resize((int(fig.width * scale), int(fig.height * scale)))
    img.paste(fig, ((1920 - fig.width) // 2, 280 + (maxh - fig.height) // 2))
    d.text((80, 1020), "Digital Career Course  |  English  |  draft for review", font=ImageFont.truetype(FR, 30), fill="#6B6B6B")
    png = os.path.join("vd", f"ch{cnum:02d}.png"); img.save(png)
    out = os.path.join(OUT, f"ch{cnum:02d}_en_draft.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", png, "-i", voice, "-i", music_ogg,
                    "-filter_complex", "[2:a]volume=0.12,aloop=loop=-1:size=2000000000[m];[1:a][m]amix=inputs=2:duration=first:dropout_transition=0[a]",
                    "-map", "0:v", "-map", "[a]", "-c:v", "libx264", "-tune", "stillimage", "-pix_fmt", "yuv420p", "-r", "10",
                    "-c:a", "aac", "-b:a", "128k", "-shortest", out], check=True)
    print("made", out)

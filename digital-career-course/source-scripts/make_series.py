import os, re, glob, subprocess, sys
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, ".")
from content import CHAPTERS
S = os.path.dirname(os.path.abspath(__file__))
INBOX = os.path.expanduser("~/ai-inbox/digital-career-course")
OUT = os.path.join(INBOX, "_video_series"); os.makedirs(OUT, exist_ok=True)
LANG = sys.argv[1] if len(sys.argv) > 1 else "en"
MUSIC_JOB = os.path.join(INBOX, "20261107-0244-digital-career-course-music-01")  # seed 11, pending Homi's pick
music = (glob.glob(os.path.join(MUSIC_JOB, "*_music.ogg")) or glob.glob(os.path.join(MUSIC_JOB, "*.ogg")))[0]
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"; FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FIGMAP = {0: "fig01_roadmap", 1: "fig09_learning_loop", 2: "fig03_toolkit", 3: "fig02_skill_matrix",
          4: "fig04_weekly_plan", 5: "fig10_rule_of_thirds", 6: "fig03_toolkit", 7: "fig05_funnel",
          8: "fig07_invoice", 9: "fig07_invoice", 10: "fig08_payment_flow", 11: "fig09_learning_loop", 12: "fig01_roadmap"}
# chunk -> job folder, from the run log
chunks = {}
for line in open(os.path.join(S, "vo2", "jobmap.txt"), encoding="utf-8"):
    m = re.search(r"^(ch\d\d_[ab]\d)\b.*?(20261107-\d{4}-digital-career-course-voice-\d\d)", line)
    if m and "RESULT: PASS" in line:
        chunks[m.group(1)] = m.group(2)
chunks["ch00_a1"] = "20261107-1200-digital-career-course-voice-01"
for n in range(13):
    names = sorted([k for k in chunks if k.startswith(f"ch{n:02d}_")], key=lambda k: int(k.split("_")[1][1:]))
    assert names, n
    work = os.path.join(S, "vo2", f"ch{n:02d}_work"); os.makedirs(work, exist_ok=True)
    oggs = [glob.glob(os.path.join(INBOX, chunks[k], "*_voice.ogg"))[0] for k in names]
    # gap of 0.4 s between chunks, then one concatenated voice track
    cmd = ["ffmpeg", "-y", "-loglevel", "error"]
    for o in oggs: cmd += ["-i", o]
    cmd += ["-f", "lavfi", "-t", "0.4", "-i", "anullsrc=r=44100:cl=mono"]
    gap = len(oggs)
    fc = ""; labels = ""
    for i in range(len(oggs)):
        fc += f"[{i}:a]aresample=44100,aformat=channel_layouts=mono[v{i}];"
        labels += f"[v{i}][{gap}:a]"
    fc += f"{labels[:-len(f'[v{len(oggs)-1}][{gap}:a]')]}"  # placeholder, rebuilt below
    parts = []
    for i in range(len(oggs)):
        parts.append(f"[v{i}]")
        if i < len(oggs) - 1: parts.append(f"[{gap}:a]")
    fc = "".join(f"[{i}:a]aresample=44100,aformat=channel_layouts=mono[v{i}];" for i in range(len(oggs)))
    fc += "".join(parts) + f"concat=n={len(parts)}:v=0:a=1[voice]"
    voice = os.path.join(work, "voice.wav")
    subprocess.run(cmd + ["-filter_complex", fc, "-map", "[voice]", voice], check=True)
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", voice], capture_output=True, text=True).stdout)
    title = CHAPTERS[n][0]
    img = Image.new("RGB", (1920, 1080), "#F6EFE6"); d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 1920, 230], fill="#7B2D5C")
    d.text((80, 60), f"Chapter {n}", font=ImageFont.truetype(FR, 44), fill="#F7DDE7")
    d.text((80, 120), title, font=ImageFont.truetype(FB, 60), fill="white")
    fig = Image.open(os.path.join(S, "figs", FIGMAP[n] + ".png")).convert("RGB")
    scale = min(700 / fig.height, 1700 / fig.width); fig = fig.resize((int(fig.width * scale), int(fig.height * scale)))
    img.paste(fig, ((1920 - fig.width) // 2, 280 + (700 - fig.height) // 2))
    d.text((80, 1020), "Digital Career Course  |  English  |  series draft for review", font=ImageFont.truetype(FR, 30), fill="#6B6B6B")
    png = os.path.join(work, "card.png"); img.save(png)
    out = os.path.join(OUT, f"ch{n:02d}_{LANG}_series.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", png, "-i", voice, "-stream_loop", "-1", "-i", music,
                    "-filter_complex", "[2:a]volume=0.12[m];[1:a][m]amix=inputs=2:duration=first:dropout_transition=0[a]",
                    "-map", "0:v", "-map", "[a]", "-c:v", "libx264", "-tune", "stillimage", "-pix_fmt", "yuv420p", "-r", "10",
                    "-c:a", "aac", "-b:a", "128k", "-t", f"{dur + 0.5:.2f}", out], check=True)
    print(f"ch{n:02d} chunks={len(oggs)} voice={dur:.1f}s -> {out}", flush=True)

"""Build Urdu chapter videos from the VoxCPM2 clips (job digcareer-urdu-ch00-12 + fix job digcareer-urdu-fix-01).
Same style as the English chapter videos: title card, drawing, joined voice, low music bed."""
import os, re, glob, subprocess, sys
from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content_ur import CHAPTERS

SP = os.environ["SP"]
JOB = os.path.expanduser("~/ai-inbox/digital-career-course/_urdu_voxcpm2/digcareer-urdu-ch00-12")
FIX = os.path.expanduser("~/ai-inbox/digital-career-course/_urdu_voxcpm2/digcareer-urdu-fix-01")
OUT = os.path.expanduser("~/ai-inbox/digital-career-course/_video_series_urdu")
os.makedirs(OUT, exist_ok=True)
MUSIC_JOB = os.path.expanduser("~/ai-inbox/digital-career-course/20261107-0244-digital-career-course-music-01")
music = (glob.glob(os.path.join(MUSIC_JOB, "*_music.ogg")) or glob.glob(os.path.join(MUSIC_JOB, "*.ogg")))[0]
FB = "/usr/share/fonts/truetype/noto/NotoNaskhArabic-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FIGMAP = {0: "fig01_roadmap", 1: "fig09_learning_loop", 2: "fig03_toolkit", 3: "fig02_skill_matrix",
          4: "fig04_weekly_plan", 5: "fig10_rule_of_thirds", 6: "fig03_toolkit", 7: "fig05_funnel",
          8: "fig07_invoice", 9: "fig07_invoice", 10: "fig08_payment_flow", 11: "fig09_learning_loop", 12: "fig01_roadmap"}
FIXED = {"ch02_a1", "ch04_b3", "ch05_b3", "ch06_a1", "ch08_a1", "ch10_a1", "ch12_b2"}


def ur(text):
    return get_display(arabic_reshaper.reshape(text))


def fit_font(path, text, start, width):
    size = start
    while size > 24:
        f = ImageFont.truetype(path, size)
        if f.getlength(ur(text)) <= width:
            return f
        size -= 2
    return ImageFont.truetype(path, size)


def ordered_clips():
    """Return the clip wav paths in course order, with the seven split clips replaced by their two halves."""
    names = [l.split("\t")[0] for l in open(os.path.join(JOB, "lines.tsv"), encoding="utf-8") if l.strip()]
    out = []
    for n in names:
        if n in FIXED:
            out += [os.path.join(FIX, "wav", f"{n}_p1.wav"), os.path.join(FIX, "wav", f"{n}_p2.wav")]
        else:
            out.append(os.path.join(JOB, "wav", f"{n}.wav"))
    return out


clips = ordered_clips()
for n in range(13):
    chunk_names = [c for c in clips if re.search(rf"/ch{n:02d}_", c)]
    assert chunk_names, n
    work = os.path.join(SP, "urdu_work", f"ch{n:02d}"); os.makedirs(work, exist_ok=True)
    cmd = ["ffmpeg", "-y", "-loglevel", "error"]
    for c in chunk_names:
        cmd += ["-i", c]
    cmd += ["-f", "lavfi", "-t", "0.4", "-i", "anullsrc=r=48000:cl=mono"]
    gap = len(chunk_names)
    fc = "".join(f"[{i}:a]aresample=48000,aformat=channel_layouts=mono[v{i}];" for i in range(gap))
    parts = []
    for i in range(gap):
        parts.append(f"[v{i}]")
        if i < gap - 1:
            parts.append(f"[{gap}:a]")
    fc += "".join(parts) + f"concat=n={len(parts)}:v=0:a=1[voice]"
    voice = os.path.join(work, "voice.wav")
    subprocess.run(cmd + ["-filter_complex", fc, "-map", "[voice]", voice], check=True)
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", voice],
                               capture_output=True, text=True).stdout)

    title = CHAPTERS[n][0]
    img = Image.new("RGB", (1920, 1080), "#F6EFE6"); d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 1920, 230], fill="#7B2D5C")
    d.text((1840, 60), ur(f"باب {n}"), font=fit_font(FB, f"باب {n}", 44, 400), fill="#F7DDE7", anchor="ra")
    d.text((1840, 130), ur(title), font=fit_font(FB, title, 60, 1700), fill="white", anchor="ra")
    fig = Image.open(os.path.join(SP, "figs_ur", FIGMAP[n] + ".png")).convert("RGB")
    scale = min(700 / fig.height, 1700 / fig.width)
    fig = fig.resize((int(fig.width * scale), int(fig.height * scale)))
    img.paste(fig, ((1920 - fig.width) // 2, 280 + (700 - fig.height) // 2))
    d.text((80, 1020), "Digital Career Course  |  Urdu  |  series draft for review",
           font=ImageFont.truetype(FR, 30), fill="#6B6B6B")
    png = os.path.join(work, "card.png"); img.save(png)
    out = os.path.join(OUT, f"ch{n:02d}_ur_series.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", png, "-i", voice, "-stream_loop", "-1", "-i", music,
                    "-filter_complex", "[2:a]volume=0.12[m];[1:a][m]amix=inputs=2:duration=first:dropout_transition=0[a]",
                    "-map", "0:v", "-map", "[a]", "-c:v", "libx264", "-tune", "stillimage", "-pix_fmt", "yuv420p", "-r", "10",
                    "-c:a", "aac", "-b:a", "128k", "-t", f"{dur + 0.5:.2f}", out], check=True)
    print(f"ch{n:02d} clips={len(chunk_names)} voice={dur:.1f}s -> {out}", flush=True)

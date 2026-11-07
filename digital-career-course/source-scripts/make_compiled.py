"""Join the chapter videos into 4 episodes (5-10 min each) and one compiled video, per language.
Episode and course title cards are added in the same style. Output goes to LLMcourse/digital-skills/<language>/."""
import os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display

SP = os.environ["SP"]
INBOX = os.path.expanduser("~/ai-inbox/digital-career-course")
DEST = "/mnt/storage/projects/LLMcourse/digital-skills"
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
UFB = "/usr/share/fonts/truetype/noto/NotoNaskhArabic-Bold.ttf"
UFR = "/usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf"

EPISODES = [(0, 2), (3, 5), (6, 8), (9, 12)]
TEXT = {
    "en": {
        "dir": "english",
        "series": "_video_series", "suffix": "en_series",
        "course": ("Digital Career Course", "Complete video, all 13 chapters"),
        "ep": lambda i, a, b: (f"Episode {i} of 4", f"Chapters {a} to {b}"),
        "files": lambda i, a, b: f"episode-{i}-chapters-{a}-to-{b}.mp4",
        "compiled": "digital-career-course-complete-english.mp4",
        "rtl": False,
    },
    "ur": {
        "dir": "urdu",
        "series": "_video_series_urdu", "suffix": "ur_series",
        "course": ("ڈیجیٹل کیریئر کورس", "مکمل ویڈیو، تمام 13 ابواب"),
        "ep": lambda i, a, b: (f"قسط {i} از 4", f"ابواب {a} تا {b}"),
        "files": lambda i, a, b: f"episode-{i}-chapters-{a}-to-{b}.mp4",
        "compiled": "digital-career-course-complete-urdu.mp4",
        "rtl": True,
    },
}


def shaped(text):
    return get_display(arabic_reshaper.reshape(text))


def card(path, line1, line2, rtl):
    img = Image.new("RGB", (1920, 1080), "#7B2D5C")
    d = ImageDraw.Draw(img)
    f1 = ImageFont.truetype(UFB if rtl else FB, 110)
    f2 = ImageFont.truetype(UFR if rtl else FR, 60)
    t1 = shaped(line1) if rtl else line1
    t2 = shaped(line2) if rtl else line2
    anchor = "ra" if rtl else "la"
    x = 1840 if rtl else 120
    d.text((x, 420), t1, font=f1, fill="white", anchor=anchor)
    d.text((x, 580), t2, font=f2, fill="#F7DDE7", anchor=anchor)
    img.save(path)


def card_clip(out, png):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-t", "4", "-i", png,
                    "-f", "lavfi", "-t", "4", "-i", "anullsrc=r=48000:cl=stereo",
                    "-c:v", "libx264", "-tune", "stillimage", "-pix_fmt", "yuv420p", "-r", "10",
                    "-c:a", "aac", "-b:a", "128k", "-shortest", out], check=True)


def concat(files, out):
    lst = out + ".txt"
    with open(lst, "w", encoding="utf-8") as f:
        for p in files:
            f.write(f"file '{p}'\n")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", out], check=True)
    os.remove(lst)


def dur(path):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
                                capture_output=True, text=True).stdout)


for lang, cfg in TEXT.items():
    if len(sys.argv) > 1 and lang not in sys.argv[1:]:
        continue
    work = os.path.join(SP, "compile", lang); os.makedirs(work, exist_ok=True)
    dest = os.path.join(DEST, cfg["dir"]); os.makedirs(dest, exist_ok=True)
    chapter = lambda n: os.path.join(INBOX, cfg["series"], f"ch{n:02d}_{cfg['suffix']}.mp4")
    # course title card for the compiled video
    cpng = os.path.join(work, "course.png"); card(cpng, *cfg["course"], cfg["rtl"])
    ccard = os.path.join(work, "course.mp4"); card_clip(ccard, cpng)
    compiled_parts = [ccard]
    for i, (a, b) in enumerate(EPISODES, 1):
        epng = os.path.join(work, f"ep{i}.png"); card(epng, *cfg["ep"](i, a, b), cfg["rtl"])
        ecard = os.path.join(work, f"ep{i}.mp4"); card_clip(ecard, epng)
        chapters = [chapter(n) for n in range(a, b + 1)]
        for c in chapters:
            assert os.path.exists(c), c
        out = os.path.join(dest, cfg["files"](i, a, b))
        concat([ecard] + chapters, out)
        print(f"{lang} episode {i}: {dur(out) / 60:.2f} min -> {out}", flush=True)
        compiled_parts += chapters
    out = os.path.join(dest, cfg["compiled"])
    concat(compiled_parts, out)
    print(f"{lang} compiled: {dur(out) / 60:.2f} min -> {out}", flush=True)

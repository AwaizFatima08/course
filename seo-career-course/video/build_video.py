#!/usr/bin/env python3
"""Build one chapter video per course chapter.

Scenes are rendered as 1920x1080 HTML slides (course diagrams reused from the
English HTML), screenshotted with headless Chrome, then joined with ffmpeg.
The chapter narration (WAV) is split across scenes in proportion to each
scene's word count, so every scene stays on screen while its part is spoken.

Usage: build_video.py <chapter-number> <narration.wav>
Output: video/out/chNN.mp4
"""
import html
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
COURSE = os.path.dirname(HERE)
OUT = os.path.join(HERE, "out")
WORK = os.path.join(HERE, "work")
FPS = 25

# Which English figure (index into the 12 SVGs of the course) belongs to a chapter.
FIGURE_FOR_CHAPTER = {1: 0, 2: 1, 3: 3, 5: 4, 6: 5, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11}


def course_svgs():
    src = open(os.path.join(COURSE, "english", "SEO_Career_Course.html"), encoding="utf-8").read()
    return re.findall(r"<svg\b.*?</svg>", src, flags=re.S)


def parse_chapters():
    md = open(os.path.join(HERE, "course_video_script.md"), encoding="utf-8").read()
    chapters = {}
    parts = re.split(r"^## Chapter (\d+):", md, flags=re.M)
    for i in range(1, len(parts), 2):
        num = int(parts[i])
        body = parts[i + 1].split("\n## ")[0]
        scenes = []
        for block in re.split(r"^\*\*Scene \d+:", body, flags=re.M)[1:]:
            title = block.split("**", 1)[0].strip().rstrip("(").strip()
            en = re.findall(r'^- EN: "?(.*?)"?$', block, flags=re.M)
            text = " ".join(e.strip().rstrip('"') for e in en)
            scenes.append({"title": title, "text": re.sub(r"\s+", " ", text).strip()})
        chapters[num] = scenes
    return chapters


def slide_html(kind, chapter_num, scene, svg):
    title = html.escape(re.sub(r"\(.*?\)", "", scene["title"]).strip())
    text = html.escape(scene["text"])
    if kind == "title":
        body = f'<div class="big">Chapter {chapter_num}</div><div class="huge">{html.escape(scene["text"].split(". ")[0].replace("Chapter %d." % chapter_num, "").strip())}</div>'
        caption = text
    elif svg:
        body = f'<div class="fig">{svg}</div>'
        caption = text
    else:
        body = f'<div class="card">{text}</div>'
        caption = ""
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
    html,body{{margin:0;width:1920px;height:1080px;overflow:hidden;background:#f7f9fc;
      font-family:"Liberation Sans",Arial,sans-serif;color:#1d2433}}
    .top{{position:absolute;left:80px;top:60px;right:80px}}
    .chap{{font-size:28px;color:#1f6feb;font-weight:bold;letter-spacing:2px;text-transform:uppercase}}
    .big{{font-size:44px;color:#1f6feb;font-weight:bold;margin-top:200px;text-align:center}}
    .huge{{font-size:96px;color:#0b3d91;font-weight:bold;text-align:center;margin:20px 120px;line-height:1.15}}
    .fig{{position:absolute;left:0;right:0;top:150px;text-align:center}}
    .fig svg{{width:1500px;height:auto}}
    .card{{position:absolute;left:160px;right:160px;top:260px;font-size:58px;line-height:1.4}}
    .cap{{position:absolute;left:0;right:0;bottom:0;height:200px;background:rgba(11,61,145,.92);color:#fff;
      font-size:34px;line-height:1.35;padding:28px 80px;box-sizing:border-box}}
    .foot{{position:absolute;left:80px;bottom:215px;font-size:22px;color:#5b6475}}
    </style></head><body>
    <div class="top"><div class="chap">SEO Career Course &middot; Chapter {chapter_num} &middot; {title}</div></div>
    {body}
    {f'<div class="cap">{caption}</div>' if caption else ''}
    </body></html>"""


def render_png(html_text, png_path):
    html_path = png_path.replace(".png", ".html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_text)
    subprocess.run(
        ["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu",
         "--hide-scrollbars", "--window-size=1920,1080",
         f"--screenshot={png_path}", "file://" + html_path],
        check=True, capture_output=True, timeout=120)


def duration(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "csv=p=0", path], capture_output=True, text=True, check=True)
    return float(out.stdout.strip())


def build(chapter_num, wav):
    chapters = parse_chapters()
    scenes = chapters[chapter_num]
    svgs = course_svgs()
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(WORK, exist_ok=True)
    total = duration(wav)
    words = [max(1, len(s["text"].split())) for s in scenes]
    share = [total * w / sum(words) for w in words]

    clips = []
    for idx, scene in enumerate(scenes, start=1):
        kind = "title" if idx == 1 else "content"
        svg = None
        if idx == 2 and chapter_num in FIGURE_FOR_CHAPTER:
            svg = svgs[FIGURE_FOR_CHAPTER[chapter_num]]
        png = os.path.join(WORK, f"ch{chapter_num:02d}_s{idx}.png")
        render_png(slide_html(kind, chapter_num, scene, svg), png)
        clip = os.path.join(WORK, f"ch{chapter_num:02d}_s{idx}.mp4")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", png,
                        "-t", f"{share[idx - 1]:.2f}", "-r", str(FPS), "-c:v", "libx264",
                        "-pix_fmt", "yuv420p", clip], check=True)
        clips.append(clip)

    listfile = os.path.join(WORK, f"ch{chapter_num:02d}_list.txt")
    with open(listfile, "w") as f:
        for c in clips:
            f.write(f"file '{c}'\n")
    silent = os.path.join(WORK, f"ch{chapter_num:02d}_video.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
                    "-i", listfile, "-c", "copy", silent], check=True)
    final = os.path.join(OUT, f"ch{chapter_num:02d}.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", silent, "-i", wav,
                    "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac",
                    "-b:a", "192k", "-shortest", final], check=True)
    print("wrote", final, f"{total:.1f}s")


if __name__ == "__main__":
    build(int(sys.argv[1]), sys.argv[2])

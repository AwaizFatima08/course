import re, json, os
SRC = "/mnt/storage/projects/LLMcourse/Course_Video_Scripts.md"
OUT = "vo"
text = open(SRC, encoding="utf-8").read()
en = text.split("## 3. English scripts")[1].split("## 4. Urdu scripts")[0]
parts = re.split(r"\n### Chapter (\d+):", en)
chapters = {}
for i in range(1, len(parts), 2):
    num = int(parts[i]); body = parts[i + 1]
    lines = [l[len("Narration: "):].strip() for l in body.splitlines() if l.startswith("Narration: ")]
    chapters[num] = " ".join(lines)
GLOSS = "Canva, WhatsApp Business, Gmail, Google Drive, Upwork, Fiverr, LinkedIn, CapCut, Payoneer, OTP, PIN, freelance"
for n, s in sorted(chapters.items()):
    inp = {"script": s, "glossary": GLOSS, "voice": "af_bella"}
    with open(f"{OUT}/ch{n:02d}_en.json", "w", encoding="utf-8") as f:
        json.dump(inp, f, ensure_ascii=False, indent=1)
    print(n, len(s.split()), "words")

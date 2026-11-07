# Urdu narration series plan (VoxCPM2)

Status (updated 7 Nov 2026): the route is Homi's `voice-voxcpm2` recipe (`~/shared/voxcpm2/RECIPE.md` on homidev),
approved for jobs submitted from hominas. It runs through `submit.sh` and jobq on homidev. The receiver engine
change and the draft `voice-hi-urdu-voxcpm2` recipe are no longer needed.

## Series split (5–10 min per video)
The course video script runs 18:40 in total, and each chapter is about 1 minute on its timeline. Five episodes would
be under 5 minutes each, so three episodes follow the script's own timeline:

| Episode | Script sections | Timeline |
|---|---|---|
| 1 | Intro to chapter 5 | 0:00–6:30 |
| 2 | Chapters 6–10 | 6:30–12:20 |
| 3 | Chapters 11–15 + outro | 12:20–18:40 |

The Urdu narration is shorter than the English timing, so an episode may come in under 6 minutes. Check the
rendered length and extend the Urdu text if needed.

## Checks before publishing
1. Homi listens to every clip. No automatic Urdu check exists.
2. Latin terms (VRAM, RAM, NVIDIA, Ollama, nvidia-smi, BIOS) may be read oddly. Fix by respelling in Urdu script or Roman Urdu.
3. The script's English says "four tiers" in chapter 3 but lists three. Decide which is correct before the English and Urdu versions are recorded.

## Job record
- Episode 1 (`urdu-ep1-intro-ch5`): 27 clips, submitted 7 Nov 2026 from hominas via `submit.sh`.

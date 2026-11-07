# Urdu-vocabulary Hindi narration: series plan (draft)

Status: NOT approved. The homidev recipe `voice-hi-urdu-voxcpm2` is a draft (`approved_by: null`),
VoxCPM2 is not in the model register, and recipes on homidev are still 9. No jobs submitted.

## Series split (5–10 min per video)
Spoken pace ~130 words/min, so 5–10 min is roughly 650–1300 English words, or about 4,000–8,000 Devanagari characters.

| Episode | Chapters | Target length |
|---|---|---|
| 1 | Intro + chapters 1–3 | 6–8 min |
| 2 | Chapters 4–6 | 6–8 min |
| 3 | Chapters 7–9 | 6–9 min |
| 4 | Chapters 10–12 | 6–9 min |
| 5 | Chapters 13–15 + outro | 6–8 min |

## Blockers before any job
1. Homi's approval recorded in `recipe.json` (`approved_by`, `approved_date`) and the recipe accepted by the receiver.
2. `max_length` is 1500 characters, which is about 2 minutes. Each episode needs about 4,000–8,000 characters, so either raise the limit or send each episode as 4–6 jobs of about 1,400 characters and join them.
3. VoxCPM2 model path on homidev is still "to be confirmed"; the licence (listed as Apache-2.0) is not yet checked against the model card.
4. No automatic Hindi/Urdu check exists. Every output needs Homi's listening review.

## Pronunciation rules to apply in the script
- Core words in Urdu form (for example: "آپ" style vocabulary, written in Devanagari with Urdu words).
- Urdu sounds in Devanagari with nukta: ख़ (kh), ग़ (gh), ज़ (z).

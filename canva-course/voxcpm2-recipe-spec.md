# VoxCPM2 voice recipe: draft spec for Homi's review

Status: **draft. Not installed on homidev.** Homi reviews, decides and installs it in the receiver. Claude does not change homidev.

## Purpose
A voice-over recipe for Devanagari Hindi scripts that use Urdu vocabulary, with Urdu sounds for kh, gh and z (ख़, ग़, ज़). Used for the Canva course Urdu video series. Urdu itself is not an officially supported language of VoxCPM2 (Hindi is), so the script must be Hindi-mode text.

## Model
- VoxCPM2 (OpenBMB), installed on homidev. Hugging Face: https://huggingface.co/openbmb/VoxCPM2
- Licence: reported as Apache-2.0 in search snippets. **Verify the licence file before commercial_ok = yes.**
- Model version and checkpoint path on homidev: to be filled in by Homi.

## Inputs (JSON object, same shape as voice-en-standard)
| Field | Required | Rule |
|---|---|---|
| `script` | yes | Devanagari Hindi text, Urdu vocabulary for core words, nukta letters for ख़ ग़ ज़ ق फ़. Never empty. |
| `glossary` | yes | Words to check after transcription: app, brand and course words, plus the Urdu-vocabulary words in the script. Never empty. |
| `voice` | no | Reference voice or voice-design prompt. Default to be set by Homi after the listening test. |
| `cfg` | no | Generation guidance value. Default to be set by Homi. |
| `seed` | no | For repeatable takes. |

## Output
- WAV master (not to be committed to any repo) and mono/stereo OGG for apps, as in voice-en-standard.
- Level: −16 LUFS with a limiter; true peak ≤ −1.5 dBFS.
- Stage 1 checks: length, loudness, true peak, leading/trailing silence, Whisper match to the script (match ≥ 0.9), licence gate.

## Listening test (before any production run)
One paragraph, three takes, same seed and voice:
- A: plain Hindi (no nukta letters)
- B: Hindi with nukta letters (ख़ ग़ ज़)
- C: nukta letters plus the Urdu vocabulary from the course glossary

Homi picks the take that sounds most Urdu. The chosen setting becomes the recipe default.

## Review
- Every voice-over goes to Homi for listening (homidev rule). Claude notes the Stage 1 facts only.
- Nothing is integrated into a project without Homi's chat approval.

## Open points for Homi
1. Recipe name to register (suggested: `voice-ur-voxcpm`).
2. Confirm the licence and set `commercial_ok`.
3. Which voice or reference clip to use as default.
4. Whether the receiver can run VoxCPM2 without unloading or blocking the GPU for other jobs. Free the GPU after each job.
5. Whether this recipe should stay separate from the English `voice-en-standard` recipe.

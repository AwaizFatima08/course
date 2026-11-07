# Digital career course: video build scripts

These scripts rebuild the chapter, episode and compiled videos from the voice clips.
The English voice comes from the homidev Kokoro job; the Urdu voice comes from VoxCPM2 (homidev, job `digcareer-urdu-ch00-12` plus fix job `digcareer-urdu-fix-01`).

Run order:
1. `draw.py` and `draw_ur.py`: make the chapter figures (English and Urdu).
2. `make_series.py`: English chapter videos.
3. `make_urdu.py`: Urdu chapter videos (uses `content_ur.py`).
4. `make_compiled.py [en|ur]`: four episodes and one compiled video per language, written to `digital-skills/<language>/`.
5. `watch_urdu.sh`: waits for the Urdu fix job on homidev, fetches it, then runs steps 3 and 4.

Requirements: Python venv with pillow, matplotlib, arabic-reshaper, python-bidi, reportlab; ffmpeg; the Noto Naskh Arabic and DejaVu fonts.

Set `SP` to a scratch folder before running. The scripts also contain hard-coded scratchpad paths in `content_ur.py`, `draw.py` and `draw_ur.py`. Change those when running in a new session.

Voice clips, music, and the final MP4 files are not stored in this repo.

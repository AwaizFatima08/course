# Canva Freelance Career: Urdu video series, plan v2 (8 Nov 2026)

Audience: a common person with basic computer use and no design or freelancing background. Each video is 5–10 minutes. The series covers the 14-chapter English course in detail, step by step, with on-screen examples.

## Review of plan v1 (what changed and why)

| Issue in v1 | Change in v2 |
|---|---|
| 5 videos of 5–10 minutes were too dense for beginners | 11 videos, one main topic each, so no single video carries 3 chapters |
| Chapter scripts were short (about 130 words) | Each video is 700–900 words of narration plus on-screen steps |
| Prices and platform fees were not dated | Prices and fees are not read out as fixed numbers. Each video says where to check them and when they were checked (8 Nov 2026). |
| Narration was assumed to be ready | Narration runs through `voice-voxcpm2` on homidev. Homi listens to every clip before use. |
| No safety or scam warnings | Each freelancing video has a scam and safety section |

## Source notes (checked 8 Nov 2026, third-party sources, verify before publishing)

- Canva pricing changed several times in 2025–26. Teams is listed as no longer available for new sign-ups in some sources; Business is the current team plan. Source: https://piktochart.com/blog/canva-pricing-2026-costs-raised/ and https://www.capterra.com/p/168956/Canva/pricing/ (conflicting figures across sources; check https://www.canva.com/pricing/).
- Upwork: a variable freelancer service fee (0–15%) per contract, reported as replacing the old tiers in May 2025. Source: https://golance.com/blogs/upwork-fees-explained-2026 (third party; confirm on Upwork's own fee page).
- Fiverr: seller commission reported as 20% of seller earnings. Source: third-party summaries only; confirm on Fiverr's Help Center.
- Etsy (US, digital downloads): listing fee plus a 6.5% transaction fee plus payment processing, reported in third-party guides. Source: https://listingview.io/blogs/how-to-sell-digital-products-on-etsy-in-2026 (confirm on Etsy's fee page).
- Creative Market and Envato: not checked yet; a separate check is needed before those videos mention commission.

## Video list

| No. | Title (Urdu-vocabulary Hindi) | Covers | Length |
|---|---|---|---|
| 1 | डिज़ाइन की दुनिया और आपका पहला क़दम | Intro, Ch 1 | 6–7 min |
| 2 | कैनवा से तआरुफ़ और अकाउंट बनाना | Ch 2–3 | 7–8 min |
| 3 | कैनवा एडिटर: स्क्रीन के हर हिस्से की पहचान | Ch 4 | 8–9 min |
| 4 | डिज़ाइन के बुनियादी उसूल: रंग, फ़ॉन्ट, जगह | Ch 5 | 8–9 min |
| 5 | पाँच प्रैक्टिस प्रोजेक्ट, क़दम-ब-क़दम | Ch 6 | 9–10 min |
| 6 | कैनवा के एडवांस फ़ीचर्स और AI टूल्स | Ch 7 | 8–9 min |
| 7 | पोर्टफ़ोलियो और ऑनलाइन शनाख़्त | Ch 8 | 7–8 min |
| 8 | रेट तय करना और ग्राहक ढूँढना | Ch 9 | 8–9 min |
| 9 | फ़्रीलांस मार्केटप्लेस: फ़ायदे, फ़ीस और ख़तरे | Ch 10 | 8–9 min |
| 10 | टेम्पलेट और डिजिटल प्रोडक्ट्स बेचना | Ch 11 | 8–9 min |
| 11 | दूसरे प्लेटफ़ॉर्म, कारोबार और 90 दिन का रोडमैप | Ch 12–14 | 9–10 min |

## Per-video structure (each video)
1. Hook (15 seconds): what the viewer will be able to do by the end.
2. Concept (1–2 minutes): the idea, in plain words, with one example.
3. Step by step (3–5 minutes): exact clicks or steps, each shown on screen.
4. Mistakes to avoid (1 minute).
5. Practice task (1 minute): one thing to do before the next video.
6. Summary and next video (30 seconds).

## Production rules
- Narration: Hindi-mode text with Urdu vocabulary (glossary in `Canva_Course_Urdu_Voice_Series.md`) and nukta letters for ख़ ग़ ज़. Final choice after Homi's listening test.
- Each paragraph of the script becomes one narration clip (under about 300 characters, for stable generation).
- Every clip is checked by Homi before the video is built.
- Visuals: screenshots or screen recordings where possible; course figures (SVG/PDF) otherwise. Price and feature screens are captured on the day of recording and dated on screen.
- Safety: no passwords or payment details shown on screen; no real client names.

## Open points for Homi
1. Choose the Urdu-vocabulary spelling style after the listening test (plain Hindi, nukta letters, or nukta letters plus Urdu vocabulary).
2. Voice: the default `m1` (male, calm) or a description for a female narrator. Homi decides.
3. Confirm the 11-video split above.

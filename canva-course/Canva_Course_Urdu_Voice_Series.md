# Canva Freelance Course: Urdu Voice Video Series (draft, not yet voiced)

Status: **planning draft. Nothing has been generated on homidev yet.** Homi must decide the open points at the end.

## 1. Voice model: what the checks show

- **Model:** VoxCPM2 (OpenBMB), https://huggingface.co/openbmb/VoxCPM2
- **Licence:** the search snippets say Apache-2.0 (commercial use allowed). I have not opened the model card or licence file myself; confirm before any release.
- **Languages:** Hindi is in the official list. **Urdu is not** (no `ur` code found). Project docs say unsupported languages may need fine-tuning.
- **Not on homidev.** VoxCPM2 is not installed there and no recipe for it exists. The approved recipes cover Kokoro voice-over, image, sound and music only. Adding the model and a recipe is a change on homidev, which Homi reserves for his own planned work.

## 2. Method (Hindi mode, Urdu vocabulary)

- Write the narration in **Devanagari Hindi** (the mode VoxCPM2 supports), using **Urdu vocabulary** for the core words listed in section 4.
- Mark the Urdu sounds with the nukta letters:
  - خ (kh) → **ख़** (e.g. ख़िदमत, ख़ास)
  - غ (gh) → **ग़** (e.g. ग़लती, आग़ाज़)
  - ز / ژ (z) → **ज़** (e.g. ज़बान, रोज़ाना)
  - ق → क़, ف → फ़ (for example तरक़्क़ी, फ़ायदा)
- **Risk:** VoxCPM2 may pronounce ख़ / ग़ / ज़ as plain ख / ग / ज. A short listening test (one paragraph, three versions) must confirm this before the full series is generated.

## 3. Series structure (five videos, 5–10 minutes each)

Target: about 650–700 words of narration per 5 minutes at a calm pace, so 900–1,300 words per video. Chapter scripts are short, so each video combines related chapters and adds worked examples.

| Video | Title (Urdu-vocab Hindi) | Chapters covered | Target length |
|---|---|---|---|
| 1 | कैनवा से शुरुआत: डिज़ाइन की दुनिया और अकाउंट | Intro, Ch 1–3 | 6–7 min |
| 2 | कैनवा एडिटर और डिज़ाइन के बुनियादी उसूल | Ch 4–5 | 8–9 min |
| 3 | पहले प्रोजेक्ट और पोर्टफ़ोलियो | Ch 6–8 | 9–10 min |
| 4 | रेट, ग्राहक और प्लेटफ़ॉर्म | Ch 9–11 | 8–9 min |
| 5 | दूसरे प्लेटफ़ॉर्म, कारोबार और 90 दिन का रोडमैप | Ch 12–14 | 8–9 min |

Video 1 is the pilot below. Videos 2–5 are not written yet; they wait for Homi's decision on the listening test.

## 4. Glossary: core Hindi word → Urdu alternative (draft for native check)

| Hindi (Sanskrit-origin) | Urdu alternative (Devanagari spelling) | Meaning |
|---|---|---|
| विचार | ख़याल | idea |
| शुरुआत | आग़ाज़ | start |
| ग़लती (Hindi: गलती) | ग़लती | mistake |
| अवसर | मौक़ा | opportunity |
| लाभ | फ़ायदा | benefit |
| हानि | नुक़सान | loss |
| ग्राहक | गाहक | customer (ग्राहक in Hindi) |
| बिक्री | फ़रोख़्त | sale |
| कार्यालय | दफ़्तर | office |
| अनुमति | इजाज़त | permission |
| भाषा | ज़बान | language |
| प्रतिदिन / हर दिन | रोज़ाना | daily |
| उपयोग | इस्तेमाल | use |
| निःशुल्क | मुफ़्त | free |
| विशेष | ख़ास | special |
| बहुत अच्छा | ख़ूब | very good |
| कौशल | हुनर | skill |
| व्यवसाय / व्यापार | कारोबार | business |
| राशि | रक़म | amount |
| प्रगति / उन्नति | तरक़्क़ी | progress |
| नौकरी | मुलाज़मत | job |
| सेवा | ख़िदमत | service |
| पहचान | शनाख़्त | identity |
| जानकारी | मालूमात | information |
| पढ़ाई / शिक्षा | तालीम | education |
| सफलता | कामयाबी | success |
| ध्यान | तवज्जोह | attention |
| परिचय | तआरुफ़ | introduction |

Keep the same in Hindi and Urdu: है/हैं, और, आप, काम, करना, सीखना, बहुत, आसान, ज़रूरी, ज़रूरत, कोशिश, ज़िंदगी, मेहनत, कैनवा, ब्रांड.

## 5. Pilot: Video 1 narration (draft)

Target about 6–7 minutes. Read aloud at a calm pace; the English course text is the reference.

---

**[दृश्य: चैनल का परिचय, शीर्षक कार्ड]**

नमस्ते दोस्तो! यह सीरीज़ उन सब के लिए है जिन्हें कंप्यूटर या मोबाइल का बुनियादी इल्म है और जो घर बैठे डिजिटल फ़्रीलांसिंग शुरू करना चाहते हैं। इस सीरीज़ में हम कैनवा सीखेंगे, डिज़ाइन बनाएँगे और उसे कमाई का ज़रिया बनाएँगे। हर वीडियो पाँच से दस मिनट का है, और आप अपनी रफ़्तार से देख सकते हैं।

**[दृश्य: डिज़ाइन की दुनिया, नक़्शा और मिसालें]**

पहला हिस्सा: डिजिटल डिज़ाइन की दुनिया।

आज दुनिया भर के छोटे कारोबार, स्कूल, यूट्यूबर और ब्रांड हर रोज़ पोस्टर, सोशल मीडिया पोस्ट, लोगो और प्रेज़ेंटेशन बनवाते हैं। उन्हें डिज़ाइनर चाहिए, लेकिन हर बार महँगा स्टूडियो नहीं। इसी ज़रूरत से फ़्रीलांसिंग का मौक़ा पैदा होता है। आप अपने घर से, अपने वक़्त पर, दुनिया के किसी भी ग्राहक के लिए काम कर सकते हैं।

लेकिन यह मौक़ा उन्हीं को मिलता है जो ठीक से सीखते हैं और लगातार मेहनत करते हैं। इस कोर्स में हम बिल्कुल शुरू से शुरू करेंगे। आपको किसी ख़ास हुनर की ज़रूरत नहीं। बस एक कंप्यूटर या मोबाइल, इंटरनेट और सीखने का इरादा चाहिए।

**[दृश्य: canva.com का होम पेज]**

दूसरा हिस्सा: कैनवा से तआरुफ़।

कैनवा एक ऑनलाइन डिज़ाइन टूल है। इसे ब्राउज़र में खोलें, यानी canva.com पर जाएँ, या मोबाइल ऐप इस्तेमाल करें। इसमें तैयार टेम्पलेट होते हैं, यानी पहले से बने डिज़ाइन, जिन्हें आप अपनी मर्ज़ी से बदल सकते हैं। फ़ोटो, आइकन, फ़ॉन्ट और रंगों का बड़ा ख़ज़ाना भी मिल जाता है।

शुरुआत के लिए कैनवा का मुफ़्त वर्ज़न काफ़ी है। बाद में प्रो वर्ज़न लिया जा सकता है, जिसमें ज़्यादा सुविधाएँ मिलती हैं। अभी के लिए मुफ़्त वर्ज़न से ही काम चलाइए।

**[दृश्य: साइन अप स्क्रीन]**

तीसरा हिस्सा: अकाउंट बनाना।

canva.com पर जाकर साइन अप करें। आप गूगल, ईमेल या फ़ोन नंबर से रजिस्टर कर सकते हैं। अपना पासवर्ड मज़बूत रखें और किसी को न बताएँ। अकाउंट बनने के बाद प्रोफ़ाइल में अपना नाम और एक छोटी सी तआरुफ़ लाइन लिखें। यही आपकी ऑनलाइन शनाख़्त की पहली ईंट है।

**[दृश्य: अभ्यास की सूची]**

अब एक छोटा सा अभ्यास करें। पहले हफ़्ते में तीन काम कीजिए:

पहला, अकाउंट बनाइए और अपनी प्रोफ़ाइल भरिए।

दूसरा, कैनवा का कोई भी एक टेम्पलेट खोलिए और उसका टेक्स्ट बदल दीजिए। अपना नाम, अपनी बात, कोई भी लाइन।

तीसरा, अपने लिए एक सवाल लिखिए: मैं किस तरह का डिज़ाइन सबसे ज़्यादा पसंद करता हूँ? सोशल मीडिया पोस्ट, लोगो, या प्रेज़ेंटेशन? इसी जवाब से आपकी ट्रेनिंग का रास्ता तय होगा।

सीखने का सबसे अच्छा तरीक़ा यह है कि हर दिन थोड़ी देर बनाइए, पूरे हफ़्ते में एक बार बड़ा काम कीजिए, और अपनी ग़लतियों को नोट कीजिए। ग़लती से डरिए मत। हर ग़लती अगले डिज़ाइन में आपकी मददगार बनती है।

**[दृश्य: अगली वीडियो का पूर्वावलोकन]**

अगली वीडियो में हम कैनवा एडिटर को क़दम-ब-क़दम देखेंगे: बाएँ पैनल, टूलबार, परतें और पेज। अगर यह वीडियो काम का लगा हो तो चैनल सब्सक्राइब कीजिए। शुक्रिया, और मिलते हैं अगली वीडियो में।

---

## 6. Decisions needed from Homi

1. **Approve VoxCPM2 on homidev?** Installing the model and adding a `voice-ur-voxcpm` recipe is Homi's work on homidev. I will not change homidev myself. Once it is installed and approved, I can submit the jobs through `asset-job.sh`.
2. **Confirm the licence** (Apache-2.0 per the search snippets) before any release.
3. **Listening test first:** one paragraph in three versions (plain Hindi; Hindi with nukta letters; Hindi with nukta letters plus Urdu vocabulary). Homi picks the version that sounds most Urdu.
4. **Native check of the glossary and Video 1 script** before Videos 2–5 are written.
5. **Video length:** 5–10 minutes as above, combining chapters. Confirm the grouping in section 3.

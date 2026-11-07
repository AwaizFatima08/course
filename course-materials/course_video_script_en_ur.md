# AI Homelab on a Budget: Chapter-wise Video Script (English and Urdu narration)

Source: the course "Running an AI Homelab on a Budget" (English PDF and Urdu PDF, 15 chapters and 3 appendices).
Each chapter below is about 60 to 75 seconds of narration. Total runtime: about 18 to 20 minutes, plus a 40-second intro and outro.

Format for every chapter:
- **Screen:** what the viewer sees.
- **English narration:** for the English video.
- **Urdu narration:** for the Urdu video. Same visuals, same timing.

---

## Intro (0:00 to 0:40)

**Screen:** Title card. Quick montage of a laptop running a chat window, an image being generated, and a timeline being edited.

**English narration:**
"Do you want your own AI studio at home, running on a laptop or an old desktop? In this course you will prepare your machine, run local language models, make images and voice-overs, generate short video clips, and edit a complete YouTube video. No monthly subscriptions are needed for the tools. Let's begin."

**Urdu narration:**
"کیا آپ گھر پر اپنا AI اسٹوڈیو چاہتے ہیں، جو لیپ ٹاپ یا پرانے ڈیسک ٹاپ پر چلے؟ اس کورس میں آپ اپنی مشین تیار کریں گے، مقامی لینگوئج ماڈلز چلائیں گے، تصاویر اور وائس اوور بنائیں گے، مختصر ویڈیو کلپس تیار کریں گے، اور یوٹیوب کی مکمل ویڈیو ایڈٹ کریں گے۔ ٹولز کے لیے ماہانہ سبسکرپشن کی ضرورت نہیں۔ آئیے شروع کرتے ہیں۔"

---

## Chapter 1: Introduction (0:40 to 1:50)

**Screen:** The seven-stage production chain diagram (Figure 1.1), each box lighting up in turn.

**English narration:**
"Almost every YouTube video follows the same chain: idea, script, voice-over, pictures and clips, editing, export, and then learning from the numbers. Your homelab can help at every step. It will not do everything, and that is fine. Human checks on facts, tone and rights always stay in the loop."

**Urdu narration:**
"تقریباً ہر یوٹیوب ویڈیو ایک ہی سلسلے سے گزرتی ہے: خیال، اسکرپٹ، وائس اوور، تصاویر اور کلپس، ایڈیٹنگ، ایکسپورٹ، اور پھر نمبروں سے سیکھنا۔ آپ کا ہوم لیب ہر مرحلے میں مدد کر سکتا ہے۔ وہ سب کچھ نہیں کرے گا، اور یہ ٹھیک ہے۔ حقائق، لہجے اور حقوق کی انسانی جانچ ہمیشہ شامل رہتی ہے۔"

---

## Chapter 2: Hardware (1:50 to 3:00)

**Screen:** Memory ladder (Figure 2.1), then the model size bar chart (Figure 2.2).

**English narration:**
"Before you buy anything, understand what matters. The most important number is graphics memory, called VRAM. An AI model must fit there to run fast. System RAM is a slower backup. A seven-billion-parameter model, compressed to four bits, needs about four and a half gigabytes. Check that number before you choose any model."

**Urdu narration:**
"کچھ خریدنے سے پہلے سمجھیں کہ کیا اہم ہے۔ سب سے اہم عدد گرافکس میموری ہے، جسے VRAM کہتے ہیں۔ تیز چلنے کے لیے AI ماڈل کو وہیں سمانا ہوتا ہے۔ سسٹم RAM سست بیک اپ ہے۔ سات ارب پیرامیٹرز والا ماڈل، چار بٹس تک سکڑا ہوا، تقریباً ساڑھے چار گیگا بائٹ لیتا ہے۔ کوئی بھی ماڈل چننے سے پہلے یہ عدد ضرور دیکھیں۔"

---

## Chapter 3: Choosing a Budget Machine (3:00 to 4:10)

**Screen:** Decision chart (Figure 3.1), then a used graphics card label close-up.

**English narration:**
"You do not need an expensive machine. There are four tiers: a basic laptop for learning, a desktop with a used 12-gigabyte NVIDIA card for real work, and a 24-gigabyte card for heavy jobs. When you buy a used card, check its memory, its power supply, and whether it has been used for mining."

**Urdu narration:**
"آپ کو مہنگی مشین کی ضرورت نہیں۔ چار درجے ہیں: سیکھنے کے لیے بنیادی لیپ ٹاپ، حقیقی کام کے لیے 12 گیگا بائٹ کے استعمال شدہ NVIDIA کارڈ والا ڈیسک ٹاپ، اور بھاری کاموں کے لیے 24 گیگا بائٹ کا کارڈ۔ استعمال شدہ کارڈ خریدتے وقت اس کی میموری، پاور سپلائی، اور مائننگ کی تاریخ ضرور چیک کریں۔"

---

## Chapter 4: Operating Systems (4:10 to 5:20)

**Screen:** Two stacked-layer diagrams side by side (Figure 4.1). Then the Ubuntu logo and the Windows logo, without emphasis on either.

**English narration:**
"Now choose an operating system. Windows 11 with the Ollama app is the easiest start. Ubuntu 24.04 LTS is the most reliable choice for a dedicated AI machine. Both work well. Pick the one you can maintain, and remember that Windows can run Linux tools through WSL2."

**Urdu narration:**
"اب آپریٹنگ سسٹم چنیں۔ Ollama ایپ کے ساتھ Windows 11 سب سے آسان آغاز ہے۔ Ubuntu 24.04 LTS ایک مخصوص AI مشین کے لیے سب سے قابلِ اعتماد ہے۔ دونوں اچھے کام کرتے ہیں۔ وہ چنیں جسے آپ سنبھال سکیں، اور یاد رکھیں کہ Windows پر WSL2 کے ذریعے Linux ٹولز بھی چل سکتے ہیں۔"

---

## Chapter 5: Preparing the System (5:20 to 6:30)

**Screen:** Terminal with the command nvidia-smi running and the card name and memory highlighted. Then the folder tree.

**English narration:**
"Next, prepare the system. Set the BIOS options, install the NVIDIA driver, add swap memory, and create your folders. The most important test is simple. Run nvidia-smi. If your card appears with its full memory, you are ready for the next step."

**Urdu narration:**
"اگلا قدم سسٹم کی تیاری ہے۔ BIOS کی ترتیبات لگائیں، NVIDIA ڈرائیور انسٹال کریں، swap میموری شامل کریں، اور فولڈرز بنائیں۔ سب سے اہم جانچ سادہ ہے۔ nvidia-smi چلائیں۔ اگر آپ کا کارڈ اپنی پوری میموری کے ساتھ نظر آئے تو آپ اگلے قدم کے لیے تیار ہیں۔"

---

## Chapter 6: Core AI Stack (6:30 to 7:40)

**Screen:** Architecture diagram (Figure 6.1). Then the browser chat, then ollama ps showing "100% GPU".

**English narration:**
"Install Ollama and Open WebUI. Download a small model, chat in your browser, and check with ollama ps that the model runs fully on the graphics card. When these checks pass, your core homelab is working. Everything else in this course builds on it."

**Urdu narration:**
"Ollama اور Open WebUI انسٹال کریں۔ ایک چھوٹا ماڈل ڈاؤن لوڈ کریں، براؤزر میں چیٹ کریں، اور ollama ps سے دیکھیں کہ ماڈل مکمل طور پر گرافکس کارڈ پر چل رہا ہے۔ جب یہ جانچیں کامیاب ہوں تو آپ کا بنیادی ہوم لیب کام کر رہا ہے۔ کورس کی باقی ہر چیز اسی پر بنتی ہے۔"

---

## Chapter 7: Selecting LLM Models (7:40 to 8:50)

**Screen:** Quantization bar chart (Figure 7.1). Then a short personal test-set checklist on screen.

**English narration:**
"Choosing a model is about fit, not fame. Start with a size your memory can hold. Quantization shrinks a model with a small loss in quality. Then test two or three candidates on your own real tasks, and choose the smallest model that scores well."

**Urdu narration:**
"ماڈل کا انتخاب شہرت کے بجائے مطابقت پر ہوتا ہے۔ ایسے سائز سے شروع کریں جو آپ کی میموری میں آ جائے۔ Quantization ماڈل کو تھوڑے معیار کے نقصان کے ساتھ چھوٹا کرتی ہے۔ پھر دو تین امیدواروں کو اپنے حقیقی کاموں پر آزمائیں، اور وہ سب سے چھوٹا ماڈل چنیں جو اچھا اسکور کرے۔"

---

## Chapter 8: LLMs for Thinking, Coding and Scripts (8:50 to 10:00)

**Screen:** Three columns: quick writing, deep thinking, coding. The Modelfile text appearing line by line.

**English narration:**
"Use a general model for quick writing, a reasoning model for hard thinking, and a coding model for scripts. A scriptwriter model with a fixed system message keeps your style consistent. Make the model mark every claim that needs checking. The model drafts, and you decide what is true."

**Urdu narration:**
"فوری تحریر کے لیے عمومی ماڈل، مشکل سوچ کے لیے reasoning ماڈل، اور اسکرپٹس کے لیے کوڈنگ ماڈل استعمال کریں۔ ایک مقررہ system message والا scriptwriter ماڈل آپ کے انداز کو یکساں رکھتا ہے۔ ماڈل سے کہیں کہ ہر قابلِ تصدیق دعوے کو نشان زد کرے۔ ماڈل مسودہ لکھتا ہے، اور سچ کا فیصلہ آپ کرتے ہیں۔"

---

## Chapter 9: Image Generation (10:00 to 11:10)

**Screen:** ComfyUI node graph (Figure 9.1), then a thumbnail with text added in an editor.

**English narration:**
"For images, use ComfyUI with a model that fits your memory. Describe the subject, the style, the lighting and the composition. For thumbnails, generate the background, then add the title text in your editor, where spelling is reliable. Always get consent before you show a real person in an image."

**Urdu narration:**
"تصاویر کے لیے ComfyUI استعمال کریں، اور ایسا ماڈل جو آپ کی میموری میں آئے۔ موضوع، انداز، روشنی اور ترتیب بیان کریں۔ تھمب نیل کے لیے پس منظر AI سے بنائیں، پھر عنوان کا متن اپنے ایڈیٹر میں لگائیں، جہاں ہجے درست رہتے ہیں۔ کسی حقیقی شخص کی تصویر دکھانے سے پہلے ہمیشہ رضامندی لیں۔"

---

## Chapter 10: Narration and Voice (11:10 to 12:20)

**Screen:** Voice chain (Figure 10.1). Then a waveform with a loudness meter reading about minus 16.

**English narration:**
"Voice-over comes from text-to-speech. Choose one voice and keep it for the whole channel, so viewers recognise you. Write short sentences, check pronunciation, then normalise loudness to about minus sixteen LUFS. Listen to every voice-over before you use it, on both speakers and earphones."

**Urdu narration:**
"وائس اوور text-to-speech سے آتا ہے۔ ایک آواز چنیں اور پورے چینل میں اسی کو رکھیں، تاکہ ناظرین آپ کو پہچانیں۔ چھوٹے جملے لکھیں، تلفظ جانچیں، پھر آواز کی بلندی تقریباً منفی سولہ LUFS پر لائیں۔ ہر وائس اوور استعمال سے پہلے اسپیکر اور ایئر فون دونوں پر ضرور سنیں۔"

---

## Chapter 11: Video Generation (12:20 to 13:30)

**Screen:** Frame strip (Figure 11.1). Then a short generated clip labelled "B-roll", next to licensed footage and a screen recording.

**English narration:**
"AI video is powerful but slow. A five-second clip can take many minutes on a 12-gigabyte card. Plan each shot first, test at low resolution, and use generated clips as short B-roll. Mix them with licensed footage, your own screen recordings, and motion graphics for a strong result."

**Urdu narration:**
"AI ویڈیو طاقتور ہے مگر سست ہے۔ 12 گیگا بائٹ کارڈ پر پانچ سیکنڈ کا کلپ کئی منٹ لے سکتا ہے۔ ہر شاٹ کی پہلے منصوبہ بندی کریں، کم ریزولیوشن پر جانچیں، اور تخلیق شدہ کلپس کو مختصر B-roll کے طور پر استعمال کریں۔ بہتر نتیجے کے لیے انہیں لائسنس یافتہ فوٹیج، اپنی اسکرین ریکارڈنگز اور موشن گرافکس کے ساتھ ملائیں۔"

---

## Chapter 12: Video Editing and Export (13:30 to 14:40)

**Screen:** Timeline (Figure 12.1). Then the export settings table.

**English narration:**
"Edit in DaVinci Resolve or Kdenlive. Lay the narration first, then the shots, then graphics and music, with the music kept well below the voice. Add subtitles, check every line, and export at 1080p, 30 frames per second, using the settings in this chapter."

**Urdu narration:**
"DaVinci Resolve یا Kdenlive میں ایڈٹ کریں۔ پہلے بیانیہ لگائیں، پھر شاٹس، پھر گرافکس اور موسیقی، اور موسیقی کو آواز سے کافی نیچے رکھیں۔ سب ٹائٹلز شامل کریں، ہر سطر جانچیں، اور اس باب کی ترتیبات کے ساتھ 1080p، 30 فریمز فی سیکنڈ پر ایکسپورٹ کریں۔"

---

## Chapter 13: Automating the Production Line (14:40 to 15:50)

**Screen:** Nightly production-line diagram (Figure 13.1), with the human-check boxes highlighted in orange.

**English narration:**
"Automation turns these steps into a nightly production line. Machines do the drafting, voice and rendering overnight. People check facts, tone, rights and the final upload. Keep a job log, use quality gates, and never publish without a human check and the right disclosure."

**Urdu narration:**
"آٹومیشن ان مراحل کو رات کی پروڈکشن لائن میں بدل دیتی ہے۔ مشینیں رات کو مسودہ، آواز اور رینڈرنگ کرتی ہیں۔ انسان حقائق، لہجہ، حقوق اور آخری اپ لوڈ جانچتے ہیں۔ جاب لاگ رکھیں، معیار کے دروازے استعمال کریں، اور انسانی جانچ اور درست اعلان کے بغیر کبھی شائع نہ کریں۔"

---

## Chapter 14: Limits and Troubleshooting (15:50 to 17:00)

**Screen:** Decision flow (Figure 14.1). Then a terminal showing the error, then nvidia-smi and ollama ps.

**English narration:**
"Your hardware has limits, and things will fail. Do not panic. Read the error, check nvidia-smi and ollama ps, then change one setting at a time. Keep a log of what you changed. It is the fastest way to learn your own machine."

**Urdu narration:**
"آپ کے ہارڈ ویئر کی حدیں ہیں، اور کچھ چیزیں ناکام ہوں گی۔ گھبرائیں نہیں۔ خرابی کا پیغام پڑھیں، nvidia-smi اور ollama ps چیک کریں، پھر ایک وقت میں ایک ترتیب بدلیں۔ جو بدلا اس کا ریکارڈ رکھیں۔ اپنی مشین کو سمجھنے کا یہ سب سے تیز طریقہ ہے۔"

---

## Chapter 15: Career Path and Study Plan (17:00 to 18:10)

**Screen:** Twelve-week timeline (Figure 15.1), then the four budget levels.

**English narration:**
"Finally, make a plan. Start with what you already own, add upgrades only when you find the real bottleneck, and follow the twelve-week study plan. Build storytelling, editing and analytics skills as much as tool skills. Those are what make a channel last."

**Urdu narration:**
"آخر میں ایک منصوبہ بنائیں۔ اس سے شروع کریں جو آپ کے پاس پہلے سے ہے، اپ گریڈ صرف اصل رکاوٹ ملنے پر کریں، اور 12 ہفتے کے منصوبے پر چلیں۔ ٹولز کی مہارت کے ساتھ کہانی سنانے، ایڈیٹنگ اور تجزیے کی مہارت بھی بڑھائیں۔ یہی چیزیں چینل کو دیرپا بناتی ہیں۔"

---

## Outro (18:10 to 18:40)

**Screen:** End card with the course title, the chapter list, and the subscribe prompt.

**English narration:**
"Thank you for watching. The full course, with every command and every chapter, is linked below. Subscribe if you want to follow the build, and tell us which chapter you want us to go deeper into."

**Urdu narration:**
"دیکھنے کا شکریہ۔ پورا کورس، ہر کمانڈ اور ہر باب کے ساتھ، نیچے لنک میں ہے۔ اگر آپ یہ سیریز آگے دیکھنا چاہتے ہیں تو سبسکرائب کریں، اور بتائیں کہ کس باب کو مزید گہرائی سے سمجھایا جائے۔"

---

## Notes for the editor

- Read each narration aloud before recording to check timing: about 130 words per minute.
- Show every command on screen for at least three seconds, and mark it as an example to check on the day of use.
- Keep the same visual template for both language versions. Only the narration track and the on-screen title language change.
- Add a short disclosure on screen or in the description: the narration is synthetic (if synthetic voice is used) and the visuals include AI-generated material.

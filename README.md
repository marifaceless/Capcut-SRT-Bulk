# Capcut SRT Bulk Generator 🎬

Generate perfectly timed `.srt` subtitle files from multiple scripts — optimized for CapCut voiceovers, YouTube narration, and AI-generated content.

🔗 **Live App**: [https://capcut-srt-bulk.streamlit.app/](https://capcut-srt-bulk.streamlit.app/)

---

## ✨ Features

- 💬 Convert **multiple scripts at once**
- ⏱️ Auto-breaks text into SRT subtitle blocks:
  - 500 character max per block
  - 80–100 words per block
  - 30-second duration per block
  - 10-second gap between blocks
- 🕓 Adds a **60-second gap between each script**
- 🔢 Continuous subtitle numbering (no resets)
- 📥 One-click `.srt` download
- ✅ Clean, responsive Streamlit interface

---

## 📦 How to Use

1. Open the app: [capcut-srt-bulk.streamlit.app](https://capcut-srt-bulk.streamlit.app/)
2. Paste your first script
3. Click “➕ Add Script” to paste more scripts
4. When ready, click **“Generate SRT”**
5. Copy or download your subtitle file!

---

## 🧠 Use Cases

- AI Voiceover Projects
- CapCut Video Editing
- YouTube or TikTok Narration
- Bulk Podcast Transcriptions
- Audiobook Formatting

---

## 🛠️ Local Development

```bash
git clone https://github.com/marifaceless/Capcut-SRT-Bulk.git
cd Capcut-SRT-Bulk
pip install -r requirements.txt
streamlit run app.py

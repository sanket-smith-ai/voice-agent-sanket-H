# 🎙 AI Voice Agent — Setup & Run Guide

This document explains **how to clone, install, and run** the AI Voice Agent locally.

---

## 1. Clone the Repository

```bash
git clone https://github.com/sanket-smith-ai/voice-agent-sanket-H.git)
cd Simuphish
```

If you downloaded a ZIP, extract it and open the `Simuphish` folder.

---

## 2. Verify Python Version

Make sure Python **3.9 – 3.11** is installed (recommended: **3.10**).

```bash
python --version
```

or on Windows:

```bash
py -0
```

If multiple versions exist, ensure Python **3.10** is used.

---

## 3. Create Virtual Environment

Inside the project folder:

```bash
python -m venv aivoice
```

Activate it:

### Windows

```bash
aivoice\Scripts\activate
```

### Linux / macOS

```bash
source aivoice/bin/activate
```

You should now see `(aivoice)` in your terminal.

---

## 4. Upgrade Pip (Recommended)

```bash
pip install --upgrade pip
```

---

## 5. Install Project Dependencies

```bash
pip install -r requirements.txt
```

⏳ This may take time on first install (Torch, Whisper, audio libs).

---

## 6. Microphone Configuration (Important)

List available microphones:

```python
import sounddevice as sd
print(sd.query_devices())
```

Open `app.py` and set the correct mic index:

```python
MIC_DEVICE_INDEX = 1  # change based on your system
```

If your default mic works:

```python
MIC_DEVICE_INDEX = None
```

---

## 7. First Run (Models Auto-Download)

On first execution, the app **automatically downloads**:

* Whisper STT model
* Silero VAD model
* Lightweight TTS model

⚠ This happens **once only** and requires internet.

---

## 8. Run the Web Application (Recommended)

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 9. How to Use the App

1. Click **🎤 Speak / Start**
2. UI shows **Listening…**
3. Speak freely
4. AI transcribes your voice
5. AI generates a response
6. AI speaks the full response
7. Repeat for continuous voice-to-voice conversation

---

## 10. Run CLI Version (Optional)

For terminal testing only:

```bash
python main.py
```

Flow:

* Records one input
* Responds with voice
* Exits

---

## 11. Folder Structure Overview

```
Simuphish/
│
├── app.py              # Streamlit frontend
├── main.py             # CLI voice agent
├── model_manager.py    # Model auto-downloads
├── llm_engine.py       # Local LLM inference
├── whisper_stt.py      # Speech-to-text
│
├── audio/
│   ├── vad.py          # Voice activity detection
│   ├── tts.py          # Text-to-speech
│   ├── chunker.py      # Sentence chunking
│
├── requirements.txt
└── README.md
```

---

## 12. Common Issues & Fixes

### ❌ No Speech Detected

* Speak louder
* Check mic index
* Allow microphone permissions
* Reduce background noise

### ❌ No Voice Output

* Check speaker volume
* Do not speak while AI is talking
* Restart app after first model download

### ❌ Slow Response

* First run is slower
* Close heavy background apps
* Use headphones to reduce echo

---

## 13. Supported Features

✔ Fully local execution
✔ Voice-to-voice conversation
✔ English-only
✔ Real-time UI feedback
✔ Temp audio cleanup
✔ Offline after setup

---

## 14. Notes

* Uses **lightweight open-source models**
* No cloud APIs used

---


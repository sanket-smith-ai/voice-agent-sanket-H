# 🎙️ AI Voice Agent – Low-Latency, Open-Source Demo

This repository contains a **real-time AI voice agent** built to demonstrate **low-latency AI system design**, practical engineering trade-offs, and clean architecture using **open-source models only**.

The application enables **voice-to-voice interaction**:

> Speak → Transcribe → Generate AI response → Convert to speech → Play audio

The primary goal of this project is **technical evaluation**, not production scale.

---

## ✨ Key Highlights

* ⚡ **Low-latency focused architecture**
* 🎤 Microphone-based voice input
* 📝 Fast speech-to-text using Whisper (small model)
* 🧠 Lightweight local LLM for response generation
* 🔊 Text-to-speech output
* 🖥️ Streamlit UI for easy testing and demonstration
* 📦 Automatic model download on first run

---

## 🏗️ High-Level Architecture

```
Microphone
   ↓
Voice Activity Detection (VAD)
   ↓
Speech-to-Text (Whisper)
   ↓
LLM Response Generation
   ↓
Sentence Chunking
   ↓
Text-to-Speech
   ↓
Speaker Output
```

Each component is modular and can be replaced independently.

---

## 📁 Project Structure

```
.
├── app.py                 # Streamlit frontend (recommended)
├── main.py                # CLI-based voice agent
├── llm_engine.py          # LLM inference logic
├── whisper_stt.py         # Speech-to-text logic
├── model_manager.py       # Auto-download & model setup
├── requirements.txt       # Python dependencies
├── README.md              # Setup & usage guide
├── README_NOTES.md        # Architecture decisions & trade-offs
├── .gitignore             # Excludes models, env, cache
├── vad.py             # Voice activity detection
├── tts.py             # Text-to-speech
└── chunker.py         # Sentence chunking for smooth TTS
```

> 📝 **Model files, virtual environments, and cache directories are intentionally excluded from Git.**

---

## 💻 System Requirements

* **Python 3.10 (recommended)**
* Working microphone
* Internet connection (first run only – for model download)
* OS: Windows / macOS / Linux

---

## 🚀 Quick Start (Easy Setup)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/sanket-smith-ai/voice-agent-sanket-H.git
cd Simuphish
```

---

### 2️⃣ Create & Activate Virtual Environment

**Windows**

```bash
python -m venv aivoice
aivoice\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv aivoice
source aivoice/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

⏳ **Note:**
On the **first run**, required models (STT, LLM, TTS) will be downloaded automatically.

---

## ▶️ Running the Voice Agent (Recommended)

### ✅ Streamlit UI (Best for Testing)

```bash
streamlit run app.py
```

* A browser window opens automatically
* Click **🎤 Speak**
* Speak naturally into your microphone
* The UI shows:

  * “Listening…” while recording
  * Transcribed user speech
  * AI response text
* The AI responds **with voice output**

✔ This is the **recommended way to evaluate the voice agent**.

---

## 🧪 CLI Mode (Optional)

For terminal-only testing:

```bash
python main.py
```

* Records a short audio clip
* Transcribes speech
* Generates AI response
* Plays TTS output
* Useful for quick latency checks

---

## 🎯 Design Intent

This project is intentionally designed to be:

* **Easy to run**
* **Easy to understand**
* **Easy to extend**

All components run **locally** using open-source models to avoid external API dependencies.

---

## ⚠️ Limitations & Assumptions

* Uses **small open-source models** for faster local inference
* Responses may be less detailed than large proprietary models
* Single-user, demo-focused setup
* Not optimized for high background noise
* English-only (current configuration)

---

## 🔮 Future Improvements

* Streaming STT and token-level LLM output
* WebSocket-based real-time audio pipeline
* Cloud LLM / TTS integration
* Multi-language support
* Long-term conversational memory

---

## 📄 Additional Notes

For detailed explanations on:

* Architecture decisions
* Latency optimizations
* Trade-offs and constraints

👉 See **README_NOTES.md**

---

## 📌 Summary

This project demonstrates:

* Real-time AI system design
* Latency-aware engineering choices
* Clean modular architecture
* Practical use of open-source AI models


---




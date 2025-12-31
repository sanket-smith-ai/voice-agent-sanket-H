## 🔧 Model Choice Rationale & Constraints

This implementation intentionally uses **small, open-source models** for all core components (STT, LLM, and TTS).

### Reasoning

* **System Constraints**

  * The solution is designed to run on a **CPU-only environment**
  * Avoids GPU dependency to ensure broader compatibility
  * Keeps memory and compute usage low

* **No External API Dependency**

  * No reliance on paid or rate-limited APIs
  * Avoids issues related to:

    * API latency
    * Network instability
    * Free-tier credit exhaustion
  * Ensures the project runs fully **offline after setup**

* **Assessment Focus**

  * The primary goal of this task is **real-time interaction and latency optimization**
  * Smaller models allow:

    * Faster inference
    * Lower end-to-end response time
    * Predictable performance

---

##  Impact of Using Small Open-Source Models

Due to the use of lightweight models:

* The **LLM may not answer highly specific or complex questions accurately**
* Responses may be:

  * Shorter
  * Less nuanced
  * Occasionally generic

This limitation is **model-related**, not architectural.

---

## 🚀 Production & API-Based Enhancement Potential

The current architecture is intentionally **API-ready** and can be significantly improved by swapping components without redesigning the system.

### Possible Upgrades

With access to **external APIs or paid models**, the system can be enhanced with:

* High-accuracy LLMs (OpenAI, Claude, Gemini)
* Streaming speech-to-text APIs (Whisper API, Deepgram)
* Neural TTS engines (ElevenLabs, Azure TTS)
* Multilingual support
* Context-aware multi-turn conversations

> The modular design allows these upgrades with minimal code changes.

---

## ✅ Summary

* Open-source, small models were chosen **by design**
* This ensures:

  * Low latency
  * Offline capability
  * Easy setup and testing
* The **architecture itself is scalable** and production-ready

---

import os
import time
import tempfile
import sounddevice as sd
import soundfile as sf

from model_manager import ensure_models
from vad import is_speech
from whisper_stt import transcribe
from llm_engine import generate_response
from chunker import chunk_text
from tts import speak
from shared_state import state, lock

FS = 16000
DURATION = 4


def record_audio():
    with lock:
        state["status"] = "🎤 Listening..."

    audio = sd.rec(int(DURATION * FS), samplerate=FS, channels=1)
    sd.wait()

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        sf.write(tmp.name, audio, FS)
        return tmp.name


def voice_loop(stop_flag):
    ensure_models()
    speak("Voice agent started. You can speak now.")

    while not stop_flag["stop"]:
        audio_path = record_audio()

        try:
            with lock:
                state["status"] = "🧠 Processing..."

            if not is_speech(audio_path):
                with lock:
                    state["status"] = "❌ No speech detected"
                os.remove(audio_path)
                time.sleep(0.5)
                continue

            text = transcribe(audio_path)

            with lock:
                state["user_text"] = text
                state["ai_text"] = ""
                state["status"] = "🤖 Thinking..."

            response = generate_response(text)

            spoken = ""
            with lock:
                state["status"] = "🔊 Speaking..."

            for chunk in chunk_text(response):
                spoken += chunk + " "
                with lock:
                    state["ai_text"] = spoken
                speak(chunk)

            with lock:
                state["status"] = "🎤 Listening..."

            time.sleep(1.2)

        finally:
            if os.path.exists(audio_path):
                os.remove(audio_path)

    with lock:
        state["status"] = "⏹ Stopped"

    speak("Voice agent stopped.")

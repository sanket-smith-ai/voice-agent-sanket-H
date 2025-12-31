import pyttsx3
import time

def speak(text: str):
    if not text.strip():
        return

    # 🔑 Engine MUST be created inside the thread
    engine = pyttsx3.init()
    engine.setProperty("rate", 175)
    engine.setProperty("volume", 1.0)

    engine.say(text)
    engine.runAndWait()

    engine.stop()
    time.sleep(0.05)  # release audio device

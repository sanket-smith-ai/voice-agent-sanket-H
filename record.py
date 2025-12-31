import sounddevice as sd
import soundfile as sf

def record_audio(duration, fs=16000):
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    path = "input.wav"
    sf.write(path, audio, fs)
    return path

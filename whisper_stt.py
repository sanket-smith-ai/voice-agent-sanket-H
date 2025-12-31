from faster_whisper import WhisperModel

model = WhisperModel(
    "small.en",
    compute_type="int8",
    download_root="models/whisper"
)

def transcribe(audio_path):
    segments, _ = model.transcribe(audio_path)
    return " ".join(seg.text for seg in segments)

import torch
import soundfile as sf

# Load Silero VAD
model, utils = torch.hub.load(
    repo_or_dir="snakers4/silero-vad",
    model="silero_vad",
    trust_repo=True
)

(get_speech_timestamps, _, _, _, _) = utils


def is_speech(audio_path):
    audio, sr = sf.read(audio_path)

    # Convert stereo → mono
    if audio.ndim > 1:
        audio = audio.mean(axis=1)

    audio = torch.tensor(audio, dtype=torch.float32)

    # Lower threshold for laptop microphones
    timestamps = get_speech_timestamps(
        audio,
        model,
        sampling_rate=sr,
        threshold=0.3
    )

    return len(timestamps) > 0

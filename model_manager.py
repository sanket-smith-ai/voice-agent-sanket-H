import os
import urllib.request

LLM_URL = "https://huggingface.co/TheBloke/phi-2-GGUF/resolve/main/phi-2.Q4_K_M.gguf"


def download(url, path):
    if not os.path.exists(path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        print(f"⬇ Downloading {os.path.basename(path)}")
        urllib.request.urlretrieve(url, path)

def ensure_models():
    download(LLM_URL, "models/llm/phi-2.q4.gguf")

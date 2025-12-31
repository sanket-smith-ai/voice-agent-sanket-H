from llama_cpp import Llama

llm = Llama(
    model_path="models/llm/phi-2.q4.gguf",
    n_ctx=1024,
    n_threads=4,
    verbose=False,
)

SYSTEM_PROMPT = """
You are a real-time AI voice assistant.

Rules:
- Always respond in clear, natural English.
- Never respond in any other language.
- The user's input comes from speech transcription.
- Ignore filler words, pauses, and minor transcription errors.
- Keep responses short and conversational (1–3 sentences).
- Use a friendly and professional tone.
"""

def generate_response(text: str) -> str:
    prompt = f"""
<System>
{SYSTEM_PROMPT}
</System>

<User>
{text}
</User>

<Assistant>
"""

    result = llm(
        prompt,
        max_tokens=120,
        temperature=0.4,
        top_p=0.9,
        stop=[
            "</Assistant>",
            "<User>",
            "<System>",
        ],
    )

    raw = result["choices"][0]["text"]

    # 🧹 CLEAN OUTPUT
    cleaned = raw.split("</Assistant>")[0]
    cleaned = cleaned.replace("<Assistant>", "")
    cleaned = cleaned.strip()

    # Prevent accidental repetition
    lines = cleaned.splitlines()
    if len(lines) > 1:
        cleaned = lines[-1].strip()

    return cleaned

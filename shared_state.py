from threading import Lock

state = {
    "user_text": "",
    "ai_text": "",
    "status": "Idle"
}

lock = Lock()

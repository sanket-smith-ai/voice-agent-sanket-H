import streamlit as st
import threading
import time

from voice_loop import voice_loop
from shared_state import state, lock

st.set_page_config(page_title="AI Voice Agent", page_icon="🎤")
st.title("🎙 AI Voice Agent")
st.caption("Click Start → Speak → Listen to reply")

if "running" not in st.session_state:
    st.session_state.running = False
    st.session_state.stop_flag = {"stop": False}
    st.session_state.thread = None

status_box = st.empty()

col1, col2 = st.columns(2)
user_box = col1.empty()
ai_box = col2.empty()

if st.button("▶ Start Voice Agent") and not st.session_state.running:
    st.session_state.stop_flag["stop"] = False
    st.session_state.thread = threading.Thread(
        target=voice_loop,
        args=(st.session_state.stop_flag,),
        daemon=True
    )
    st.session_state.thread.start()
    st.session_state.running = True
    st.success("Voice agent started")

if st.button("⏹ Stop Voice Agent") and st.session_state.running:
    st.session_state.stop_flag["stop"] = True
    st.session_state.running = False
    st.warning("Voice agent stopped")

# 🔄 Live UI updates
while st.session_state.running:
    with lock:
        status_box.info(state["status"])
        user_box.markdown(f"### 🧑 You\n{state['user_text']}")
        ai_box.markdown(f"### 🤖 AI\n{state['ai_text']}")

    time.sleep(0.2)

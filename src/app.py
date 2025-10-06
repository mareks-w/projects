# save this as app.py
import streamlit as st
import matplotlib.pyplot as plt
from run_pitch_coaching import run_pitch_coaching

st.title("🎤 PitchPerfect: ML Singing Coach")

uploaded = st.file_uploader("Upload your singing (.wav)", type=["wav"])
if uploaded:
    with open("temp.wav", "wb") as f:
        f.write(uploaded.read())

    st.success("Audio uploaded!")
    result = run_pitch_coaching("temp.wav")

    st.subheader("Pitch Accuracy")
    st.metric("Within ±50 cents", f"{result['pitch_accuracy']}%")

    st.subheader("Pitch Deviation Curve")
    fig, ax = plt.subplots()
    ax.plot(result["cents"], label="Cents Deviation")
    ax.axhline(0, color="gray", linestyle="--")
    ax.axhline(50, color="green", linestyle="--")
    ax.axhline(-50, color="red", linestyle="--")
    ax.set_ylabel("Cents Deviation")
    ax.set_xlabel("Frame")
    ax.legend()
    st.pyplot(fig)

    st.subheader("GLAP-based Feedback")
    for label, score in result["scores"].items():
        st.write(f"**{label}:** {score}")

import streamlit as st
import random

st.set_page_config(
    page_title="Number Guessing Game",
    page_icon="🎯"
)

st.title("🎯 Number Guessing Game")
st.write("I have chosen a number between 1 and 100.")

# Start game
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.message = ""

# Input
guess = st.number_input(
    "Enter your guess:",
    min_value=1,
    max_value=100,
    step=1
)

# Guess button
if st.button("🔍 Guess"):
    st.session_state.attempts += 1

    if guess < st.session_state.number:
        st.session_state.message = "🔵 Too low! Try again."

    elif guess > st.session_state.number:
        st.session_state.message = "🟠 Too high! Try again."

    else:
        st.session_state.message = (
            f"🎉 Correct! You guessed the number in "
            f"{st.session_state.attempts} attempts."
        )

# Display message
if st.session_state.message:
    st.info(st.session_state.message)

# Attempts
st.write(f"📊 Attempts: {st.session_state.attempts}")

# Restart button
if st.button("🔄 Play Again"):
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.message = ""
    st.rerun()
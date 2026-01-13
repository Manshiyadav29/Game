import streamlit as st
import random

st.title("🎯 Number Guessing Game")

if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.over = False

guess = st.number_input("Guess a number between 1 and 100", 1, 100)

if st.button("Check"):
    st.session_state.attempts += 1
    if guess < st.session_state.number:
        st.warning("Too low!")
    elif guess > st.session_state.number:
        st.warning("Too high!")
    else:
        st.success(f"🎉 Correct! You guessed it in {st.session_state.attempts} attempts.")
        st.balloons()
        st.session_state.over = True

if st.session_state.over and st.button("Restart"):
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.over = False

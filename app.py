import streamlit as st
import random

st.set_page_config(page_title="Rock Paper Scissors Game")

st.title("✊ 🖐️ ✌️ Rock-Paper-Scissors Game")
st.write("Play against the computer!")

choices = ["rock", "paper", "scissor"]

user_choice = st.selectbox("Choose your move:", choices)

if st.button("Play"):
    computer_choice = random.choice(choices)
    st.write(f"💻 Computer chose: **{computer_choice}**")

    if user_choice == computer_choice:
        st.success("It's a tie!")
    elif user_choice == "rock" and computer_choice == "scissor":
        st.success("You win!")
    elif user_choice == "paper" and computer_choice == "rock":
        st.success("You win!")
    elif user_choice == "scissor" and computer_choice == "paper":
        st.success("You win!")
    else:
        st.error("Computer wins!")

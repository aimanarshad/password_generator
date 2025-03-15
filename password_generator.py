# ----------------------------------password generater using stremalit----------------------------------------------
#uv init password_manager
#cd password manager
#uv venv
#copy path and past
#uv add streamlit
#change main.py to passowrd_generated.py
#streamlit run password_generater


import streamlit as st
import random
import string

def password_generator(length, use_digits, use_special):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    return ''.join(random.choice(characters) for _ in range(length))

st.title("Password Generator")

length = st.slider("Select Password Length", min_value=4, max_value=32, value=12)
use_digits = st.checkbox("Include Digits")
use_special = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    password = password_generator(length, use_digits, use_special)
    st.write(f"Generated Password: `{password}`")










# ascii_letters--------------->give uppercase and lower case letters from string
# join-------------->join the random character in a specific words
# choice----------->provide random chracter
# _------------------>tell that loop has no specific length
# min_value---------->is a parameter and we will give it a arrgument means pass it a specific value

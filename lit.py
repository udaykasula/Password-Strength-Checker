import streamlit as st
import re
from streamlit.runtime.scriptrunner import add_script_run_ctx
import threading

# Add Streamlit context to the main thread to avoid warnings
def run_with_context():
    add_script_run_ctx(threading.current_thread())

run_with_context()

st.title("🔐 Password Strength Tester")
st.write("Check how strong your password is!")

def check_strength(password):
    strength = 0
    remarks = []

    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        remarks.append("Add an uppercase letter.")

    if re.search(r'[a-z]', password):
        strength += 1
    else:
        remarks.append("Add a lowercase letter.")

    if re.search(r'[0-9]', password):
        strength += 1
    else:
        remarks.append("Include a number.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        remarks.append("Use a special character.")

    return strength, remarks

password = st.text_input("Enter a password:", type="password")

if st.button("Check Strength"):
    strength, feedback = check_strength(password)
    
    if strength < 3:
        st.error(f"Weak Password ({strength}/5) ❌")
    elif strength < 5:
        st.warning(f"Moderate Password ({strength}/5) ⚠️")
    else:
        st.success(f"Strong Password ({strength}/5) ✅")
    
    if feedback:
        st.subheader("Suggestions to Improve:")
        for item in feedback:
            st.write(f"- {item}")
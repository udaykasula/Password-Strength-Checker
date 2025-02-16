import streamlit as st
import re
from streamlit.runtime.scriptrunner import add_script_run_ctx
import threading
import webbrowser
import time
st.image("./img/uk.jpg")
st.markdown('<h1 style="color:purple;">Check Your Privacy by UK</h1>', unsafe_allow_html=True)


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
        st.toast("Can Be Hacked...", icon="👨‍💻")
    elif strength < 5:
        st.warning(f"Moderate Password ({strength}/5) ⚠️")
    else:
        st.success(f"Strong Password ({strength}/5) ✅")
        st.toast("Hard To Hack...", icon="👨‍💻")
    
    # if feedback:
    #     st.subheader("Suggestions to Improve:")
    #     for item in feedback:
    #         st.write("ham here to write")

col1, col2, col3 = st.columns([1,2,1])

def show_feedback():
    st.markdown('<p style="color:purple; font-size:20px;">Suggestions to Improve</p>', unsafe_allow_html=True)

# show_feedback()
# st.link_button("Visit Instagram🅾", "https://www.instagram.com/uday_kasula_?igsh=cTBsbTh1dzNwaHcw")

# if 'show_snow' not in st.session_state:
#     st.session_state.show_snow = False

# Show link button
# if st.link_button("Visit Instagram 🅾", "https://www.instagram.com/uday_kasula_?igsh=cTBsbTh1dzNwaHcw"):
#     st.session_state.show_snow = True

# Display snow if the button was clicked
# if st.session_state.show_snow:
#     st.snow()
#     st.toast("Secure Yourself! ", icon="🌐")

# def show_feedback():
#     st.markdown('<p style="color:purple; font-size:20px;">Suggestions to Improve</p>', unsafe_allow_html=True)

st.markdown('<p style="color:purple; font-size:20px;">Suggestions to Improve</p>', unsafe_allow_html=True)
if st.button("Visit Instagram 🅾"):
    with st.spinner('Loading Instagram... 🚀'):
        time.sleep(2)  # Simulate loading time
    st.success('Ready to launch! 🌟')
    time.sleep(0.5)
    
    webbrowser.open_new_tab("https://www.instagram.com/uday_kasula_?igsh=cTBsbTh1dzNwaHcw")
import re
import streamlit as st

# Set page title
st.set_page_config(page_title="Password Strength Meter", layout="centered")

# Title
st.title("🔐 Password Strength Meter")

def check_password(password):
    score = 0
    feedback = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check uppercase and lowercase letters
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password should include both uppercase and lowercase letters.")

    # Check digits
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Password should include at least one digit (0-9).")

    # Check special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Password should include at least one special character (!@#$%^&*).")

    return score, feedback

# User input
password = st.text_input("Enter your password:", type="password")

# Button to check strength
if st.button("Check Strength"):
    if password:
        score, feedback = check_password(password)

        # Display password strength
        if score == 4:
            st.success("✅ Strong password! Your password is secure.")
        elif score == 3:
            st.info("⚠ Moderate password. Consider adding more security features.")
        else:
            st.error("❌ Weak password. Follow the suggestions below.")

        # Display feedback
        if feedback:
            with st.expander("🔧 Improve your password:"):
                for item in feedback:
                    st.write(f"- {item}")

    else:
        st.warning("Please enter a password!")

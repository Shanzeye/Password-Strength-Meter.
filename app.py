import streamlit as st
import re

# Function to calculate password strength
def check_password_strength(password):
    score = 0
    # Length check
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    # Check for digits
    if re.search(r'\d', password):
        score += 1
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    # Check for special characters
    if re.search(r'[@$!%*?&]', password):
        score += 1
    # Calculate strength based on score
    if score <= 2:
        strength = "Weak"
        color = "red"
    elif score <= 4:
        strength = "Moderate"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"
    return strength, color

# Streamlit UI
st.markdown(
    """
    <style>
        /* Body background color */
        .stApp {
            background-color: #f3f4f6 !important;
            font-family: 'Arial', sans-serif;
        }

        /* Title Styling */
        .main-title {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            color: #4CAF50;
            margin-bottom: 30px;
        }

        /* Input Box Styling */
        .stTextInput input {
            padding: 12px;
            font-size: 18px;
            border-radius: 12px;
            border: 1px solid #d3d3d3;
            background-color: #ffffff;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        }

        .stTextInput label {
            font-size: 18px;
            font-weight: bold;
            color: #333333;
        }

        /* Button Styling */
        .stButton {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            border-radius: 12px;
            padding: 12px 25px;
            font-size: 16px;
            transition: background-color 0.3s;
        }

        .stButton:hover {
            background-color: #45a049;
            cursor: pointer;
        }

        /* Progress Bar Styling */
        .stProgress div {
            border-radius: 8px;
        }

        /* Result Text Styling */
        .result-text {
            font-size: 22px;
            font-weight: bold;
            color: #FF5722;
            text-align: center;
            margin-top: 30px;
        }

        /* Centering the main content */
        .content-center {
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        /* Title Styling */
        .stTextInput {
            margin-top: 20px;
            margin-bottom: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit title and description
st.markdown("<h1 class='main-title'>🔒 Password Strength Meter</h1>", unsafe_allow_html=True)

# Input field for password
password = st.text_input("Enter your password", type="password")

# Check password strength
if password:
    strength, color = check_password_strength(password)
    # Display password strength
    st.markdown(f"<h3 class='result-text' style='color:{color};'>Password Strength: {strength}</h3>", unsafe_allow_html=True)

    # Display the strength meter
    if strength == "Weak":
        st.progress(33)
    elif strength == "Moderate":
        st.progress(66)
    elif strength == "Strong":
        st.progress(100)

    # Additional password criteria
    st.markdown("### Tips to improve password strength:")
    st.markdown("- Use at least 12 characters.")
    st.markdown("- Include uppercase and lowercase letters.")
    st.markdown("- Use digits and special characters (e.g., `@`, `$`, `!`).")
else:
    st.markdown("<p style='color:gray;'>Please enter a password to check its strength.</p>", unsafe_allow_html=True)

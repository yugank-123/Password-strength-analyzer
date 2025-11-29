import streamlit as st
import re
import math

# Function to calculate password strength
def calculate_strength(password):
    length = len(password)
    strength = 0
    
    # Check for character types
    if re.search(r'[a-z]', password):
        strength += 1
    if re.search(r'[A-Z]', password):
        strength += 1
    if re.search(r'\d', password):
        strength += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    
    # Length bonus
    if length >= 8:
        strength += 1
    if length >= 12:
        strength += 1

    # Entropy estimation
    entropy = length * math.log2(2 + strength)
    
    return strength, entropy

# Streamlit UI
st.title("🔒 Password Strength Analyzer")
st.write("Check your password strength and get suggestions to improve it.")

password = st.text_input("Enter your password", type="password")

if password:
    strength, entropy = calculate_strength(password)
    
    if strength <= 2:
        st.error("Weak Password ❌")
    elif strength <= 4:
        st.warning("Moderate Password ⚠️")
    else:
        st.success("Strong Password ✅")
    
    st.info(f"Password Strength Score: {strength}/6 | Estimated Entropy: {entropy:.2f}")
    
    # Suggestions
    suggestions = []
    if len(password) < 8:
        suggestions.append("Use at least 8 characters")
    if not re.search(r'[A-Z]', password):
        suggestions.append("Include uppercase letters")
    if not re.search(r'[a-z]', password):
        suggestions.append("Include lowercase letters")
    if not re.search(r'\d', password):
        suggestions.append("Include numbers")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        suggestions.append("Include special characters")
    
    if suggestions:
        st.subheader("Suggestions to Improve Password:")
        for s in suggestions:
            st.write(f"- {s}")

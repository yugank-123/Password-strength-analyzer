import tkinter as tk
from tkinter import messagebox
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

# Function to handle password input and show results
def analyze_password():
    password = password_entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password.")
        return
    
    strength, entropy = calculate_strength(password)
    
    if strength <= 2:
        result_label.config(text="Weak Password ❌", fg="red")
    elif strength <= 4:
        result_label.config(text="Moderate Password ⚠️", fg="orange")
    else:
        result_label.config(text="Strong Password ✅", fg="green")
    
    score_label.config(text=f"Strength Score: {strength}/6 | Estimated Entropy: {entropy:.2f}")
    
    suggestions = []
    if len(password) < 8:
        suggestions.append("Use at least 8 characters")
    if not re.search(r'[A-Z]', password):
        suggestions.append("Include uppercase letters")
    if not re.search(r'[a-z]', password):
        suggestions.append("Include lowercase letters")
    if not re.search(r'\d', password):
        suggestions.append("Include numbers")
    if not re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        suggestions.append("Include special characters")
    
    suggestion_text = "\n".join(suggestions) if suggestions else "Your password is strong!"
    suggestion_label.config(text=suggestion_text)

# Tkinter GUI setup
root = tk.Tk()
root.title("Password Strength Analyzer")
root.geometry("400x350")

tk.Label(root, text="Enter your password:", font=("Arial", 12)).pack(pady=10)
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)

tk.Button(root, text="Check Strength", command=analyze_password).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=5)

score_label = tk.Label(root, text="", font=("Arial", 10))
score_label.pack(pady=5)

suggestion_label = tk.Label(root, text="", font=("Arial", 10), justify="left")
suggestion_label.pack(pady=10)

root.mainloop()

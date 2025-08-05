import tkinter as tk
from tkinter import messagebox
import re

# ------------------------
# Function to assess password
# ------------------------
def assess_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("❌ Minimum 8 characters required.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("❌ Add uppercase letters.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("❌ Add lowercase letters.")

    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("❌ Add digits.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("❌ Add special characters.")

    if strength == 5:
        level = ("Very Strong", "green")
    elif strength == 4:
        level = ("Strong", "#4caf50")
    elif strength == 3:
        level = ("Moderate", "#ffc107")
    elif strength == 2:
        level = ("Weak", "#ff5722")
    else:
        level = ("Very Weak", "red")

    return level, feedback

# ------------------------
# GUI Functions
# ------------------------
def check_strength():
    pwd = entry.get()
    if not pwd:
        messagebox.showwarning("Warning", "Please enter a password")
        return

    level, suggestions = assess_password_strength(pwd)
    strength_label.config(text=f"Strength: {level[0]}", fg=level[1])

    suggestion_text = "\n".join(suggestions) if suggestions else "✅ Great password!"
    suggestions_label.config(text=suggestion_text)

def copy_to_clipboard():
    pwd = entry.get()
    if not pwd:
        messagebox.showinfo("Info", "No password to copy!")
        return
    root.clipboard_clear()
    root.clipboard_append(pwd)
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# ------------------------
# Main Window
# ------------------------
root = tk.Tk()
root.title("Password Strength Analyzer")
root.geometry("500x350")
root.resizable(False, False)
root.configure(bg="#1e1e2f")

# ------------------------
# UI Elements
# ------------------------

title = tk.Label(root, text="🔐 Password Strength Analyzer", font=("Helvetica", 16, "bold"),
                 bg="#1e1e2f", fg="cyan")
title.pack(pady=10)

entry = tk.Entry(root, font=("Helvetica", 14), show="*", width=30, bd=2, relief="flat")
entry.pack(pady=10)

# Analyze Button
analyze_btn = tk.Button(root, text="Analyze", font=("Helvetica", 12, "bold"),
                        bg="#2196f3", fg="white", padx=10, pady=5,
                        activebackground="#1976d2", activeforeground="white",
                        relief="flat", command=check_strength)
analyze_btn.pack(pady=5)

# Copy Button
copy_btn = tk.Button(root, text="Copy Password", font=("Helvetica", 12, "bold"),
                     bg="#4caf50", fg="white", padx=10, pady=5,
                     activebackground="#388e3c", activeforeground="white",
                     relief="flat", command=copy_to_clipboard)
copy_btn.pack(pady=5)

# Strength Label
strength_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"),
                          bg="#1e1e2f", fg="white")
strength_label.pack(pady=5)

# Suggestions Label
suggestions_label = tk.Label(root, text="", font=("Helvetica", 11),
                             bg="#1e1e2f", fg="#e0e0e0", justify="left", wraplength=450)
suggestions_label.pack(pady=5)

# ------------------------
# Run the App
# ------------------------
root.mainloop()


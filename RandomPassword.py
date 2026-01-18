import tkinter as tk
import random
import string

# Function to generate random password
def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to display password in GUI
def show_password():
    try:
        length = int(entry_length.get())
    except ValueError:
        result_label.config(text="Please enter a valid number!")
        return
    
    password = generate_password(length)
    result_label.config(text=f"Generated Password: {password}")

# Tkinter GUI setup
root = tk.Tk()
root.title("Random Password Generator")

# Label and Entry for password length
tk.Label(root, text="Enter password length:").pack(pady=5)
entry_length = tk.Entry(root)
entry_length.pack(pady=5)

# Button to generate password
tk.Button(root, text="Generate Password", command=show_password).pack(pady=10)

# Label to display result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the GUI loop
root.mainloop()

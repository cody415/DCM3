import tkinter as tk
import random

# Function to play the game
def play(choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)

    # Show choices
    result_text = f"You chose: {choice}\nComputer chose: {computer_choice}\n"

    # Decide winner using conditionals
    if choice == computer_choice:
        result_text += "Result: It's a Tie!"
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        result_text += "Result: You Win!"
    else:
        result_text += "Result: Computer Wins!"

    result_label.config(text=result_text)

# Tkinter GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors Game")

# Instructions
tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 12)).pack(pady=10)

# Buttons for choices
tk.Button(root, text="Rock", width=15, command=lambda: play("Rock")).pack(pady=5)
tk.Button(root, text="Paper", width=15, command=lambda: play("Paper")).pack(pady=5)
tk.Button(root, text="Scissors", width=15, command=lambda: play("Scissors")).pack(pady=5)

# Result display
result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=20)

# Run the GUI loop (loop keeps program running)
root.mainloop()

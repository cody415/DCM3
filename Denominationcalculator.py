import tkinter as tk

# Function to calculate denominations
def calculate_notes():
    try:
        amount = int(entry_amount.get())
        if amount < 100:
            result_label.config(text="Enter amount of at least 100")
            return

        # Calculate notes
        n2000 = amount // 2000
        amount %= 2000

        n500 = amount // 500
        amount %= 500

        n100 = amount // 100
        amount %= 100

        # Display result
        result_text = (
            f"2000 Notes: {n2000}\n"
            f"500 Notes: {n500}\n"
            f"100 Notes: {n100}\n"
        )
        result_label.config(text=result_text)

    except ValueError:
        result_label.config(text="Please enter a valid number!")

# Tkinter GUI setup
root = tk.Tk()
root.title("Denomination Calculator")

# Label and Entry for amount
tk.Label(root, text="Enter Amount:", font=("Arial", 12)).pack(pady=5)
entry_amount = tk.Entry(root, font=("Arial", 12))
entry_amount.pack(pady=5)

# Button to calculate
tk.Button(root, text="Calculate Notes", font=("Arial", 12), command=calculate_notes).pack(pady=10)

# Label to display result
result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=10)

# Run the GUI loop
root.mainloop()

#TASK-2-------CALCULATOR---------


import tkinter as tk

# ---------------------------
# Main Window
# ---------------------------
root = tk.Tk()
root.title("Modern Calculator")
root.geometry("420x520")   # ← INCREASED WIDTH
root.config(bg="#1e1e1e")  # Dark modern background

# ---------------------------
# Display Screen
# ---------------------------
display = tk.Entry(
    root, font=("Arial", 28), bg="#2d2d2d", fg="white",
    bd=0, highlightthickness=0, justify="right"
)
display.pack(fill="both", ipadx=8, ipady=20, padx=10, pady=20)


# ---------------------------
# Functions
# ---------------------------
def add_to_display(value):
    display.insert("end", value)

def clear_display():
    display.delete(0, "end")

def calculate():
    try:
        expression = display.get()
        result = eval(expression)
        clear_display()
        display.insert("end", str(result))
    except:
        clear_display()
        display.insert("end", "Error")


# ---------------------------
# Button Layout
# ---------------------------
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack()

buttons = [
    ["C", "7", "8", "9", "÷"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

for row in buttons:
    row_frame = tk.Frame(frame, bg="#1e1e1e")
    row_frame.pack(pady=5)

    for btn in row:

        if btn == "=":
            b = tk.Button(
                row_frame, text=btn, font=("Arial", 20, "bold"),
                width=5, height=2, bg="#0fb9b1", fg="white",
                activebackground="#0aa39c", bd=0,
                command=calculate
            )

        elif btn == "C":
            b = tk.Button(
                row_frame, text="C", font=("Arial", 20, "bold"),
                width=5, height=2, bg="#eb3b5a", fg="white",
                activebackground="#cf3047", bd=0,
                command=clear_display
            )

        elif btn == "÷":   # divide symbol
            b = tk.Button(
                row_frame, text="÷", font=("Arial", 20),
                width=5, height=2, bg="#3b3b3b", fg="white",
                activebackground="#555", bd=0,
                command=lambda: add_to_display("/")
            )

        else:
            b = tk.Button(
                row_frame, text=btn, font=("Arial", 20),
                width=5, height=2, bg="#3b3b3b", fg="white",
                activebackground="#555", bd=0,
                command=lambda b=btn: add_to_display(b)
            )

        b.pack(side="left", padx=5)


# ---------------------------
# CLEAR Button (bottom)
# ---------------------------
clear_btn = tk.Button(
    root, text="CLEAR", font=("Arial", 20, "bold"),
    width=20, height=2, bg="#eb3b5a", fg="white",
    activebackground="#cf3047", bd=0,
    command=clear_display
)
clear_btn.pack(pady=20)

root.mainloop()


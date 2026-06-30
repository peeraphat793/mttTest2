import tkinter as tk

# -------------------- Window --------------------
root = tk.Tk()
root.title("Modern Calculator")
root.geometry("380x600")
root.configure(bg="#1E1E2E")
root.resizable(False, False)

expression = ""

# -------------------- Functions --------------------
def press(value):
    global expression
    expression += str(value)
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set("")

def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)

def equal():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

# -------------------- Display --------------------
equation = tk.StringVar()

display = tk.Entry(
    root,
    textvariable=equation,
    font=("Segoe UI", 28),
    bg="#2A2A3D",
    fg="white",
    bd=0,
    justify="right",
    insertbackground="white"
)

display.pack(fill="both", padx=15, pady=20, ipady=25)

# -------------------- Button Style --------------------
btn_font = ("Segoe UI", 18, "bold")

button_color = "#313244"
operator_color = "#F38BA8"
equal_color = "#89B4FA"
text_color = "white"

frame = tk.Frame(root, bg="#1E1E2E")
frame.pack(expand=True, fill="both", padx=10, pady=10)

buttons = [
    ["C", "⌫", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["(", "0", ")", "="],
    [".", ""]
]

for r, row in enumerate(buttons):
    frame.rowconfigure(r, weight=1)

for c in range(4):
    frame.columnconfigure(c, weight=1)

for r, row in enumerate(buttons):
    for c, item in enumerate(row):
        if item == "":
            continue

        color = button_color

        if item in ["+", "-", "*", "/", "%"]:
            color = operator_color

        if item == "=":
            color = equal_color

        if item == "C":
            cmd = clear
        elif item == "⌫":
            cmd = backspace
        elif item == "=":
            cmd = equal
        else:
            cmd = lambda x=item: press(x)

        btn = tk.Button(
            frame,
            text=item,
            command=cmd,
            font=btn_font,
            bg=color,
            fg=text_color,
            bd=0,
            relief="flat",
            activebackground="#585B70",
            activeforeground="white",
            cursor="hand2"
        )

        btn.grid(
            row=r,
            column=c,
            padx=6,
            pady=6,
            sticky="nsew",
            ipadx=10,
            ipady=20
        )

root.mainloop()
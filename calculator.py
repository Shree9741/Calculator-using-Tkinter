import tkinter as tk
#this is python file
def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                value = "Error"
        scvalue.set(value)
        screen.update()
    elif text == "c":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = tk.Tk()
root.geometry("300x400")
root.title("CALCULATOR")

scvalue = tk.StringVar()
scvalue.set("")
screen = tk.Entry(root, textvar=scvalue, font=("Helvetica", 20))
screen.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=8, ipady=10, sticky="nsew")

buttons = [
    ("7", "#D1B2FF"), ("8", "#D1B2FF"), ("9", "#D1B2FF"), ("/", "#FFC478"),
    ("4", "#D1B2FF"), ("5", "#D1B2FF"), ("6", "#D1B2FF"), ("*", "#FFC478"),
    ("1", "#D1B2FF"), ("2", "#D1B2FF"), ("3", "#D1B2FF"), ("-", "#FFC478"),
    ("c", "#FFC478"), ("0", "#FFC478"), ("=", "#FFC478"), ("+", "#FFC478")
]

row_value = 1
col_value = 0

for button_text, button_color in buttons:
    button = tk.Button(root, text=button_text, padx=10, pady=10, font=("Helvetica", 15), bg=button_color)
    button.grid(row=row_value, column=col_value, padx=5, pady=5, sticky="nsew")
    button.bind("<Button-1>", click)
    
    col_value += 1
    if col_value > 3:
        col_value = 0
        row_value += 1

# Configure row and column weights to make the buttons expand with window resizing
for i in range(1, 5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()

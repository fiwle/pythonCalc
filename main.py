import tkinter as tk
from tkinter import ttk

expr = ""


def btn_click(item):
    try:
        global expr
        input_field['state'] = "normal"
        expr += item
        input_field.insert(tk.END, item)
        if item == '=':
            result = str(eval(expr[:-1]))
            input_field.delete(0, tk.END)
            input_field.insert(tk.END, result)
            expr = ""
        if len(expr) > 16:
            expr = expr[:-1]
            input_field.delete(0, tk.END)
            input_field.insert(tk.END, expr)
        input_field['state'] = "readonly"
    except ZeroDivisionError:
        input_field.delete(0, tk.END)
        input_field.insert(tk.END, "Error: Zero division")
    except SyntaxError:
        input_field.delete(0, tk.END)
        input_field.insert(tk.END, "Error")


def btn_clear():
    global expr
    expr = ""
    input_field["state"] = "normal"
    input_field.delete(0, tk.END)
    input_field["state"] = "readonly"


def btn_del():
    global expr
    expr = expr[:-1]
    input_field["state"] = "normal"
    input_field.delete(0, tk.END)
    input_field.insert(tk.END, expr)
    input_field["state"] = "readonly"


root = tk.Tk()
root.title("Calculator")
root.geometry("480x560")
root.resizable(False, False)
root.columnconfigure(index=0, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=6)

input_frame = ttk.Frame(root, padding=10)
input_frame.grid(column=0, row=0, columnspan=1, sticky="nsew")

input_field = ttk.Entry(input_frame, font="Comfortaa 36 bold", state="readonly")
input_field.pack(fill=tk.BOTH, expand=True)

btns = (('7', '8', '9', '/'),
        ('4', '5', '6', '*'),
        ('1', '2', '3', '-'),
        ('0', '.', '=', '+'))

btns_frame = ttk.Frame(root)
btns_frame.grid(column=0, row=1, sticky="nsew")
for i in range(4):
    btns_frame.columnconfigure(index=i, weight=1)
for i in range(5):
    btns_frame.rowconfigure(index=i, weight=1)


button_del = ttk.Button(btns_frame, text="DEL", command=lambda: btn_del())
button_del.grid(row=0, column=2, columnspan=1, sticky="nsew")

button_clear = ttk.Button(btns_frame, text='C', command=lambda: btn_clear())
button_clear.grid(row=0, column=3, columnspan=1, sticky="nsew")

for row in range(4):
    for col in range(4):
        ttk.Button(btns_frame, width=2, text=btns[row][col],
                   command=lambda row=row, col=col: btn_click(btns[row][col])).grid(row=row+1, column=col,
                                                                                    sticky="nsew", padx=1, pady=1)

root.mainloop()

from tkinter import Tk, ttk, Entry, INSERT, END, W, E
from math import sqrt

root = Tk()
root.title('VermaksCalculator')
style = ttk.Style()
style.configure('TButton', background='#fff', foreground='navy', font='Arial 12')

button_list = [
    '%', '√', 'x²', 'C',
    '(', ')', '1/x', '/',
    '7', '8', '9', '*', 
    '4', '5' , '6', '-',
    '1', '2', '3', '+',
    '+/-', '0', '.', '=' 
]

for i, btn in enumerate(button_list):
    def com(k=btn):
        return calculation(k)
    ttk.Button(root, text=btn, command=com).grid(row=i // 4+1, column=i % 4, ipady=10)

calculator = Entry(
    root, font='Arial 28', insertontime=0,
    relief='solid', state='normal', fg='navy')
calculator.focus()
calculator.grid(row=0, column=0, columnspan=4, sticky=W + E, ipady=4)


def calculation(key):
    calculator.focus()
    if key == '=':
        try:
            result = eval(calculator.get())
            calculator.insert(END, f'={result}')
        except (ZeroDivisionError, SyntaxError, IndexError, ValueError, NameError):
            calculator.delete(0, END)
            calculator.insert(0, 'error')
    elif key == 'C':
        calculator.delete(0, END)
    elif key == '%':
        result = eval(calculator.get()) / 100
        calculator.delete(0, END)
        calculator.insert(0, str(result))
    elif key == '√':
        result = sqrt(float(calculator.get()))
        num = calculator.get()
        calculator.delete(0, END)
        calculator.insert(0, f'√{num}={result}')
    elif key == 'x²':
        result = float(calculator.get()) ** 2
        num = calculator.get()
        calculator.delete(0, END)
        calculator.insert(0, f'{num}²={result}')
    elif key == '1/x':
        result = 1 /  float(calculator.get())
        num = calculator.get()
        calculator.delete(0, END)
        calculator.insert(0, f'1/{num}={result}')
    elif key == '+/-':
        if calculator.get()[0] == '-':
            calculator.delete(0)
        elif calculator.get()[0] == '+':
            calculator.delete(0)
            calculator.insert(0, '-')
        else:
            calculator.insert(0, '-')
    else:
        calculator.insert(END, key)

def sym(e):
    e_key = e.keysym
    if e_key == 'Escape':
        root.destroy()
    elif e_key == 'Return':
        calculation('=')
    elif ('=' in calculator.get() or 'error' in calculator.get()):
        calculator.delete(0, END)
    elif e_key not in button_list and len(e_key) <= 2:
        calculator.delete(0, END)


root.bind('<Key>', sym)
root.mainloop()

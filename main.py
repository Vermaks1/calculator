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
    button = ttk.Button(root, text=btn, command=com)
    button.grid(row=i // 4+1, column=i % 4, ipady=10)

calculator = Entry(
    root, font='Arial 28', insertontime=0,
    relief='solid', state='normal', fg='navy')
calculator.focus()
calculator.grid(row=0, column=0, columnspan=4, sticky=W + E, ipady=4)


def calculation(key):
    try:
        result = eval(calculator.get())
    except (ZeroDivisionError, SyntaxError, IndexError, ValueError, NameError):
        calculator.delete(0, END)
        calculator.insert(0, 'error')


def sym(e):
    e_key = e.keysym
    if e_key == 'Escape':
        root.destroy()


root.bind('<Key>', sym)
root.mainloop()

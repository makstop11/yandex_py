import tkinter as tk

win = tk.Tk()
win.geometry('240x270')
win.resizable(width=0, height=0)
win['bg'] = '#273746'
win.title('MagicCalc v1.0')

calc = tk.Entry(
    win,
    justify=tk.RIGHT,
    font=('Arial', 15),
    width=15
)
calc.insert(0, '0')
calc.grid(
    row=0,
    column=0,
    columnspan=4,
    stick='we',
    padx=5
)


def add_digit(digit):
    value = calc.get()
    if value[0] == '0':
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0, value + digit)


def add_operation(operation):
    value = calc.get()
    if value[-1] in '-+*/':
        value = value[:-1]
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)


def calculate():
    value = calc.get()
    if value[-1] in '+-/*':
        value = value + value[:-1]
    calc.delete(0, tk.END)
    calc.insert(0, eval(value))


def clear():
    calc.delete(0, tk.END)
    calc.insert(0, "0")


def make_digit_button(digit):
    return tk.Button(
        text=digit,
        bd=5,
        font=('Arial', 13),
        command=lambda: add_digit(digit)
    )


def make_operation_button(operation):
    return tk.Button(
        text=operation,
        bd=5, font=('Arial', 13),
        fg='red',
        command=lambda: add_operation(operation)
    )


def make_calc_button(operation):
    return tk.Button(
        text=operation,
        bd=5,
        font=('Arial', 13),
        fg='red',
        command=calculate
    )


def make_clear_button(operation):
    return tk.Button(
        text=operation,
        bd=5,
        font=('Arial', 13),
        fg='red',
        command=clear
    )


if __name__ == '__main__':
    make_digit_button('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)
    make_digit_button('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)
    make_digit_button('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
    make_digit_button('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
    make_digit_button('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
    make_digit_button('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
    make_digit_button('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
    make_digit_button('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
    make_digit_button('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)
    make_digit_button('0').grid(row=4, column=0, stick='wens', padx=5, pady=5)

    make_operation_button('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
    make_operation_button('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
    make_operation_button('/').grid(row=3, column=3, stick='wens', padx=5, pady=5)
    make_operation_button('*').grid(row=4, column=3, stick='wens', padx=5, pady=5)

    make_calc_button('=').grid(row=4, column=2, stick='wens', padx=5, pady=5)
    make_clear_button('c').grid(row=4, column=1, stick='wens', padx=5, pady=5)

    win.grid_columnconfigure(0, minsize=60)
    win.grid_columnconfigure(1, minsize=60)
    win.grid_columnconfigure(2, minsize=60)
    win.grid_columnconfigure(3, minsize=60)

    win.grid_rowconfigure(1, minsize=60)
    win.grid_rowconfigure(2, minsize=60)
    win.grid_rowconfigure(3, minsize=60)
    win.grid_rowconfigure(4, minsize=60)

    win.mainloop()

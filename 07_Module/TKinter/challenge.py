from tkinter import *
from functools import *


def callback(key: str):
    if key.isnumeric():
        appendnum(key)
    else:
        button_func[key]()


def appendnum(num: str):
    global num_buffer_1, num_buffer_2
    if act_buffer == '':
        num_buffer_1 += num
        # resultBox.replace('1.0', END, num_buffer_1)
        resultLabel.config(text=num_buffer_1)
    else:
        num_buffer_2 += num
        # resultBox.replace('1.0', END, num_buffer_2)
        resultLabel.config(text=num_buffer_2)


def clear_buffers():
    global num_buffer_1, num_buffer_2, act_buffer
    num_buffer_1 = ''
    num_buffer_2 = ''
    act_buffer = ''


def clear():
    clear_buffers()
    # resultBox.delete('1.0', END)
    resultLabel.config(text='')


def plus():
    global act_buffer, num_buffer_2
    if num_buffer_2 != '':
        equals()
    act_buffer = '+'


def minus():
    global act_buffer, num_buffer_2
    if num_buffer_2 != '':
        equals()
    act_buffer = '-'


def multiple():
    global act_buffer, num_buffer_2
    if num_buffer_2 != '':
        equals()
    act_buffer = '*'


def divide():
    global act_buffer, num_buffer_2
    if num_buffer_2 != '':
        equals()
    act_buffer = '/'


def equals():
    global num_buffer_1, num_buffer_2, act_buffer
    ans = 0.0
    if act_buffer == '+':
        ans = float(num_buffer_1) + float(num_buffer_2)
    elif act_buffer == '-':
        ans = float(num_buffer_1) - float(num_buffer_2)
    elif act_buffer == '*':
        ans = float(num_buffer_1) * float(num_buffer_2)
    elif act_buffer == '/':
        ans = float(num_buffer_1) / float(num_buffer_2)

    if ans.is_integer():
        ans = int(ans)
    ans_str = str(ans)

    resultLabel.config(text=ans_str)
    # resultBox.replace('1.0', END, ans_str)
    clear_buffers()
    num_buffer_1 = ans_str


num_buffer_1 = ''
num_buffer_2 = ''
act_buffer = ''

mainWindow = Tk()
mainWindow.title('計算機')
mainWindow.geometry('240x240')
mainWindow.minsize(width=240, height=240)
mainWindow.maxsize(width=480, height=480)
mainWindow['padx'] = 8
mainWindow['pady'] = 8

for c in range(4):
    mainWindow.columnconfigure(index=c, weight=1)
for r in range(6):
    mainWindow.rowconfigure(index=r, weight=1)

resultLabel = Label(
    mainWindow, bg='white', anchor='e',
    border=1, relief='sunken', font=('Arial', 25))
resultLabel.grid(column=0, row=0, sticky='news', columnspan=4)

# resultBox = Text(mainWindow, height=1)
# resultBox.grid(column=0, row=0, sticky='news', columnspan=4)

dict_button = {
    'C': (0, 1, 1), 'CE': (1, 1, 1),
    '7': (0, 2, 1), '8': (1, 2, 1), '9': (2, 2, 1), '+': (3, 2, 1),
    '4': (0, 3, 1), '5': (1, 3, 1), '6': (2, 3, 1), '-': (3, 3, 1),
    '1': (0, 4, 1), '2': (1, 4, 1), '3': (2, 4, 1), '*': (3, 4, 1),
    '0': (0, 5, 1), '=': (1, 5, 2), '/': (3, 5, 1),
}

button_func = {
    'c': clear, 'ce': clear, '+': plus, '-': minus,
    '*': multiple, '=': equals, '/': divide,
}

for key, button in dict_button.items():
    _col, _row, _span = button
    b = Button(mainWindow, text=key, name=str(key).casefold())
    b.grid(column=_col, row=_row, columnspan=_span,
           sticky='news', padx=2, pady=2)
    b.config(
        command=partial(callback, b.winfo_name())
    )

mainWindow.mainloop()

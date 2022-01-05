from tkinter import *


def ButtonCommand(output: Text, value: str):
    output.replace('1.0', END, value)


var_buffer = ''


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

resultBox = Text(mainWindow)
resultBox.grid(column=0, row=0, sticky='new', columnspan=4)

dict_button = {
    'C':(0,1,1), 'CE':(1,1,1),
    '7':(0,2,1), '8':(1,2,1), '9':(2,2,1), '+':(3,2,1),
    '4':(0,3,1), '5':(1,3,1), '6':(2,3,1), '-':(3,3,1),
    '1':(0,4,1), '2':(1,4,1), '3':(2,4,1), '*':(3,4,1),
    '0':(0,5,1), '=':(1,5,2), '/':(3,5,1), 
}

for key, button in dict_button.items():
    _col, _row, _span = button
    b = Button(mainWindow, text=key)
    b.grid(column=_col, row=_row, columnspan=_span, sticky='news',)
    
mainWindow.mainloop()
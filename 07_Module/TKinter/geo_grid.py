import tkinter
from tkinter.constants import BOTH

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry("640x480")

label = tkinter.Label(mainWindow, text="Hello there")
label.pack(side='top')

canvas = tkinter.Canvas(mainWindow, relief='raised',
                        borderwidth='2', background='green')
canvas.pack(side='left', fill=BOTH, expand=False)

button1 = tkinter.Button(mainWindow, text='Button 1')
button2 = tkinter.Button(mainWindow, text='Button 2')
button3 = tkinter.Button(mainWindow, text='Button 3')
button1.pack(side='right', anchor='n')  # n for North
button2.pack(side='right', anchor='s')  # s for South
button3.pack(side='right', anchor='e')  # e for East

mainWindow.mainloop()

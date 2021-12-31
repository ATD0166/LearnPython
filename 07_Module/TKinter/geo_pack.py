from tkinter import *
import tkinter
from typing import TYPE_CHECKING

mainWindow = tkinter.Tk()
mainWindow.title('My Window')
mainWindow.geometry('800x600')
mainWindow.config(bg='black')

tk_label = tkinter.Label(mainWindow, text='This is a label', fg='white', bg='green')
tk_label.grid(column=0, row=0)

frame_1 = tkinter.Frame(mainWindow, bg='pink')
frame_1.grid(column=1, row=1)

frame_2 = tkinter.Frame(mainWindow, bg='cyan')
frame_2.grid(column=2, row=1)

button_1 = tkinter.Button(frame_1, text='button 1')
button_1.grid(column=0, row= 3)

button_2 = tkinter.Button(frame_1, text='button 2')
button_2.grid(column=1, row= 4)

button_3 = tkinter.Button(frame_2, text='button 3')
button_3.grid(column=1, row= 1)

button_3 = tkinter.Button(frame_2, text='button 4')
button_3.grid(column=0, row= 2)



mainWindow.mainloop()

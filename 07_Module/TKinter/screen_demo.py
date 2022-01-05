from tkinter import *
import os
import tkinter

mainWindow = Tk()
mainWindow.title("Grid Demo")
mainWindow.geometry("640x480")
mainWindow.config(padx=10, pady=10)

# Label
label = Label(mainWindow, text="Tkinter grid demo")
label.grid(column=0, row=0, columnspan=3)

# Grid layout
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=3)
mainWindow.columnconfigure(3, weight=3)
mainWindow.columnconfigure(4, weight=3)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=1)
mainWindow.rowconfigure(4, weight=3)

# List box
fileList = Listbox(mainWindow)
fileList.grid(column=0, row=1, sticky='news', rowspan=2)
fileList.config(border=2, relief='sunken')
for zone in os.listdir('/Windows/System32'):
    fileList.insert('end', zone)

# Scroll bar of the list box
listScroll = Scrollbar(mainWindow, orient=VERTICAL, command=fileList.yview)
listScroll.grid(column=1, row=1, sticky='nsw', rowspan=2)
fileList.config(yscrollcommand=listScroll.set)

# Label frame
optionFrame = LabelFrame(mainWindow, text='File Details')
optionFrame.grid(column=3, row=1, sticky='ne')

# Radio buttoms
rbValue = IntVar()
rbValue.set(1)

radioButtom_1 = Radiobutton(
    optionFrame, text='Filename', value=1, variable=rbValue,
    command=lambda:
        tBox.replace('1.0', END, f"rbValue = {rbValue.get()}"))
radioButtom_2 = Radiobutton(
    optionFrame, text='Path', value=2, variable=rbValue,
    command=lambda:
        tBox.replace('1.0', END, f"rbValue = {rbValue.get()}"))
radioButtom_3 = Radiobutton(
    optionFrame, text='Timestamp', value=3, variable=rbValue,
    command=lambda:
        tBox.replace('1.0', END, f"rbValue = {rbValue.get()}"))
radioButtom_1.grid(row=0, column=0, sticky='w')
radioButtom_2.grid(row=1, column=0, sticky='w')
radioButtom_3.grid(row=2, column=0, sticky='w')

# Text box
tBox = Text(mainWindow, width=20, height=3)
tBox.grid(column=3, row=2, sticky='se')

mainWindow.mainloop()

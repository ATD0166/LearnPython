from tkinter import *
import os
import platform

mainWindow = Tk()
mainWindow.title("Grid Demo")
mainWindow.geometry("640x480")
mainWindow['padx'] = 20
mainWindow['pady'] = 10

# Label
label = Label(mainWindow, text="Tkinter grid demo")
label.grid(column=0, row=0, columnspan=3)

# Grid layout
mainWindow.columnconfigure(0, weight=100)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=100)
mainWindow.columnconfigure(3, weight=3)
mainWindow.columnconfigure(4, weight=3)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=1)
mainWindow.rowconfigure(4, weight=2)

# List box
fileList = Listbox(mainWindow)
fileList.grid(column=0, row=1, sticky='news', rowspan=2)
fileList.config(border=2, relief='sunken')

folder_path = ''
if platform.system() != 'Windows':
    folder_path = '/usr/bin'
else:
    folder_path = '/Windows/System32'

for zone in os.listdir(folder_path):
    fileList.insert('end', zone)

# Scroll bar of the list box
listScroll = Scrollbar(mainWindow, orient=VERTICAL, command=fileList.yview)
listScroll.grid(column=1, row=1, sticky='nsw', rowspan=2)
fileList.config(yscrollcommand=listScroll.set)

# Text box
tBox = Text(mainWindow, width=20, height=3)
tBox.grid(column=2, row=3, sticky='sew')

# Label frame
optionFrame = LabelFrame(mainWindow, text='File Details')
optionFrame.grid(column=2, row=1, sticky='ne')

# Radio buttons
rbValue = IntVar()
rbValue.set(1)

radioButton_1 = Radiobutton(
    optionFrame, text='Filename', value=1, variable=rbValue,
    command=lambda:
        tBox.replace('1.0', END, f"rbValue = {rbValue.get()}"))
radioButton_2 = Radiobutton(
    optionFrame, text='Path', value=2, variable=rbValue,
    command=lambda:
        tBox.replace('1.0', END, f"rbValue = {rbValue.get()}"))
radioButton_3 = Radiobutton(
    optionFrame, text='Timestamp', value=3, variable=rbValue,
    command=lambda:
        tBox.replace('1.0', END, f"rbValue = {rbValue.get()}"))
radioButton_1.grid(row=0, column=0, sticky='w')
radioButton_2.grid(row=1, column=0, sticky='w')
radioButton_3.grid(row=2, column=0, sticky='w')

# Widgets to display the result
resultFrame = Frame(mainWindow)
resultFrame.grid(column=2, row=2, sticky='sw')
resultLabel = Label(resultFrame, text="Result")
resultLabel.grid(column=0, row=0, sticky='sw')
result = Entry(resultFrame)
result.grid(column=0, row=1, sticky='sw')

# Time spinner
timeFrame = LabelFrame(mainWindow, text='Time')
timeFrame.grid(column=0, row=3, sticky='new')
timeFrame['padx'] = 36

hourSpinner = Spinbox(timeFrame, width=2, from_=0, to=23)
minuteSpinner = Spinbox(timeFrame, width=2, from_=0, to=59)
secSpinner = Spinbox(timeFrame, width=2, from_=0, to=59)
hourSpinner.grid(column=0, row=0)
Label(timeFrame, text=':').grid(column=1, row=0)
minuteSpinner.grid(column=2, row=0)
Label(timeFrame, text=':').grid(column=3, row=0)
secSpinner.grid(column=4, row=0)

# Date spinner
dateFrame = Frame(mainWindow)
dateFrame.grid(column=0, row=4, sticky='new', )

Label(dateFrame, text='Day').grid(column=0, row=0)
Label(dateFrame, text='Month').grid(column=1, row=0)
Label(dateFrame, text='Year').grid(column=2, row=0)

daySpinner = Spinbox(dateFrame, width=4, from_=1, to=31)
monSpinner = Spinbox(dateFrame, width=4, values=(
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
yearSpinner = Spinbox(dateFrame, width=4, from_=1970, to=2099)
daySpinner.grid(column=0, row=1)
monSpinner.grid(column=1, row=1)
yearSpinner.grid(column=2, row=1)

# Buttons
button_ok = Button(mainWindow, text='OK')
button_cancel = Button(mainWindow, text='Cancel', command=mainWindow.destroy)
button_ok.grid(column=3, row=4, sticky='e')
button_cancel.grid(column=4, row=4, sticky='w')

mainWindow.mainloop()

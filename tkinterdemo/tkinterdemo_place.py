try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter  # The module 'Tkinter' is not found if you are using P3.

""" Learning about the simple geometric function place witch is absolute position.
    then we are using grid instead of pack.  
"""


# print(tkinter.TkVersion)
# print(tkinter.TclVersion)

#  tkinter._test()  A test window just to see if all is working.

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")  # the name of the window.
mainWindow.geometry('640x480-8-200')  # size and placement

label = tkinter.Label(mainWindow, text="Hello TkI World")  # text in the window.
label.grid(row=0, column=0)

leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row=1, column=1)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
# canvas.pack(side='right', fill=tkinter.BOTH, expand=True)
# Above, the problem with not expanding. try with X and Y and with and without expand
canvas.grid(row=1, column=0)

rightFrame = tkinter.Frame(mainWindow)
rightFrame.grid(row=1, column=2, sticky='n')
button1 = tkinter.Button(rightFrame, text='button1')
button2 = tkinter.Button(rightFrame, text='button2')
button3 = tkinter.Button(rightFrame, text='button3')
button1.grid(row=1, column=1)
button2.grid(row=2, column=1)
button3.grid(row=3, column=1)

# configure the columns
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.grid_columnconfigure(2, weight=1)

leftFrame.config(relief='sunken', borderwidth=1)
rightFrame.config(relief='sunken', borderwidth=1)
leftFrame.grid(sticky='ns')
rightFrame.grid(sticky='new')

rightFrame.columnconfigure(0, weight=1)
button2.grid(sticky='w')

mainWindow.mainloop()  # Must call this to handle all events and pass
# the control over to tkinter.
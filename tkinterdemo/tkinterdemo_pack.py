try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter  # The module 'Tkinter' is not found if you are using P3.

""" Learning about the simple geometric manager pack(), is good for
simple placement of graphic. 
"""


# print(tkinter.TkVersion)
# print(tkinter.TclVersion)

#  tkinter._test()  A test window just to see if all is working.

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")  # the name of the window.
mainWindow.geometry('640x480+8+400')  # size and placement

label = tkinter.Label(mainWindow, text="Hello TkI World")  # text in the window.
label.pack(side='top') # adding to the window.

leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
# canvas.pack(side='right', fill=tkinter.BOTH, expand=True)
# Above, the problem with not expanding. try with X and Y and with and without expand

canvas.pack(side='left', anchor='n')

rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side='right', anchor='n', expand=True)

button1 = tkinter.Button(rightFrame, text='button1')
button2 = tkinter.Button(rightFrame, text='button2')
button3 = tkinter.Button(rightFrame, text='button3')

button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')

mainWindow.mainloop()  # Must call this to handle all events and pass
# the control over to tkinter.




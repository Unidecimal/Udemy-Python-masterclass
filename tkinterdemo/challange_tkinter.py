# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.

try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter  # The module 'Tkinter' is not found if you are using P3.


def a_testfunktion(num, hum):
    print()


buttons = ["C", "CE",
           "7", "8", "9", "+",
           "4", "5", "6", "-",
           "1", "2", "3", "*",
           "0", "=", "/",
           ]

mainWindow = tkinter.Tk()
mainWindow.minsize(185, 185)
mainWindow.title("Calculator")  # the name of the window.
mainWindow.geometry('320x320')  # size and placement
mainWindow['padx'] = 8

#configure rows an columns

mainWindow.columnconfigure(0, weight=0)
mainWindow.columnconfigure(1, weight=0)
mainWindow.columnconfigure(2, weight=0)
mainWindow.columnconfigure(3, weight=0)
mainWindow.rowconfigure(0, weight=0)
mainWindow.rowconfigure(1, weight=0)
mainWindow.rowconfigure(2, weight=0)
mainWindow.rowconfigure(3, weight=0)
mainWindow.rowconfigure(4, weight=0)
mainWindow.rowconfigure(5, weight=0)

# result display
result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, columnspan=4, sticky='nesw')

# dashboard
colIndex = 0
for index, button in enumerate(buttons):
    mButton = tkinter.Button(mainWindow, text=str(button))
    if index <= 1:
        mButton.grid(row=1, column=colIndex, sticky='nesw')
        colIndex += 1
    elif 1 < index < 6:
        if index == 2:
            colIndex = 0
        mButton.grid(row=2, column=colIndex, sticky='nesw')
        colIndex += 1
    elif 5 < index < 10:
        if index == 6:
            colIndex = 0
        mButton.grid(row=3, column=colIndex, sticky='nesw')
        colIndex += 1
    elif 9 < index < 14:
        if index == 10:
            colIndex = 0
        mButton.grid(row=4, column=colIndex, sticky='nesw')
        colIndex += 1
    elif 13 < index < 17:
        if index == 14:
            colIndex = 0
        if index == 15:
            mButton.grid(row=5, column=colIndex, columnspan=2, sticky='nesw')
            colIndex += 2
        else:
            mButton.grid(row=5, column=colIndex, sticky='nesw')
            colIndex += 1
        print(index, button)



mainWindow.mainloop()

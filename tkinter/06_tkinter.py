from Tkinter import *

root = Tk()


def printName(event):
    print("Hello my name is Bucky")


button_1 = Button(root, text="Print Message")
# <Button-1> is an event that means "clicked left mouse button"
button_1.bind("<Button-1>", printName) # (event, function)
button_1.pack()

root.mainloop()

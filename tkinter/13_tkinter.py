from Tkinter import *

root = Tk()

canvas = Canvas(root, width=200, height=100)
canvas.pack()

blackLine = canvas.create_line(0, 0, 200, 50) # (X_start, Y_start, X_end, Y_end)
redLine = canvas.create_line(0, 100, 200, 50, fill="red")
greenBox = canvas.create_rectangle(25, 25, 130, 60, fill="green")

# canvas.delete(redLine)
# canvas.delete(ALL)

root.mainloop()

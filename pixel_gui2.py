from tkinter import *
import pixel as px
from PIL import ImageTk

root = Tk()

# Left frame and contents
def run_pixelate():
    rank = int(entry.get())
    global image
    image.photo = ImageTk.PhotoImage(px.pixelate(px.im, rank))
    image.configure(image=image.photo)
    image.pack()

def reset():
    global image
    image.photo = ImageTk.PhotoImage(px.og)
    px.im = px.og.copy()
    image.configure(image=image.photo)
    image.pack()

leftFrame = Frame(root)
leftFrame.pack(side=LEFT)

label1 = Label(leftFrame, text='Rank')
label1.grid(row=0, column=0)
entry = Entry(leftFrame)
entry.grid(row=0, column=1)
button1 = Button(leftFrame, text='Pixelate', command=run_pixelate)
button1.grid(row=1, columnspan=2)
button2 = Button(leftFrame, text='Reset', command=reset)
button2.grid(row=2, columnspan=2)


# Right frame and contents
rightFrame = Frame(root)
rightFrame.pack(side=LEFT)

photo = ImageTk.PhotoImage(px.og)
image = Label(rightFrame, image=photo)
image.photo = photo
image.pack()

root.mainloop()

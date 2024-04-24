import tkinter
from tkinter import *
from tkinter import PhotoImage
from PIL import Image
from subprocess import call

root=tkinter.Tk()
root.title("head page")
root.geometry("1024x1024")
root.resizable(width=False,height=True)
def next():
    root.destroy()
    call(['python', 'choosingwindow.py'])

image_path = PhotoImage(file="C:\\Users\\HP\\Downloads\\WhatsApp Image 2024-03-14 at 20.32.45_d5da845f.png")

bg_image = tkinter.Label(root,image=image_path)
bg_image.pack()

next_btn = Button(root, text="NEXT", fg="white",bg="Blue", font="times 15 bold", command=next)
next_btn.place(x=800,y=700)

root.mainloop()
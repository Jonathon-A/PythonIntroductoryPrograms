#Import tkinter constants and functions
from tkinter import *
#Create window
Window = Tk()
#Setting window attrivuts
Window.title("GUI Example")
Window.geometry("350x200")
def clicked1():
    res = "Hello" + " Bob"
    lbl.configure(text = res)
def clicked2():
    res = "Hello" + " Tom"
    lbl.configure(text = res)
def clicked3():
    res = "Hello" + " Jess"
    lbl.configure(text = res)
#Creating label component
lbl = Label(Window, text = "Hello")
#creating buttons and binding the event handler to function
btn_1 = Button(Window,text = "Bob",command = clicked1)
btn_2 = Button(Window,text = "Tom",command = clicked2)
btn_3 = Button(Window,text = "Jess",command = clicked3)
#componenet positions
btn_1.grid(column=0,row=0)
btn_2.grid(column=0,row=1)
btn_3.grid(column=0,row=2)
lbl.grid(column=1,row=1)




Window.mainloop()

#frame = Frame(tk, relief=RIDGE, borderwidth=2)
#frame.pack(fill=BOTH,expand=1)
#label = Label(frame, text="Hello, World")
#label.pack(fill=X, expand=1)
#button = Button(frame,text="Exit",command=tk.destroy)
#button.pack(side=BOTTOM)

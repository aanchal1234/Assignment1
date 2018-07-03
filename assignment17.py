
# #1Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.
# import tkinter
# from tkinter import *
# import sys
# root=Tk()
# root.title("my app")
# root.geometry("250x250")
# root.minsize(200,200)
# root.maxsize(300,300)
# l=Label(root,text="Hello World!",width=25,font='20')
# l.pack()
# b=Button(root,text="Hello World!",width=25,command='exit')
# b.pack()
# root.mainloop()

#2 Write a python program to in the same interface as above and create a action when the button is click it will display some text.
import tkinter
from tkinter import *
def  display():
    l = Label(root,text="world",width=25,bg="pink")
    l.place(x=60,y=120)
root=Tk()
root.title("myapp")
root.geometry("250x250")
root.minsize(200,200)
root.maxsize(300,300)
l = Label(root,text="Hello",width=25,bg="blue")
l.place(x=30, y=100)
b=Button(text="show",width=25,command=display)
b.place(x=20,y=100)
root.mainloop()

# #3. Create a frame using tkinter with any label text and two buttons.One to exit and other to change the label to some other text.
# import  tkinter
# from tkinter import *
# root=Tk()
# f1=Frame(root)
# def show():
#     l2=Label(f1,text="new text",fg='blue')
#     l2.grid(row=3,column=1)
#
# l1=Label(f1,text="hello world!",fg='red')
# l1.grid(row=1,column=1)
# root.geometry("250x250")
# b=Button(f1,text="exit",bg="blue",width=20,command=exit)
# b.grid(row=0,column=0)
# b=Button(f1,text="label",bg="blue",width=20,command=show)
# b.grid(row=2,column=0)
# f1.pack()
# root.mainloop()

# #4 Write a python program using tkinter interface to take an input in the GUI program and print it
# import  tkinter
# from tkinter import *
# def show():
#     t1=entry.get()
#     l2=Label(root,text=1,fg='blue')
#     l2.place(x=60,y=70)
# root=Tk()
# root.title("myapp")
# root.geometry("250x250")
# root.minsize(200,200)
# root.maxsize(300,300)
# root.resizable(false,false)
# b=Button(f1,text="exit",bg="blue",width=20,command=exit)
# b.place(x=40,y=140)
# b=Button(f1,text="show",bg="blue",width=20,command=show)
# b.place(x=50,y=100)
root.mainloop()
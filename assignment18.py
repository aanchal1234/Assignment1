#1Create a dict with name and mobile number.Define a GUI interface using tkinter and pack the label and create a scrollbar to scroll the list of keys in the dictionary.
# import tkinter
# from tkinter import *
# root=Tk()
# s=Scrollbar(root)
# s.pack(side=RIGHT,fill=Y)
# d={"sakshi":8950678120,"pankil":8950126798,"mansi":7404612895}
# a=Listbox(root,yscrollcommand=s.set)
# for i in d:
#     a.insert(ACTIVE,i)
# a.pack(fill=BOTH)
# Scrollbar(a,orient="vertical")
# s.config(command=a.yview())
# root.mainloop()

#2In the same tkinter file as created above, create a function to insert items into the dictionary.
import tkinter
from tkinter import *
d={"sakshi":8950678120,"pankil":8950126798,"mansi":7404612895}
root=Tk()
root.geometry("250x250")

root.resizable(True,False)

sc=Scrollbar(root)
sc.pack(side=RIGHT,fill=Y)
mylist=Listbox(root,yscrollcommand=sc.get)
for  i in d:
    mylist.insert(END,i)
entry=Entry(root,width=25)
entry.place(x=40,y=10)
entry1=Entry(root,width=25)
entry1.place(x=40,y=30)
mylist.place(x=60,y=100)
Scrollbar(mylist,orient="vertical")
sc.config(command=mylist.yview)
def show():
    k=entry.get()
    v=entry.get()
    d[k]=v
    mylist.insert(END,k)
btn=Button(root,text="insert",command=show)
btn.place(x=90,y=50)
root.mainloop()




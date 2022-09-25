from tkinter import *
from backend import *

window = Tk()

l1 = Label(window,text="Title")
l1.grid(row=0,column=0)

l3 = Label(window,text="Publisher")
l3.grid(row=0,column=2)

l4 = Label(window,text="Author")
l4.grid(row=1,column=0)

l6 = Label(window,text="Pages")
l6.grid(row=1,column=2)

title_text = StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

published_text = StringVar()
e2=Entry(window,textvariable=published_text)
e2.grid(row=0,column=3)

author_text = StringVar()
e4=Entry(window,textvariable=author_text)
e4.grid(row=1,column=1)

genre_text = StringVar()
e5=Entry(window,textvariable=genre_text)
e5.grid(row=1,column=3)

list1 = Listbox(window,height=20,width=50)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1 = Button(window,text="View all",width=12)
b1.grid(row=2,column=3)

b2 = Button(window,text="Search book",width=12)
b2.grid(row=3,column=3)

b3 = Button(window,text="Close",width=12)
b3.grid(row=4,column=3)

window.mainloop()
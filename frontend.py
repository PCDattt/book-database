from tkinter import *
from backend import *

def get_selected_row(event):
    global book
    index = list1.curselection()[0]
    book = list1.get(index)
    e1.delete(0,END)
    e1.insert(END,book[0])
    e2.delete(0,END)
    e2.insert(END,book[3])
    e3.delete(0,END)
    e3.insert(END,book[2])
    e4.delete(0,END)
    e4.insert(END,book[4])
    e5.delete(0,END)
    e5.insert(END,book[1])

def view_all_command():
    list1.delete(0,END)
    for row in view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in search(title_text.get(),publisher_text.get(),pages_text.get(),author_text.get(),rating_text.get()):
        list1.insert(END,row)


window = Tk()

window.wm_title("Book Database")

l1 = Label(window,text="Title")
l1.grid(row=0,column=0)

l2 = Label(window,text="Publisher")
l2.grid(row=0,column=2)

l3 = Label(window,text="Rating")
l3.grid(row=0,column=4)

l4 = Label(window,text="Author")
l4.grid(row=1,column=0)

l5 = Label(window,text="Pages")
l5.grid(row=1,column=2)

title_text = StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

publisher_text = StringVar()
e2=Entry(window,textvariable=publisher_text)
e2.grid(row=0,column=3)

rating_text = StringVar()
e3=Entry(window,textvariable=rating_text)
e3.grid(row=0,column=5)

author_text = StringVar()
e4=Entry(window,textvariable=author_text)
e4.grid(row=1,column=1)

pages_text = StringVar()
e5=Entry(window,textvariable=pages_text)
e5.grid(row=1,column=3)

list1 = Listbox(window,height=20,width=90)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1 = Button(window,text="View all",width=12,command = view_all_command)
b1.grid(row=2,column=3)

b2 = Button(window,text="Search book",width=12, command = search_command)
b2.grid(row=3,column=3)

b3 = Button(window,text="Close",width=12,command=window.destroy)
b3.grid(row=4,column=3)

window.mainloop()
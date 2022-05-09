from tkinter import*
top=Tk()
top['bg']="#51E1DC"
top.geometry("300x250")
lbl=Label(top,text="My Favourite Fruits",bg="Orange",width="200").pack()
listbox=Listbox(top)
listbox.insert(1,"Apple")
listbox.insert(2,"Orange")
listbox.insert(3,"Cherry")
listbox.insert(4,"Mango")
#delete selected item from list
#by default it deletes from top if not selected any item
btn=Button(top,text="delete",bg="orange",command=lambda listbox=listbox:listbox.delete(ANCHOR))
listbox.pack(pady=5)
btn.pack()
top.mainloop()

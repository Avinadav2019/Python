from tkinter import*
top=Tk()
#window dimension
top.geometry("300x150")
top['bg']="#51E1DC"
Label(top,text="My Favourite Fruits").pack()
listbox=Listbox(top,height="20")
listbox.insert(1,"Apple")
listbox.insert(2,"Orange")
listbox.insert(3,"Cherry")
listbox.insert(4,"Mango")
listbox.pack()
top.mainloop()

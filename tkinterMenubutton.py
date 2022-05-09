from tkinter import*
top=Tk()
top.geometry("200x160")
top['bg']="#51E1DC"
mb=Menubutton(top,text="Programming",bg="navy",fg="white",relief=GROOVE)
mb.grid()
mb.menu=Menu(mb)
mb["menu"]=mb.menu
mb.menu.add_checkbutton(label="C")
mb.menu.add_checkbutton(label="C++")
mb.menu.add_checkbutton(label="JAVA")
mb.menu.add_checkbutton(label="PYTHON")
mb.pack()
top.mainloop()

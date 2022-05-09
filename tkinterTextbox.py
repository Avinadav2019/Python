from tkinter import*
top=Tk()
#window dimension
top.geometry("330x150")
top['bg']="#51E1DC"
label=Label(top,text="Are you a Christian?",).place(x=50,y=50)
#creating text box
ent=Entry(top).place(x=190,y=50)
top.mainloop()

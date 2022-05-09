from tkinter import*
top=Tk()
#window dimension
top.geometry("300x180")
top['bg']="#51E1DC"
rdb=IntVar()
Label(top,text="Select Gender").pack()
Radiobutton(top,text="Male",variable=rdb,value=1).place(x=50,y=20)
Radiobutton(top,text="Female",variable=rdb,value=2).place(x=50,y=50)
Radiobutton(top,text="Other",variable=rdb,value=3).place(x=50,y=80)
top.mainloop()

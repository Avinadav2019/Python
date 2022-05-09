from tkinter import messagebox
from tkinter import*
top=Tk()
#window dimension
top.geometry("300x180")
top['bg']="#51E1DC"
def fun():
    str=""
    if chk1.get()==1:
        str=str+"Apple"
    if chk2.get()==1:
        str=str+"Orange"
    if chk3.get()==1:
        str=str+"Cherry"
    messagebox.showinfo("Result",str+" selected")
chk1=IntVar()
chk2=IntVar()
chk3=IntVar()
#creating check boxes
Checkbutton(top,text="Apple",variable=chk1,width="15",onvalue=1,offvalue=0).place(x=10,y=20)
Checkbutton(top,text="Orange",variable=chk1,width="15",onvalue=1,offvalue=0).place(x=10,y=50)
Checkbutton(top,text="Cherry",variable=chk1,width="15",onvalue=1,offvalue=0).place(x=10,y=80)
Button(top,text="CLICK",command=fun).place(x=15,y=110)
top.mainloop()            

from tkinter import messagebox
from tkinter import*
top=Tk()
#window dimension
top.geometry("300x180")
top['bg']="#51E1DC"
#defining function
def add():
    f=firstNum.get()
    s=secondNum.get()
    messagebox.showinfo("Sum",(f+s))
#declaring variables
firstNum=IntVar()
secondNum=IntVar()
#creating labels
Label(top,text="First Number",width="13").place(x=50,y=50)
Label(top,text="Second Number",width="13").place(x=50,y=90)
#creating text boxes
Entry(top,textvariable=firstNum).place(x=150,y=50)
Entry(top,textvariable=secondNum).place(x=150,y=90)
#creating button
Button(top,text="Add",width="5",bg="Purple",command=add).place(x=100,y=120)
top.mainloop()

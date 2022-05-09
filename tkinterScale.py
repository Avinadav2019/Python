from tkinter import*
top=Tk()
top.geometry("200x150")
top['bg']="#51E1DC"
#defining function
def myFun():
    sel="Selected Value="+str(var.get())
    label.config(text=sel)
var=IntVar()
#creating scale
Scale(top,variable=var,from_=10,to=20, orient=HORIZONTAL).pack(anchor=CENTER,pady=5)
#creating button
Button(top,text="Value",command=myFun).pack()
label=Label(top)
label.pack()
top.mainloop()

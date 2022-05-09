from tkinter import*
top=Tk()
top.geometry("200x150")
top['bg']="#51E1DC"
c=Canvas(top,bg="#51E1DC",height="200",width=200)
#create arc
arc=c.create_arc((50,20,150,120),start=315,extent=270,fill="yellow")
#create_rectangle
arc=c.create_rectangle((50,120,150,140),fill="red")
c.pack()
top.mainloop()

from tkinter import messagebox
from tkinter import*
top=Tk()
top.geometry("200x250")
top['bg']="#51E1DC"
def info():
    messagebox.showinfo("Info","Info")
def warning():
    messagebox.showwarning("Warning","Warning")
def error():
    messagebox.showerror("Error","Error")
def askq():
    messagebox.askquestion("Question","Are you okay?")
def askyes():
    messagebox.askyesno("Application","Do you want to install?")
def askok():
    messagebox.askokcancel("Storage","Allow storage")
def askretry():
    messagebox.askretrycancel("Failed","Try again!")
Button(top,text="ShowInfo",command=info).pack(pady=2)
Button(top,text="ShowWarning",command=warning).pack(pady=2)
Button(top,text="ShowError",command=error).pack(pady=2)
Button(top,text="AskQuestion",command=askq).pack(pady=2)
Button(top,text="AskOkCancel",command=askok).pack(pady=2)
Button(top,text="AskYesNo",command=askyes).pack(pady=2)
Button(top,text="AskRetry",command=askretry).pack(pady=2)
top.mainloop()

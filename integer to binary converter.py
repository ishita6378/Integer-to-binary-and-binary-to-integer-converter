from tkinter import *
root= Tk()
root.geometry("780x340")
f1 = Frame(root,bg="light green",borderwidth=10)
f1.grid()
L1 = Label(f1,text="INTEGER TO BINARY \n AND \n BINARY TO INTEGER\nCONVERTER",fg = "Black",bg="light green",font="Times 30 bold")
L1.grid(row=0,column=0)
L2 = Label(f1,text="INTEGER NUMBER",fg = "Black",bg="light green",font="bold")
L2.grid(row=1,column=0)
L3 = Label(f1,text="BINARY NUMBER",fg = "Black",bg="light green",font="bold")
L3.grid(row=2,column=0)
a = StringVar()
s1 = Entry(f1,textvariable=a)
s1.grid(row=1, column=1,ipadx=100)
b = StringVar()
s2 = Entry(f1,textvariable=b)
s2.grid(row=2, column=1,ipadx=100)
def IntegerTobinary(n):
    n=int(n)
    p = bin(n).replace("0b","")
    return p
def binaryToInteger(n):
    q = int(n,2)
    return q
def button1():
    x = IntegerTobinary(s1.get())
    b.set(x)
    s1.update()
    s2.update()
def button2():
    y = binaryToInteger(s2.get())
    a.set(y)
    s1.update()
    s2.update()
b1=Button(f1,text="INTERGER TO BINARY",command=button1,bg="black",fg="light green",font="bold")
b1.grid(row=4,column=1)
b1=Button(f1,text="BINARY TO INTERGER",command=button2,bg="black",fg="light green",font="bold")
b1.grid(row=5,column=1)
root.mainloop()

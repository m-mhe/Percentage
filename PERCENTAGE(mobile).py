from logging import root
from tkinter import *
import math


root = Tk()
root.title("_PERCENTAGE_")
root.geometry('820x300')
#root.resizable(height=False, width=False)
root.configure(background="#1E1F35")





def percentage():
    total = float(TotalNumD1.get())
    number = float(NumD1.get())
    percent = (100/total)*number
    output = "%0.2f" %(percent)
    PercentageD1.delete(0, END)
    PercentageD1.insert(0, (output+"%"))

def number():
    total = float(TotalNumD2.get())
    percent = float(PercentageD2.get())
    num = (total/100)*percent
    output = "%0.2f" %(num)
    NumD2.delete(0, END)
    NumD2.insert(0, output)

def totalnumber():
    percent = float(PercentageD3.get())
    number = float(NumD3.get())
    total = (number/percent)*100
    output = "%0.2f" %(total)
    TotalNumD3.delete(0, END)
    TotalNumD3.insert(0, output)




#1
TotalNum1 = Label(root, text="Total Number", bg="#8BB158", fg="#1E1F35", height=2).grid(row=0, column=0, padx=(25, 15), pady=(400, 10))
TotalNumD1 = Entry(root, bg="#1E1F35", fg="#EAC394", justify=CENTER, width=11)
TotalNumD1.grid(row=1, column=0, padx=(25, 15), ipady=6, pady=(0, 10))

Num1 = Label(root, text="Number", bg="#8BB158", fg="#1E1F35", height=2, width=11).grid(row=2, column=0, padx=(25, 15), pady=(0, 10))
NumD1 = Entry(root, bg="#1E1F35", fg="#EAC394", justify=CENTER, width=11)
NumD1.grid(row=3, column=0, padx=(25, 15), ipady=6, pady=(0, 10))

Percentage1 = Button(root, text="Percentage", bg="#8BB158", fg="#1E1F35", height=2, width=7, bd=0, command=percentage).grid(row=4, column=0, padx=(25, 15), pady=(0, 10))
PercentageD1 = Entry(root, bg="#1E1F35", fg="#EAC394", justify=CENTER, width=11)
PercentageD1.grid(row=5, column=0, padx=(25, 15), ipady=6, pady=(0, 0))


#2
TotalNum2 = Label(root, text="Total Number", bg="#8BB158", fg="#1E1F35", height=2).grid(row=0, column=1, padx=(0, 15), pady=(400, 10))
TotalNumD2 = Entry(root, bg="#1E1F35", fg="#EAC394", justify=CENTER, width=11)
TotalNumD2.grid(row=1, column=1, padx=(0, 15), ipady=6, pady=(0, 10))

Percentage2 = Label(root, text="Percentage", bg="#8BB158", fg="#1E1F35", height=2, width=11).grid(row=2, column=1, padx=(0, 15), pady=(0, 10))
PercentageD2 = Entry(root, bg="#1E1F35", fg="#EAC394", justify=CENTER, width=11)
PercentageD2.grid(row=3, column=1, padx=(0, 15), ipady=6, pady=(0, 10))

Num2 = Button(root, text="Number", bg="#8BB158", fg="#1E1F35", height=2, width =7, command=number, bd=0).grid(row=4, column=1, padx=(0, 15), pady=(0, 10))
NumD2 = Entry(root, bg="#1E1F35", fg="#EAC394", justify=CENTER, width=11)
NumD2.grid(row=5, column=1, padx=(0, 15), ipady=6, pady=(0, 0))


#3
Percentage3 = Label(root, text="Percentage", bg="#8BB158", fg="#1E1F35", height=2, width=11, bd=0).grid(row=0, column=2, pady=(400, 10))
PercentageD3 = Entry(root, bg="#1E1F35", fg="#EAC394", justify=CENTER, width=11)
PercentageD3.grid(row=1, column=2, ipady=6, pady=(0, 10))

Num3 = Label(root, text="Number", bg="#8BB158", fg="#1E1F35", height=2, width=11, bd=0).grid(row=2, column=2, pady=(0, 10))
NumD3 = Entry(root, bg="#1E1F35", fg="#EAC394", justify=CENTER, width=11)
NumD3.grid(row=3, column=2, ipady=6, pady=(0, 10))

TotalNum3 = Button(root, text="Total Number", bg="#8BB158", fg="#1E1F35", height=2, bd=0, command=totalnumber, width=7).grid(row=4, column=2, pady=(0, 10))
TotalNumD3 = Entry(root, bg="#1E1F35", fg="#EAC394", justify=CENTER, width=11)
TotalNumD3.grid(row=5, column=2, ipady=6, pady=(0, 0))

footer = Button(root, text="©MMHE", bg="#2B2B2B", fg="#6CE890", font=('bold', 4), height=0, width=1, bd=0)
footer.grid(row=5, column=3, columnspan=3, pady=(0,0), padx=(15,0))
footer2 = Button(root, text="©MMHE", bg="#2B2B2B", fg="#6CE890", font=('bold', 4), height=0, width=1, bd=0)
footer2.grid(row=4, column=3, columnspan=3, pady=(0,0), padx=(15,0))
footer3 = Button(root, text="©MMHE", bg="#2B2B2B", fg="#6CE890", font=('bold', 4), height=0, width=1, bd=0)
footer3.grid(row=3, column=3, columnspan=3, pady=(0,0), padx=(15,0))
footer4 = Button(root, text="©MMHE", bg="#2B2B2B", fg="#6CE890", font=('bold', 4), height=0, width=1, bd=0)
footer4.grid(row=2, column=3, columnspan=3, pady=(0,0), padx=(15,0))
footer5 = Button(root, text="©MMHE", bg="#2B2B2B", fg="#6CE890", font=('bold', 4), height=0, width=1, bd=0)
footer5.grid(row=1, column=3, columnspan=3, pady=(0,0), padx=(15,0))
footer6 = Button(root, text="©MMHE", bg="#2B2B2B", fg="#6CE890", font=('bold', 4), height=0, width=1, bd=0)
footer6.grid(row=0, column=3, columnspan=3, pady=(400,0), padx=(15,0))



root.mainloop()
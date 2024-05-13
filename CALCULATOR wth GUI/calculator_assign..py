from tkinter import * 
from math import *
root = Tk()
root.maxsize(width=280, height=350)
root.title("AnkitCodex's Calculator")
def value1():
    t1.insert("end",1)
def value2():
    t1.insert("end",2)
def value3():
    t1.insert("end",3)
def value4():
    t1.insert("end",4)
def value5():
    t1.insert("end",5)
def value6():
    t1.insert("end",6)
def value7():
    t1.insert("end",7)
def value8():
    t1.insert("end",8)
def value9():
    t1.insert("end",9)
def value0():
    t1.insert("end",0)

def sum1():
    t1.insert("end","+")
def sub1():
    t1.insert("end","-")
def mul1():
    t1.insert("end","*")
def div1():
    t1.insert("end","/")
def dot1():
    t1.insert("end",".")
def clear1():
    t1.delete(0,"end")
def exit1():
    root.destroy()
def eval1():
    z=eval(t1.get())
    float(z)
    t1.delete(0,"end")
    t1.insert("end",z)

topframe=Frame(root)
topframe.pack()
bottom=Frame(root)
bottom.pack(side=BOTTOM)
t1=Entry(topframe,font="times 20" ,bg="lightblue",justify="right")
t1.pack()

but11=Button(bottom,text=1,font="times 25" ,bg="darkgrey" ,command=value1)
but11.grid(row=2 , column=0,sticky=W+N+E+S)
but22=Button(bottom,text=2,font="times 25 ",bg="darkgrey" ,command=value2)
but22.grid(row=2 , column=1,sticky=W+N+E+S)
but33=Button(bottom,text=3,font="times 25 ",bg="darkgrey" ,command=value3)
but33.grid(row=2 , column=2,sticky=W+N+E+S)
but44=Button(bottom,text=4,font="times 25 ",bg="darkgrey" ,command=value4)
but44.grid(row=1 , column=0,sticky=W+N+E+S)
but55=Button(bottom,text=5,font="times 25 ",bg="darkgrey" ,command=value5)
but55.grid(row=1, column=1,sticky=W+N+E+S)
but66=Button(bottom,text=6,font="times 25 ",bg="darkgrey" ,command=value6)
but66.grid(row=1 , column=2,sticky=W+N+E+S)
but77=Button(bottom,text=7,font="times 25 ",bg="darkgrey" ,command=value7)
but77.grid(row=0 , column=0,sticky=W+N+E+S)
but88=Button(bottom,text=8,font="times 25 ",bg="darkgrey" ,command=value8)
but88.grid(row=0 , column=1,sticky=W+N+E+S)
but99=Button(bottom,text=9,font="times 25 ",bg="darkgrey" ,command=value9)
but99.grid(row=0 , column=2,sticky=W+N+E+S)
but00=Button(bottom,text=0,font="times 24 ",bg="darkgrey" ,command=value0)
but00.grid(row=3 , column=1,sticky=W+N+E+S)

but1=Button(bottom,text="+",font="times 24 ",bg="skyblue",command=sum1)
but1.grid(row=0,column=3,columnspan=1,rowspan=1,sticky=W+N+E+S)
but2=Button(bottom,text="-",font="times 24 ",bg="skyblue",command=sub1)
but2.grid(row=2,column=3,columnspan=1,rowspan=1,sticky=W+N+E+S)
but3=Button(bottom,text="*",font="times 24 ",bg="skyblue",command=mul1)
but3.grid(row=1,column=3,columnspan=1,rowspan=1,sticky=W+N+E+S)
but4=Button(bottom,text="/",font="times 24 ",bg="skyblue",command=div1)
but4.grid(row=3,column=3,columnspan=1,rowspan=1,sticky=W+N+E+S)
butdot=Button(bottom,text=".",font="times 24 ",bg="darkgrey",command=dot1)
butdot.grid(row=3,column=0,sticky=W+N+E+S)
but5=Button(bottom,text="C",font="times 18 ",bg="skyblue",command=clear1)
but5.grid(row=4,column=2,columnspan=2,sticky=W+N+E+S)
but6=Button(bottom,text="EXIT",bg="red",font="times 18 ",command=exit1)
but6.grid(row=4,column=0,columnspan=2,sticky=W+N+E+S)
but7=Button(bottom,text="=",font="times 24 ",bg="darkgrey",command=eval1)
but7.grid(row=3,column=2,sticky=W+N+E+S)

root.mainloop()

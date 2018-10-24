from tkinter import *
import random
from tkinter import messagebox

awailable=[]

root=Tk()
#=============================================frames
top=Frame(root,width=400,height=400,relief=SUNKEN)
top.pack()

bottom=Frame(root,width=400,height=400,relief=SUNKEN )
bottom.pack()
#====================================================
b00=Button(top,font=('arial',20,'bold'),text='',bd=10,height = 1, width = 2)
b00.grid(row=1,column=0)

b01=Button(top,font=('arial',20,'bold'),text='',bd=10,height = 1, width = 2)
b01.grid(row=1,column=1)

b02=Button(top,font=('arial',20,'bold'),text='',bd=10,height = 1, width = 2)
b02.grid(row=1,column=2)

b03=Button(top,font=('arial',20,'bold'),text='',bd=10,height = 1, width = 2)
b03.grid(row=1,column=3)

b10=Button(top,font=('arial',20,'bold'),text='',bd=10,height = 1, width = 2)
b10.grid(row=2,column=0)

b11=Button(top,font=('arial',20,'bold'),text='',bd=10,padx=18,pady=10,height = 1, width = 2)
b11.grid(row=2,column=1)

b12=Button(top,font=('arial',20,'bold'),text='',bd=10,padx=18,pady=10,height = 1, width = 2)
b12.grid(row=2,column=2)

b13=Button(top,font=('arial',20,'bold'),text='',bd=10,padx=18,pady=10,height = 1, width = 2)
b13.grid(row=2,column=3)

b20=Button(top,font=('arial',20,'bold'),text='',bd=10,padx=18,pady=10,height = 1, width = 2)
b20.grid(row=3,column=0)

b21=Button(top,font=('arial',20,'bold'),text='',bd=10,padx=18,pady=10,height = 1, width = 2)
b21.grid(row=3,column=1)

b22=Button(top,font=('arial',20,'bold'),text='',bd=10,padx=18,pady=10,height = 1, width = 2)
b22.grid(row=3,column=2)

b23=Button(top,font=('arial',20,'bold'),text='',bd=10,padx=18,pady=10,height = 1, width = 2)
b23.grid(row=3,column=3)

b30=Button(top,font=('arial',20,'bold'),text='',bd=10,padx=18,pady=10,height = 1, width = 2)
b30.grid(row=4,column=0)

b31=Button(top,font=('arial',20,'bold'),text='',bd=10,padx=18,pady=10,height = 1, width = 2)
b31.grid(row=4,column=1)

b32=Button(top,font=('arial',20,'bold'),text='',bd=10,padx=18,pady=10,height = 1, width = 2)
b32.grid(row=4,column=2)

b33=Button(top,font=('arial',20,'bold'),text='',bd=10,padx=18,pady=10,height = 1, width = 2)
b33.grid(row=4,column=3)
#================================================insert
def awail():
    try:
        awailable = []
        if b00.cget('text') == '':
            awailable.append(0)

        if b01.cget('text') == '':
            awailable.append(1)
        if b02.cget('text') == '':
            awailable.append(2)
        if b03.cget('text') == '':
            awailable.append(3)
        if b10.cget('text') == '':
            awailable.append(10)

        if b11.cget('text') == '':
            awailable.append(11)
        if b12.cget('text') == '':
            awailable.append(12)
        if b13.cget('text') == '':
            awailable.append(13)
        if b20.cget('text') == '':
            awailable.append(20)
        if b21.cget('text') == '':
            awailable.append(21)
        if b22.cget('text') == '':
            awailable.append(22)
        if b23.cget('text') == '':
            awailable.append(23)
        if b30.cget('text') == '':
            awailable.append(30)
        if b31.cget('text') == '':
            awailable.append(31)
        if b32.cget('text') == '':
            awailable.append(32)
        if b33.cget('text') == '':
            awailable.append(33)

        return awailable
    except:
        pass


def insert():
    i=[4,2]
    return random.choice(i)

def choisetoinsert():
    awail()
    try:

     if len(awailable)==0:

        r = random.choice(awail())
        if r == 0:
            b00.config(text=insert())
        if r == 1:
            b01.config(text=insert())
        if r == 2:
            b02.config(text=insert())
        if r == 3:
            b03.config(text=insert())
        if r == 10:
            b10.config(text=insert())
        if r == 11:
            b11.config(text=insert())
        if r == 12:
            b12.config(text=insert())
        if r == 13:
            b13.config(text=insert())
        if r == 20:
            b20.config(text=insert())
        if r == 21:
            b21.config(text=insert())

        if r == 22:
            b22.config(text=insert())
        if r == 23:
            b23.config(text=insert())
        if r == 30:
            b30.config(text=insert())
        if r == 31:
            b31.config(text=insert())
        if r == 32:
            b32.config(text=insert())
        if r == 33:
            b33.config(text=insert())
     else:
         messagebox.showinfo("game over", "game over")
    except:
        messagebox.showinfo("game over", "game over")

def em(list):
    for i in range(len(list)):
        list[i]=list[i+1]

def row1(a,b,c,d):
        lst1 = [a, b, c, d]
        for i in range(len(lst1)):
            try:
                if lst1[i].cget('text') == '' and lst1[i + 1].cget('text') == '' and lst1[i + 2].cget('text') == '':
                    lst1[i].config(text=lst1[i + 3].cget('text'))
                    lst1[i + 3].config(text='')
                    row1(a,b,c,d)
                    continue

                if lst1[i].cget('text') == '' and lst1[i + 1].cget('text') == '':
                    lst1[i].config(text=lst1[i + 2].cget('text'))
                    lst1[i + 2].config(text='')
                    row1(a,b,c,d)
                    continue

                if lst1[i].cget('text') == '':
                    lst1[i].config(text=lst1[i + 1].cget('text'))
                    lst1[i + 1].config(text='')
                    row1(a,b,c,d)
                    continue

                if lst1[i].cget('text') == lst1[i + 1].cget('text'):
                    lst1[i].config(text=lst1[i].cget('text') + lst1[i + 1].cget('text'))
                    lst1[i + 1].config(text='')
                    row1(a,b,c,d)
                    continue

                if lst1[i + 1].cget('text') == '' and lst1[i].cget('text') == lst1[i + 2].cget('text'):
                    lst1[i].config(text=lst1[i].cget('text') + lst1[i + 2].cget('text'))
                    lst1[i + 1].config(text='')
                    lst1[i + 2].config(text='')
                    row1(a,b,c,d)
                    continue
            except:
                pass


def up():
    row1(b00, b10, b20, b30)
    row1(b01, b11, b21, b31)
    row1(b02, b12, b22, b32)
    row1(b03, b13, b23, b33)
    choisetoinsert()


def down():
    row1(b30, b20, b10, b00)
    row1(b31, b21, b11, b01)
    row1(b32, b22, b12, b02)
    row1(b33, b23, b13, b03)
    choisetoinsert()





def righ():
    row1(b03, b02, b01, b00)
    row1(b13, b12, b11, b10)
    row1(b23, b22, b21, b20)
    row1(b33, b32, b31, b30)
    choisetoinsert()


def lef():
    row1(b00, b01, b02, b03)
    row1(b10, b11, b12, b13)
    row1(b20, b21, b22, b23)
    row1(b30, b31, b32, b33)
    choisetoinsert()




upButton=Button(bottom,text='^',font=('arial',20,'bold'),bd=10,height = 1, width = 2,command=up)
upButton.grid(row=5,column=3)

rButton=Button(bottom,text='>',font=('arial',20,'bold'),bd=10,height = 1, width = 2,command=righ)
rButton.grid(row=7,column=4)

lButton=Button(bottom,text='<',font=('arial',20,'bold'),bd=10,height = 1, width = 2,command=lef)
lButton.grid(row=7,column=2)

dButton=Button(bottom,text='v',font=('arial',20,'bold'),bd=10,height = 1, width = 2,command=down)
dButton.grid(row=9,column=3)
root.mainloop()



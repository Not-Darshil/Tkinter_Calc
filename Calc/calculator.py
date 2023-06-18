import tkinter
from tkinter import *
win=Tk(className='Calculator By Darshil')
win.geometry("415x550")
win.configure(bg="black")

def button(x1,y1,x2,y2,txt,do):
    button=Button(win,text=str(txt),height=(y2-y1),width=(x2-x1),command=lambda:fx())
    button.place(x=x1,y=y1)
    return

def change_output(res):
    lab.config(text="%d"%res)
    

def button_press(a):
##    res=res*10+x
    print("hi")
    
    
def fx(x,y):
    button_press(x)
    change_output(y)
        
    
#input and output display
res=222
lab=Label(win,text="22",height=7,width=53,bg="white")
lab.place(x=20,y=20)
#1st line
##button(320,145,330,150,"+",add())
##button(120,145,130,150,"2",add())
##button(220,145,230,150,"3",add())
b1=Button(win,text="1",height=5,width=10,command=lambda:fx("Hello", 123))
b1.place(x=20,y=145)
b2=Button(win,text="2",height=5,width=10,command=change_output)
b2.place(x=120,y=145)
b3=Button(win,text="3",height=5,width=10,command=change_output)
b3.place(x=220,y=145)
b_add=Button(win,text="+",height=5,width=10,command=change_output)
b_add.place(x=320,y=145)


###2nd line
##button(20,245,30,250,"4",add()) 
##button(120,245,130,250,"5",add())
##button(220,245,230,250,"6",add())
##button(320,245,330,250,"-",add())
b4=Button(win,text="4",height=5,width=10,command=change_output)
b4.place(x=20,y=245)
b5=Button(win,text="5",height=5,width=10,command=change_output)
b5.place(x=120,y=245)
b6=Button(win,text="6",height=5,width=10,command=change_output)
b6.place(x=220,y=245)
b_sub=Button(win,text="-",height=5,width=10,command=change_output)
b_sub.place(x=320,y=245)



###3rd line
b7=Button(win,text="7",height=5,width=10,command=change_output)
b7.place(x=20,y=345)
b8=Button(win,text="8",height=5,width=10,command=change_output)
b8.place(x=120,y=345)
b9=Button(win,text="9",height=5,width=10,command=change_output)
b9.place(x=220,y=345)
b_div=Button(win,text="/",height=5,width=10,command=change_output)
b_div.place(x=320,y=345)
##button(20,345,30,350,"7",add()) 
##button(120,345,130,350,"8",add())
##button(220,345,230,350,"9",add())
##button(320,345,330,350,"/",add())


###4th line
b_del=Button(win,text="Delete",height=5,width=10,command=change_output)
b_del.place(x=20,y=445)
b0=Button(win,text="0",height=5,width=10,command=change_output)
b0.place(x=120,y=445)
b_equ=Button(win,text="=",height=5,width=10,command=change_output)
b_equ.place(x=220,y=445)
b_mul=Button(win,text="*",height=5,width=10,command=change_output)
b_mul.place(x=320,y=445)
##button(20,445,30,450,"Delete",add()) 
##button(120,445,130,450,"0",add())
##button(220,445,230,450,"=",change_output)
##button(320,445,330,450,"*",add())






win.mainloop()

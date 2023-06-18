import tkinter
from tkinter import *
win = Tk(className='Calculator By Darshil')
win.geometry("415x550")
win.configure(bg="black")
out_put = ""
lst = [""]
k = []


def button(x1, y1, x2, y2, txt):
    button = Button(win, text=str(txt), height=(y2-y1),width=(x2-x1), command=lambda: fx(txt))
    button.place(x=x1, y=y1)
    return


def change_output(x=out_put):
    lab.config(text=x)
    return


def button_press(a):
    global out_put
    global lst
    global k
    print("lst:",lst)
    if a in "1234567890+-*/":
        if a in "1234567890":
            out_put = out_put + a
            change_output(out_put)
        else:
            lst.append(out_put)
            change_output(a)
            out_put =" "
    if a in "+-*/":
        c=0
        for i in range(-1,-len(lst)-1,-1):
            if lst[i] in range(9**999) :#list check krni pdegi
                c=0
            if lst[i] in "+-*/":
                if c==0:
                    lst.append(a)   
                    c=1
                
    

    elif a == "=":
        st = ""
        for k in lst:
            st = st+str(k)
        print(st)
        lst = []
        lst.append(str(eval(st)))
        out_put = str(eval(st))
        change_output(out_put)
        out_put = ""
        
    elif a == "Delete":
        out_put = out_put[:-1:1]
        change_output(out_put)
    elif a == "All\nClear":
        out_put = ""
        lst = []
        change_output(out_put)

def fx(x):
    change_output()
    button_press(x)

# input and output display
lab = Label(win, text="", height=7, width=53, bg="white")
lab.place(x=20, y=20)
# 1st line
button(20, 145, 30, 150, "1")
button(120, 145, 130, 150, "2")
button(220, 145, 230, 150, "3")
button(320, 145, 330, 150, "+")
# 2nd line
button(20, 245, 30, 250, "4")
button(120, 245, 130, 250, "5")
button(220, 245, 230, 250, "6")
button(320, 245, 330, 250, "-")
# 3rd line
button(20, 345, 30, 350, "7")
button(120, 345, 130, 350, "8")
button(220, 345, 230, 350, "9")
button(320, 345, 330, 350, "/")
# 4th line
button(20, 445, 25, 450, "Delete")
button(75, 445, 79, 450, "All\nClear")
button(120, 445, 130, 450, "0")
button(220, 445, 230, 450, "=")
button(320, 445, 330, 450, "*")
win.mainloop()


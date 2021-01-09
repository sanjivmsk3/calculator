from tkinter import *

expression = ""

def clear():
    global expression
    expression = ""
    diaplayValue.set(expression)

def equal():
    global expression
    expression = str(eval(expression))
    diaplayValue.set(expression)

def btnClick(num):
    global expression
    expression += str(num)
    diaplayValue.set(expression)

win = Tk()
win.title("snv calculator")
win.geometry("325x205")
win.configure(background='light green')

diaplayValue = StringVar()
diaplayValue.set('0')

display = Entry(win,width=50,justify=RIGHT, textvariable=diaplayValue)
display.grid(row=0,columnspan=4,pady=10,padx=10)

# 1st row

btn1 = Button(win,width=10,height=2,fg='black',bg='white',text='1',command=lambda:btnClick(1))
btn1.grid(row=1,column=0)

btn2 = Button(win,width=10,height=2,fg='black',bg='white',text='2',command=lambda:btnClick(2))
btn2.grid(row=1,column=1)

btn3 = Button(win,width=10,height=2,fg='black',bg='white',text='3',command=lambda:btnClick(3))
btn3.grid(row=1,column=2)

btn4 = Button(win,width=10,height=2,fg='black',bg='white',text='+',command=lambda:btnClick('+'))
btn4.grid(row=1,column=3)

# 2nd row

btn21 = Button(win,width=10,height=2,fg='black',bg='white',text='4',command=lambda:btnClick(4))
btn21.grid(row=2,column=0)

btn22 = Button(win,width=10,height=2,fg='black',bg='white',text='5',command=lambda:btnClick(5))
btn22.grid(row=2,column=1)

btn23 = Button(win,width=10,height=2,fg='black',bg='white',text='6',command=lambda:btnClick(6))
btn23.grid(row=2,column=2)

btn24 = Button(win,width=10,height=2,fg='black',bg='white',text='/',command=lambda:btnClick('/'))
btn24.grid(row=2,column=3)

# 3rd row

btn31 = Button(win,width=10,height=2,fg='black',bg='white',text='7',command=lambda:btnClick(7))
btn31.grid(row=3,column=0)

btn32 = Button(win,width=10,height=2,fg='black',bg='white',text='8',command=lambda:btnClick(8))
btn32.grid(row=3,column=1)

btn33 = Button(win,width=10,height=2,fg='black',bg='white',text='9',command=lambda:btnClick(9))
btn33.grid(row=3,column=2)

btn34 = Button(win,width=10,height=2,fg='black',bg='white',text='-',command=lambda:btnClick('-'))
btn34.grid(row=3,column=3)

# 4th row

btn41 = Button(win,width=10,height=2,fg='black',bg='white',text='0',command=lambda:btnClick(0))
btn41.grid(row=4,column=0)

btn42 = Button(win,width=10,height=2,fg='black',bg='white',text='=',command=equal)
btn42.grid(row=4,column=1)

btn43 = Button(win,width=10,height=2,fg='white',bg='red',text='C',command=clear)
btn43.grid(row=4,column=2)

btn44 = Button(win,width=10,height=2,fg='black',bg='white',text='*',command=lambda:btnClick('*'))
btn44.grid(row=4,column=3)


win.mainloop()

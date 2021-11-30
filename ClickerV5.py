import tkinter
import tkinter as tk
from tkinter import BooleanVar, Button, ttk
from tkinter.constants import TRUE



Number = 0
OrginColor = 'gray'
ClickedUp = False
ClickedDown = False
ButtonBool = False

def Add():
    global OrginColor
    global Number
    global ClickedUp 
    global ClickedDown
    ClickedUp = True
    ClickedDown = False
    Number +=1 
    numberLabel['text'] = Number
    if Number > 0:
        root['background'] = 'green'
        OrginColor = 'green'
    elif Number < 0:
        root['background'] = 'red'
        OrginColor = 'red'
    else:
        root['background'] = 'gray'
        OrginColor = 'gray'

def Sub():
    global OrginColor
    global Number
    global ClickedDown
    global ClickedUp
    ClickedUp = False
    ClickedDown = True

    Number -= 1
    numberLabel['text'] = Number
    if Number > 0:
        root['background'] = 'green'
        OrginColor = 'green'
    elif Number < 0:
        root['background'] = 'red'
        OrginColor = 'red'
    else:
        root['background'] = 'gray'
        OrginColor = 'gray'

def LabelClick(event):
    global ClickedDown
    global ClickedUp
    global Number

    if ClickedUp:
        Number = Number * 3
    else:
        Number = round((Number/3),2)
    numberLabel['text'] = Number

def KeyAdd(event):
    global OrginColor
    global Number
    global ClickedUp 
    global ClickedDown
    ClickedUp = True
    ClickedDown = False
    Number +=1 
    numberLabel['text'] = Number
    if Number > 0:
        root['background'] = 'green'
        OrginColor = 'green'
    elif Number < 0:
        root['background'] = 'red'
        OrginColor = 'red'
    else:
        root['background'] = 'gray'
        OrginColor = 'gray'

def KeySub(event):
    global OrginColor
    global Number
    global ClickedDown
    global ClickedUp
    ClickedUp = False
    ClickedDown = True

    Number -= 1
    numberLabel['text'] = Number
    if Number > 0:
        root['background'] = 'green'
        OrginColor = 'green'
    elif Number < 0:
        root['background'] = 'red'
        OrginColor = 'red'
    else:
        root['background'] = 'gray'
        OrginColor = 'gray'


def ColorChange(event):
    global OrginColor
    root["background"] = 'yellow'
def ColorChange1(event):
    root["background"] = OrginColor

def Clicker():
    global ButtonBool
    if ButtonBool:
        ButtonBool = False
    else:
        ButtonBool = True

def Clicker2():
    if ButtonBool:
        if ClickedUp:
            Add()
        else:
            Sub()
    root.after(5000,Clicker2)
    
root = tkinter.Tk()
root.configure(bg='gray')
root.geometry('300x350')

buttonUp = tkinter.Button(root)
buttonUp.configure(text= 'Up', command=Add)
buttonUp.pack(padx=50,pady=50,expand=True)

buttonDown = tkinter.Button(root)
buttonDown.configure(text= 'Down', command=Sub)
buttonDown.pack(padx=50,pady=50,expand=True)

numberLabel = tkinter.Label(root, text = Number)
numberLabel.pack(ipadx=20,ipady=20)

root.bind("<Enter>",ColorChange)
root.bind("<Leave>",ColorChange1)
root.bind("+",KeyAdd)
root.bind("-",KeySub)
root.bind("<Up>",KeyAdd)
root.bind("<Down>",KeySub)
root.bind("<space>",LabelClick)
numberLabel.bind("<Double-Button-1>",LabelClick)

agreement = tkinter.StringVar()

ttk.Checkbutton(root,
                text='After 5 Seconds Repeat',
                command= lambda:[Clicker(),Clicker2()],
                variable=agreement,
                onvalue='True',
                offvalue='False').pack(ipadx=5, ipady= 5)
                

root.mainloop()
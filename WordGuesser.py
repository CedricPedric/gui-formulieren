import tkinter
from tkinter.messagebox import showinfo
import string


alphabet = list(string.ascii_lowercase)

def ButtonCommand():
    bool,word = wordSetup()
    if bool:
        createSpinboxes(word)


def wordSetup():
    word = textbox.get()
    if len(list(word)) > 7:
        tkinter.messagebox.showinfo("Wow Pop Up",'Vul SVP een woord in wat minder dan 7 letters is.')
        return False,list(word)
    else:
        textbox.destroy()
        button.destroy()
        return True,list(word)


def createSpinboxes(word:list):
    listofboxes = []
    placex = 25
    for z in range(len(word)):
        spinbox = tkinter.Spinbox(
            window,
            value= alphabet,
            width=2
        )
        spinbox.pack(pady=2,padx=2)
        spinbox.place(x=placex,y=35,anchor='center')
        listofboxes.append(spinbox)
        placex += 25

    button2 = tkinter.Button(text='Guess',command=None)
    button2.pack()
    button2.place(y=100,x=75)
    None

window = tkinter.Tk()
window.geometry('200x200')

textbox = tkinter.Entry()
textbox.place(x=40,y=20)

button = tkinter.Button(text='Stel het woord in',command=ButtonCommand)
button.pack()
button.place(y=100,x=50)

window.mainloop()

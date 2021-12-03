import tkinter
import random
from tkinter.messagebox import showinfo, showerror
import string

lives = 0
alphabet = list(string.ascii_lowercase)

def ButtonCommand():
    bool,word = wordSetup()
    if bool:
        createSpinBox_Button(word)


def wordSetup():
    word = textbox.get()
    if len(list(word)) > 7 or len(list(word)) < 4:
        tkinter.messagebox.showinfo("Wow Pop Up",'Vul SVP een woord in wat tussen de 4 en 7 letters is.')
        return False,list(word)
    else:
        textbox.destroy()
        button.destroy()
        textlabel.destroy()
        window.geometry('200x200')
        return True,list(word)


def createSpinBox_Button(word:list):
    global lives
    listofboxes = []
    placex = 25
    stringvar = tkinter.StringVar()
    for z in range(len(word)):
        spinbox = tkinter.Spinbox(
            window,
            value= alphabet,
            textvariable= stringvar,
            width=2
        )
        spinbox.pack(pady=2,padx=2)
        spinbox.place(x=placex,y=35,anchor='center')
        listofboxes.append(spinbox)
        placex += 25
    
    randomnumber = random.randint(1,len(word))
    number = len(word)
    for z in range(len(word)):
        if number == randomnumber:
            randomString = tkinter.StringVar()
            randomString.set(word[z])
            listofboxes[z].config(textvariable= randomString)
        else:
            randomString = tkinter.StringVar()
            randomString.set(random.choice(alphabet))
            listofboxes[z].config(textvariable= randomString)
        number -= 1
        None
    
    lives = len(word) * len(word)
    liveslabel = tkinter.Label(text=f"{lives}:Lives")
    liveslabel.pack(ipadx=50,ipady=50)
    liveslabel.place(y=150,x=75)

    button2 = tkinter.Button(text='Guess',command= lambda: [WordChecker(word,listofboxes,liveslabel),LivesCheck()])
    button2.pack()
    button2.place(y=100,x=75)
    None

def WordChecker(word:list,listofboxes:list,liveslabel):
    global lives
    amountsame = 0
    amountwrong = 0
    for z in range(len(word)):
        letter = listofboxes[z].get()
        if word[z].lower() == letter.lower():
            amountsame += 1
        else:
            amountwrong += 1
    if amountsame == len(word):
        tkinter.messagebox.showinfo("Wow Pop Up",'Wow you won!')
        window.destroy()
    else:
        lives -= (amountwrong * 2) 
        liveslabel['text'] = f"{lives}:Lives"
    

    None

def LivesCheck():
    global lives
    if lives <= 0:
        tkinter.messagebox.showerror("",'You lost!  :(',)
        window.destroy()

window = tkinter.Tk()
window.geometry('255x200')

textbox = tkinter.Entry()
textbox.place(x=40,y=20)

textlabel = tkinter.Label(text="Het woord moet tussen die 4 en 7 letters zitten.")
textlabel.pack(ipadx=20,ipady=20)
textlabel.place(y=50,x=0)

button = tkinter.Button(text='Stel het woord in',command=ButtonCommand)
button.pack()
button.place(y=100,x=50)
window.mainloop()

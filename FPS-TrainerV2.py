import tkinter
import random
from tkinter.messagebox import askyesno

a = 21
score = 0
randomPlaceX= ['25','50','75','100','125','150','175','200','225',]
randomPlaceY = ['25','50','75','100','125','150','175','200','225','250']

def randomLabel():
    global a
    if a  <= 0:
        return confirm()
    randomNumber = random.randint(1,8)
    if randomNumber == 1:
        clickOnce()
    elif randomNumber == 2:
        clickTwice()
    elif randomNumber == 3:
        clickTrice()
    elif randomNumber == 4:
        clickW()
    elif randomNumber == 5:
        clickA()
    elif randomNumber == 6:
        clickS()
    elif randomNumber == 7:
        clickD()
    elif randomNumber == 8:
        clickSpace()






    
def MouseScorePlus(event):
    global score
    score += 2
    scoreLabel['text'] = f"Score: {score}"
def KeyBoardPlus(event):
    global score
    score += 1
    scoreLabel['text'] = f"Score: {score}"

def CountDown():
    global a
    global score
    if a  <= 0:
        return
    a -= 1
    stringVar.set(f"Time remaining {a}")
    timeLabel.after(1000,CountDown)

def clickOnce():
    global randomPlaceX
    global randomPlaceY
    randomX = random.choice(randomPlaceX)
    randomY = random.choice(randomPlaceY)
    clickWindow = tkinter.Label(window)
    clickWindow.config(text = 'Click Once!')
    clickWindow.config(bg='red',fg='black')
    clickWindow.pack(ipady= '20',ipadx='20')
    clickWindow.place(x= randomX, y=randomY)
    clickWindow.bind("<Button-1>",lambda event:[MouseScorePlus(event),window.unbind("<Button-1>"),clickWindow.destroy(),randomLabel()])
    
    
def clickTwice():
    global randomPlaceX
    global randomPlaceY
    randomX = random.choice(randomPlaceX)
    randomY = random.choice(randomPlaceY)
    clickWindow = tkinter.Label(window)
    clickWindow.config(text = 'Click Twice!')
    clickWindow.config(bg='orange',fg='black')
    clickWindow.pack(ipady= '20',ipadx='20')
    clickWindow.place(x= randomX, y=randomY)
    window.bind("<Double-Button-1>",lambda event:[MouseScorePlus(event),window.unbind("<Double-Button-1>"),clickWindow.destroy(),randomLabel()])

def clickTrice():
    global randomPlaceX
    global randomPlaceY
    randomX = random.choice(randomPlaceX)
    randomY = random.choice(randomPlaceY)
    clickWindow = tkinter.Label(window)
    clickWindow.config(text = 'Click Trice!')
    clickWindow.config(bg='yellow',fg='black')
    clickWindow.pack(ipady= '20',ipadx='20')
    clickWindow.place(x= randomX, y=randomY)
    window.bind("<Triple-Button-1>",lambda event:[MouseScorePlus(event),window.unbind("<Triple-Button-1>"),clickWindow.destroy(),randomLabel()])

def clickW():
    global randomPlaceX
    global randomPlaceY
    randomX = random.choice(randomPlaceX)
    randomY = random.choice(randomPlaceY)
    clickWindow = tkinter.Label(window)
    clickWindow.config(text = 'Press W!')
    clickWindow.config(bg='green',fg='black')
    clickWindow.pack(ipady= '20',ipadx='20')
    clickWindow.place(x= randomX, y=randomY)
    window.bind("w",lambda event:[KeyBoardPlus(event),clickWindow.destroy(),window.unbind("w"),randomLabel()]) and window.bind("W",lambda event:[KeyBoardPlus(event),clickWindow.destroy(),window.unbind("W"),randomLabel()])

def clickA():
    global randomPlaceX
    global randomPlaceY
    randomX = random.choice(randomPlaceX)
    randomY = random.choice(randomPlaceY)
    clickWindow = tkinter.Label(window)
    clickWindow.config(text = 'Press A!')
    clickWindow.config(bg='lightblue',fg='black')
    clickWindow.pack(ipady= '20',ipadx='20')
    clickWindow.place(x= randomX, y=randomY)
    window.bind("a",lambda event:[KeyBoardPlus(event),window.unbind("a"),clickWindow.destroy(),randomLabel()]) and window.bind("A",lambda event:[KeyBoardPlus(event),window.unbind("A"),clickWindow.destroy(),randomLabel()])


def clickS():
    global randomPlaceX
    global randomPlaceY
    randomX = random.choice(randomPlaceX)
    randomY = random.choice(randomPlaceY)
    clickWindow = tkinter.Label(window)
    clickWindow.config(text = 'Press S!')
    clickWindow.config(bg='pink',fg='black')
    clickWindow.pack(ipady= '20',ipadx='20')
    clickWindow.place(x= randomX, y=randomY)
    window.bind("s",lambda event:[KeyBoardPlus(event),window.unbind("s"),clickWindow.destroy(),randomLabel()]) and window.bind("S",lambda event:[KeyBoardPlus(event),window.unbind("S"),clickWindow.destroy(),randomLabel()])
    

def clickD():
    global randomPlaceX
    global randomPlaceY
    randomX = random.choice(randomPlaceX)
    randomY = random.choice(randomPlaceY)
    clickWindow = tkinter.Label(window)
    clickWindow.config(text = 'Press D!')
    clickWindow.config(bg='purple',fg='black')
    clickWindow.pack(ipady= '20',ipadx='20')
    clickWindow.place(x= randomX, y=randomY)
    window.bind("d",lambda event:[KeyBoardPlus(event),window.unbind("d"),clickWindow.destroy(),randomLabel()]) and window.bind("D",lambda event:[KeyBoardPlus(event),window.unbind("D"),clickWindow.destroy(),randomLabel()])

def clickSpace():
    global randomPlaceX
    global randomPlaceY
    randomX = random.choice(randomPlaceX)
    randomY = random.choice(randomPlaceY)
    clickWindow = tkinter.Label(window)
    clickWindow.config(text = 'Press Space!')
    clickWindow.config(bg='white',fg='black')
    clickWindow.pack(ipady= '20',ipadx='20')
    clickWindow.place(x= randomX, y=randomY)
    window.bind("<space>",lambda event:[KeyBoardPlus(event),window.unbind("<space>"),clickWindow.destroy(),randomLabel()])
    
def confirm():
    global score
    global a
    answer = askyesno(title='confirmation',
                    message=f'Your score is: {score} \n Do you want to try again?')
    if answer:
        score = 0
        a = 21
        scoreLabel['text'] = f"Score: {score}"
        BeginFPS()
    else:
        window.destroy()

def BeginFPS():
    CountDown()
    randomLabel()

window = tkinter.Tk()
window.geometry('300x300')
stringVar = tkinter.StringVar(value=f"Time remaining {a}")

entry1 = tkinter.Entry (window) 
entry1.insert(0, "20")
entry1.pack(ipadx=20,ipady=20)

timeLabel = tkinter.Label(window)
timeLabel.config(textvariable=stringVar)
timeLabel.config(bg='black',fg='white')
timeLabel.pack(ipadx= '0',fill='x',expand=True,side='left',anchor='nw')


scoreLabel = tkinter.Label(window)
scoreLabel.config(text=f"Score: {score}")
scoreLabel.config(bg='red',fg='black')
scoreLabel.pack(ipadx= '0',fill='x',expand=True,side='right',anchor='ne')

beginButton = tkinter.Button(window,text='Press To Begin The Game',command=lambda:[BeginFPS(),beginButton.destroy(),entry1.destroy()])
beginButton.place(x= '150', y= '150', anchor='center')




window.mainloop()
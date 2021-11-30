import tkinter as tk
import tkinter
from tkinter import ttk
import time
from tkinter.messagebox import showinfo
import tkinter.messagebox
from typing import Text


Time = time.localtime()
CurrentYear =Time[0]
CurrentMonth = Time[1]
CurrentDay = Time[2]
MonthList = ['January','February','March','April','May','June','July','Augustus','September','October','November','December']

def calculateStuff():                                                                                                                                                                                   
    MonthVar = Monthcombobox.get()
    MonthVar = (MonthList.index(MonthVar) +1)
    calculateMonth = int(MonthVar) - int(CurrentMonth)
    messageVar = ""
    if calculateMonth < 0:
        messageVar += (f"This was {-calculateMonth} month(s) ago. ")
    elif calculateMonth > 0:
        messageVar += (f"This is {calculateMonth} over month(s).")
    else:
        messageVar += ("This is the current month")
    var = combobox.get()
    calculate = int(var) - int(CurrentDay)
    if calculate < 0:
        messageVar += (f"This was {-calculate} day(s) ago. ")
    elif calculate > 0:
        messageVar += (f"This is {calculate} over day(s).")
    else:
        messageVar += ("This is today!:)")
    YearVar = YearEntry.get()
    yearCalculate = int(YearVar) - int(CurrentYear)
    if yearCalculate < 0:
        messageVar += (f"This was {-yearCalculate} year(s) ago. ")
    elif yearCalculate > 0:
        messageVar += (f"This is {yearCalculate} over year(s).")
    else:
        messageVar += ("This is the current year!")
    
    tkinter.messagebox.showinfo("Wie dit leest is cool B)",messageVar)
    
#De main window
window = tk.Tk()
window.geometry('150x150')
#De combobox
combobox = ttk.Combobox(window)
combobox['values'] = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
combobox["state"] = "readonly"
combobox.pack()
#Month Combobox
Monthcombobox = ttk.Combobox(window)
Monthcombobox['values'] = MonthList
Monthcombobox["state"] = "readonly"
Monthcombobox.pack()
#Year Entry:
YearEntry = tk.Entry()
Yearlabel = tk.Label(text= "please put in the year: ")
Yearlabel.pack(ipady=5, ipadx=5 )
YearEntry.pack(ipadx=5,ipady=5)
#De button
button = tk.Button(text="Press",command=calculateStuff)
button.pack(ipadx=5, ipady=5)



window.mainloop()
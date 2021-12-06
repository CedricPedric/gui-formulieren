import tkinter as tk
from tkinter import TclVersion, ttk
from tkinter.messagebox import showinfo, showerror
from typing import List, Text

# root window
root = tk.Tk()
root.geometry('300x400')
root.resizable(False, False)
root.title('Event Form')


def show_selected():
    ListResults = []

    ListResults.append(entry1.get())
    ListResults.append(entry2.get())
    ListResults.append(entry3.get())
    ListResults.append(selected_date.get())
    ListResults.append(selected_age.get())
    if "" in ListResults:
        showerror(
            title='Warning!',
            message="Please make u filled everything in!"
        )
    else:
        Ticket = f"{ListResults[0]} CODE:"
        if ListResults[3] == '19 December 2021':
            Ticket += "D"
        elif ListResults[3] == '9 Januari 2022':
            Ticket += "J"
        elif ListResults[3] == "7 Maart 2022":
            Ticket += "M"
        Ticket += ListResults[4]
        showinfo(
        title='Result',
        message= Ticket
        )


selected_age = tk.StringVar()
sizes = (('Boven de 16, Onder de 18', 'N'),
        ('Boven de 18+', 'L'))

# label
label = ttk.Label(text="What is your age:")
label.pack(fill='x', padx=5, pady=5)

# radio buttons
for size in sizes:
    r = ttk.Radiobutton(
        root,
        text=size[0],
        value=size[1],
        variable=selected_age
    )
    r.pack(fill='x', padx=5, pady=5)

label2 = tk.Label(text="What is your Full Name:")
label2.pack(fill='x', padx=5, pady=5)
entry1 = tk.Entry()
entry1.pack(fill='x', padx=5, pady=5)

label3 = tk.Label(text="What is your Email:")
label3.pack(fill='x', padx=5, pady=5)
entry2 = tk.Entry()
entry2.pack(fill='x', padx=5, pady=5)

label4 = tk.Label(text="What is your Phone Number:")
label4.pack(fill='x', padx=5, pady=5)
entry3 = tk.Entry()
entry3.pack(fill='x', padx=5, pady=5)

label5 = ttk.Label(text="Please select when u want to come:")
label5.pack(fill=tk.X, padx=5, pady=5)

Dates = ["19 December 2021","9 Januari 2022","7 Maart 2022"]
selected_date = tk.StringVar()
month_cb = ttk.Combobox(root, textvariable=selected_date)

month_cb['values'] = Dates
month_cb['state'] = 'readonly'
month_cb.pack(fill=tk.X, padx=5, pady=5)

# button
button = ttk.Button(
    root,
    text="Press when selected",
    command=show_selected)

button.pack(fill='x', padx=5, pady=5)


root.mainloop()






import tkinter as tk

SIZE = 10



root = tk.Tk()
root.geometry('100x100')
canvas = tk.Canvas(root)
canvas.pack()

color = 'white'
for y in range(8):
    for x in range(8):
        x1 = x*SIZE
        y1 = y*SIZE
        x2 = x1 + SIZE
        y2 = y1 + SIZE
        canvas.create_rectangle((x1, y1, x2, y2), fill=color)
        if color == 'white':
            color = 'black'
        else:    
            color = 'white'
    if color == 'white':
        color = 'black'
    else:    
        color = 'white'


root.mainloop()  
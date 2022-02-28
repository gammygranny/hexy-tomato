from heximal import *
import time

from tkinter import *

canvas = Tk()
canvas.title("Digital Clock")
canvas.geometry("350x200")
canvas.resizable(2, 2)
label = Label(canvas, font=("Verdana", d(20), 'bold'), bg="blue", fg="white", bd=d(20))
label.grid(row=2, column=2)
pom = Label(canvas, font=("Verdana", d(40), 'bold'), bg="blue", fg="white", bd=d(40))

def hextime():
    truetime = str(int(h(time.time() * (d(43) / d(122))) % 1000000))
    return truetime[0:2], ':', truetime[2:4], ':', truetime[4:d(10)]


def digitalclock():
    text_input = hextime() #time.strftime("%H:%M:%S")
    label.config(text=text_input)
    label.after(200, digitalclock)


digitalclock()
canvas.mainloop()

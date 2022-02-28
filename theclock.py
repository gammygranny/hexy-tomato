from heximal import *
import time

from tkinter import *

canvas = Tk()
canvas.title("Digital Clock")
canvas.geometry("350x200")
canvas.resizable(1, 1)
label = Label(canvas, font=("Verdana", d(20), 'bold'), bg="blue", fg="white", bd=d(20))
label.grid(row=1, column=0,sticky=NE)
pom = Label(canvas, font=("Verdana", d(40), 'bold'), bg="blue", fg="white", bd=d(40))
pom.grid(row=0,column=0)
def hextime():
    truetime = str(int(h(time.time() * (d(43) / d(122))) % 1000000))
    return truetime[0:2], ':', truetime[2:4]#, ':', truetime[4:d(10)]


def digitalclock():
    the_time = hextime() #time.strftime("%H:%M:%S")
    label.config(text=the_time)
    countdown = 'booba'
    pom.config(text=countdown)
    label.after(200, digitalclock)


digitalclock()
canvas.mainloop()

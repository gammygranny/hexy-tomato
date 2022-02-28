from heximal import *
import time
import tkinter as tk
import time

from tkinter import *

canvas = Tk()
canvas.title("Digital Clock")
canvas.geometry("350x200")
canvas.resizable(1, 1)
label = Label(canvas, font=("Courier", 30, 'bold'), bg="blue", fg="white", bd=30)
label.grid(row=0, column=1)

def hextime():
    truetime = str(int(h(time.time() * (d(43) / d(122))) % 1000000))
    return truetime[0:2], ':', truetime[2:4], ':', truetime[4:d(10)]


def digitalclock():
    text_input = hextime() #time.strftime("%H:%M:%S")
    label.config(text=text_input)
    label.after(200, digitalclock)


digitalclock()
canvas.mainloop()


i = lasttime = 0
while i < d(50):
    truetime = str(int(h(time.time() * (d(43) / d(122))) % 1000000))
    if lasttime != truetime:
        clear_screen()
        print(int(h(time.time() * (d(43) / d(122)))))
        print(truetime[0:2], ':', truetime[2:4], ':', truetime[4:d(10)])
        lasttime = truetime
        i += 1

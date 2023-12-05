from tkinter import *

import random

JATEK_SZELESSEG = 700
JATEK_MAGASSAG = 700
GYORSASAG = 50
HELY_MERET = 50 #maga a kaja és a kígyó nagysága
TESTRESZ = 2
KIGYO_SZINE = "#0b99e0"
KAJA_SZINE = "#ebbc13"
HATTERSZIN = "#83eb13"


class Kigyo:
    pass

class Etel:
    pass

def next_turn():
    pass

def change_direction():
    pass

def check_collisions():
    pass

def game_over():
    pass

window = Tk()
window.title("Kígyós Játék")
window.resizable(False,False)

pontszam = 0
elhelyezes = 'top'

label = Label(window, text = "Pontszám: {}".format(pontszam),font=('Verdana', 30))
label.pack()

canvas = Canvas(window, bg = HATTERSZIN, height=JATEK_MAGASSAG, width=JATEK_SZELESSEG)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}") # nem lehet float érték, csak int. ezért castoltam

window.mainloop()
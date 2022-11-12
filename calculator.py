from tkinter import *
import math

window = Tk()

window.title("Entry Logger")
window.geometry("650x900")
z = ""

def one():
    global z
    global e_value
    z += "1"
    e_value.set(z)

def two():
    global z
    global e_value
    z += "2"
    e_value.set(z)

def three():
    global z
    global e_value
    z += "3"
    e_value.set(z)

def four():
    global z
    global e_value
    z += "4"
    e_value.set(z)

def five():
    global z
    global e_value
    z += "5"
    e_value.set(z)

def six():
    global z
    global e_value
    z += "6"
    e_value.set(z)

def seven():
    global z
    global e_value
    z += "7"
    e_value.set(z)

def eight():
    global z
    global e_value
    z += "8"
    e_value.set(z)

def nine():
    global z
    global e_value
    z += "9"
    e_value.set(z)

def zero():
    global z
    global e_value
    z += "0"
    e_value.set(z)

def power():
    global z
    global e_value
    z += "**"
    e_value.set(z)

def plus():
    global z
    global e_value
    z += "+"
    e_value.set(z)

def minus():
    global z
    global e_value
    z += "-"
    e_value.set(z)

def mult():
    global z
    global e_value
    z += "*"
    e_value.set(z)

def div():
    global z
    global e_value
    z += "/"
    e_value.set(z)

def root():
    global z
    global e_value
    z += "**0.5"
    z = eval(z)
    z = str(z)
    e_value.set(z)

def lB():
    global z
    global e_value
    z += "("
    e_value.set(z)

def rB():
    global z
    global e_value
    z += ")"
    e_value.set(z)

def dec():
    global z
    global e_value
    z += "."
    e_value.set(z)


def sine():
    global z
    global e_value
    z = eval(z)
    z = math.sin(z)
    z = str(z)
    e_value.set(z)

def cosine():
    global z
    global e_value
    z = eval(z)
    z = math.cos(z)
    z = str(z)
    e_value.set(z)

def tangent():
    global z
    global e_value
    z = eval(z)
    z = math.tan(z)
    z = str(z)
    e_value.set(z)

def secant():
    global z
    global e_value
    z = eval(z)
    z = math.acos(z)
    z = str(z)
    e_value.set(z)

def cosecant():
    global z
    global e_value
    z = eval(z)
    z = math.asin(z)
    z = str(z)
    e_value.set(z)

def cotangent():
    global z
    global e_value
    z = eval(z)
    z = math.atan(z)
    z = str(z)
    e_value.set(z)

def eq():
    global z
    global e_value
    try:
        z = eval(z)
        z = str(z)
        e_value.set(z)
    except:
        e_value.set("ERROR!")

def clr():
    global z
    global e_value
    z = ""
    e_value.set(z)

e_value = StringVar()
e = Entry(window, textvariable = e_value, font='Calibri 30')
e.config(state= "disabled")

#1
button11 = Button(window, text = "  1  ", command = one, font='Calibri 32', bg='red')
button12 = Button(window, text = "  2  ", command = two, font='Calibri 32', bg='red')
button13 = Button(window, text = "  3  ", command = three, font='Calibri 32', bg='red')
#2
button21 = Button(window, text = "  4  ", command = four, font='Calibri 32', bg='red')
button22 = Button(window, text = "  5  ", command = five, font='Calibri 32', bg='red')
button23 = Button(window, text = "  6  ", command = six, font='Calibri 32', bg='red')

#3
button31 = Button(window, text = "  7  ", command = seven, font='Calibri 32', bg='red')
button32 = Button(window, text = "  8  ", command = eight, font='Calibri 32', bg='red')
button33 = Button(window, text = "  9  ", command = nine, font='Calibri 32', bg='red')

#4
button41 = Button(window, text = "  0  ", command = zero, font='Calibri 32', bg='red')
button42 = Button(window, text = "  ** ", command = power, font='Calibri 32', bg='red')
button43 = Button(window, text = "  +  ", command = plus, font='Calibri 32', bg='red')

#5
button51 = Button(window, text = "  -  ", command = minus, font='Calibri 32', bg='red')
button52 = Button(window, text = "  *  ", command = mult, font='Calibri 32', bg='red')
button53 = Button(window, text = "  /  ", command = div, font='Calibri 32', bg='red')

#6
button61 = Button(window, text = "  .  ", command = dec, font='Calibri 32', bg='red')
button62 = Button(window, text = "  (  ", command = lB, font='Calibri 32', bg='red')
button63 = Button(window, text = "  )  ", command = rB, font='Calibri 32', bg='red')

#7
button71 = Button(window, text = " ²√  ", command = root, font='Calibri 32', bg='pink')
buttonE = Button(window, text= "  =  ", command = eq, font='Calibri 32', bg = 'blue')
buttonC = Button(window, text= "  C  ", command = clr, font='Calibri 32', bg = 'blue')

#8
button81 = Button(window, text = " sin ", command = sine, font='Calibri 32', bg='pink')
button82 = Button(window, text = " cos ", command = cosine, font='Calibri 32', bg='pink')
button83 = Button(window, text = " tan ", command = tangent, font='Calibri 32', bg='pink')

#9
button91 = Button(window, text = "cosec", command = cosecant, font='Calibri 32', bg='pink')
button92 = Button(window, text = " sec ", command = secant, font='Calibri 32', bg='pink')
button93 = Button(window, text = " cot ", command = cotangent, font='Calibri 32', bg='pink')


e.grid(row = 1, column = 1)

button11.grid(row = 2, column = 0)
button12.grid(row = 2, column = 1)
button13.grid(row = 2, column = 2)

button21.grid(row = 3, column = 0)
button22.grid(row = 3, column = 1)
button23.grid(row = 3, column = 2)

button31.grid(row = 4, column = 0)
button32.grid(row = 4, column = 1)
button33.grid(row = 4, column = 2)

button41.grid(row = 5, column = 0)
button42.grid(row = 5, column = 1)
button43.grid(row = 5, column = 2)

button51.grid(row = 6, column = 0)
button52.grid(row = 6, column = 1)
button53.grid(row = 6, column = 2)

button61.grid(row = 7, column = 0)
button62.grid(row = 7, column = 1)
button63.grid(row = 7, column = 2)

button71.grid(row = 8, column = 0)
buttonE.grid(row = 8, column = 1)
buttonC.grid(row = 8, column = 2)

button81.grid(row = 9, column = 0)
button82.grid(row = 9, column = 1)
button83.grid(row = 9, column = 2)

button91.grid(row = 10, column = 0)
button92.grid(row = 10, column = 1)
button93.grid(row = 10, column = 2)

window.mainloop()
## Imports
from tkinter import *

## Window
window = Tk()
window.geometry("1200x6000")
window.title("Standalone Caeser GUI")

Tops = Frame(window, width = 1600, relief = SUNKEN)
Tops.pack(side = TOP)

f1 = Frame(window, width = 800, height = 700,
                            relief = SUNKEN)
f1.pack(side = LEFT)

## String Variables
rand = StringVar()
string = StringVar()
shift = IntVar()
code = StringVar()
cipher = StringVar()

## Functions
def encrypt(string, shift):

    cipher = ''
    for char in string:
        if char == ' ':
            cipher = cipher + char
        elif  char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)

    return cipher

def decrypt(string, shift):

    cipher = ''
    for char in string:
        if char == ' ':
            cipher = cipher + char
        elif  char.isupper():
            cipher = cipher + chr((ord(char) - shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) - shift - 97) % 26 + 97)

    return cipher

def Output():
    print("String= ", (string.get()))

    stringF = string.get()
    shiftF = shift.get()
    codeF = code.get()

    if (codeF == 'e'):
        cipher.set(encrypt(stringF, shiftF))
    else:
        cipher.set(decrypt(stringF, shiftF))

def Reset():
    rand.set("")
    string.set("")
    shift.set("")
    code.set("")
    cipher.set("")

def Exit():
    window.destroy()
## Buttons
btnTotal = Button(f1, padx = 16, pady = 8, bd = 16, fg = "black",
                 font = ('arial', 16), width = 10,
                 text = "Encrypt/Decrypt",
                 command = Output).grid(row = 7, column = 1)

btnReset = Button(f1, padx = 16, pady = 8, bd = 16,fg = "black",
                 font = ('arial', 16), width = 10,
                 text = "Reset",
                 command = Reset).grid(row = 7, column = 2)

btnExit = Button(f1, padx = 16, pady = 8, bd = 16,
                 fg = "black", font = ('arial', 16),width = 10,
                 text = "Exit",
                 command = Exit).grid(row = 7, column = 3)

## Labels
lblStr = Label(f1, font = ('arial', 16),
         text = "String", bd = 16, anchor = "w")

lblShi = Label(f1, font = ('arial', 16),
            text = "shift", bd = 16, anchor = "w")

lblCod = Label(f1, font = ('arial', 16),
          text = "code(e for encrypt, d for decrypt)",
                                bd = 16, anchor = "w")

lblOutput = Label(f1, font = ('arial', 16),
             text = "The cipher-", bd = 16, anchor = "w")

## Textboxes
txtStr = Entry(f1, font = ('arial', 16),
         textvariable = string, bd = 10, insertwidth = 4, justify = 'right')

txtShi = Entry(f1, font = ('arial', 16),
         textvariable = shift, bd = 10, insertwidth = 4, justify = 'right')

txtCod = Entry(f1, font = ('arial', 16),
          textvariable = code, bd = 10, insertwidth = 4, justify = 'right')

txtOutput = Entry(f1, font = ('arial', 16),
             textvariable = cipher, bd = 10, insertwidth = 4, justify = 'right')

## Grid Position
lblStr.grid(row = 1, column = 0)
txtStr.grid(row = 1, column = 1)
lblShi.grid(row = 2, column = 0)
txtShi.grid(row = 2, column = 1)
lblCod.grid(row = 3, column = 0)
txtCod.grid(row = 3, column = 1)
lblOutput.grid(row = 2, column = 2)
txtOutput.grid(row = 2, column = 3)

## Main()
window.mainloop()
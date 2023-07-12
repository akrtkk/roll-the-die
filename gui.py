# tkinter module for window
from tkinter import *
# random for random number
from random import randint
# Roll functions
def roll():
    text.delete(0.0, END)
    text.insert(END, str(randint(1, 6)))

# Setup of window
tk = Tk()
tk.geometry("400x210")
tk.title("Roll The Die")
tk.iconbitmap("dice.ico")
# Number box and Button
text = Text(tk, width=50, height=5, font=("Arial", 18))
buttonA = Button(tk, text="Press to roll!", command=roll, width=50, height=10)
# Initialization of button, text box and window
text.pack()
buttonA.pack()
tk.mainloop()


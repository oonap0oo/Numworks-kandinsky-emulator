# This code allows a MicroPython program made for the Numworks calculator
# that makes use of the kandinsky module to run under CPython
# it emulates kandinsky using Tkinter.
# Shared without any warranty
# 
# add to the end of the Numworks Micropython code:
# only for running under Cpython:
# >>>  kandinsky.mainloop()   <<<

from tkinter import *

def color(*args):
    r, g, b  = args
    color_str = f"#{r:02x}{g:02x}{b:02x}"
    return color_str
    
def set_pixel(x, y, col):
    x1, y1 = x * magnification, y * magnification
    x2, y2 = x1 + magnification, y1 + magnification
    canvas1.create_rectangle(x1, y1, x2, y2, fill = col) 
    
def fill_rect(x, y, width, height,col):
    x1, y1 = x * magnification, y * magnification
    width1, height1 = width * magnification, height * magnification
    canvas1.create_rectangle(x1, y1, x1 + width1, y1 + height1, fill = col)
    
def draw_string(txt, x, y, fg_color = "black", bg_color = "white"):
    x1, y1 = x * magnification, y * magnification
    canvas1.create_text(x1, y1, text = txt, fill = fg_color, font = ("", 13))
    
magnification = 2 # size of a pixel in the Tkinter window compared to a pixel in the calculator
kandinsky_width = 320 # width of calculator screen
kandinsky_height = 240 # height of calculator screen
# generating a tkinter window with a canvas widget
window = Tk()
canvas1 = Canvas(window, 
                width = kandinsky_width * magnification, 
                height = kandinsky_height * magnification)
canvas1.pack()

# add to the Numworks Micropython code:
# only for running under Cpython:
# >>>  kandinsky.mainloop()   <<<
    


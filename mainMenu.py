import numpy as np
import pandas as pd
from tkinter import *
from PIL import ImageTk, Image
from openpyxl.workbook import Workbook
from tkcalendar import *
from openpyxl import load_workbook
from tkinter.font import Font
from tkinter import ttk


screen = Tk()
screen.minsize(600 , 600)
screen.maxsize(600 , 600)
screen.title("UniNode")
screen.iconbitmap(" /Users/emmaeconomopoulou/Desktop/gui/logo.ico")
screen.configure(background = "white")


my_img=ImageTk.PhotoImage(Image.open("/Users/emmaeconomopoulou/Desktop/gui/logo.png"))
my_label=Label(image=my_img)
my_label.pack()


custFont = Font(
    family = "Helvetica",
    size = 24,
    weight = "bold"
)

title= Label (text="Main Menu", font = custFont, fg =  "#800000")
title.place(x=230, y=130)

button1= Button(screen, text= "University Map",width = 15 ,height = 7 ,fg ="#800000")
button1.place(x=60, y =200)

button2= Button(screen, text= "Calendar",width = 15 ,height = 7 ,fg ="#800000")
button2.place(x=230, y =200)

button3= Button(screen, text= "giaKafedaki",width = 15 ,height = 7 ,fg ="#800000")
button3.place(x=400, y =200)

button4= Button(screen, text= "Average Grade",width = 15 ,height = 7 ,fg ="#800000")
button4.place(x=60, y =350)

button5= Button(screen, text= "Add friend",width = 15 ,height = 7 ,fg ="#800000")
button5.place(x=230, y =350)

button6= Button(screen, text= "Meet Professor",width = 15 ,height = 7 ,fg ="#800000")
button6.place(x=400, y =350)

button_quit= Button(screen ,text= "Exit",width = 10 ,height = 2 ,fg ="#800000", command = screen.quit)
button_quit.place(x= 450, y=520)

screen.mainloop()
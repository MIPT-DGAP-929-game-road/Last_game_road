from tkinter import *
from random import randrange as rnd, choice
 
root = Tk()
root.geometry('1500x650+0+0')
 
canv = Canvas(bg='white')
canv.pack(fill=BOTH,expand=1)

#---------------------------------------------------------------menu_itself------------------------------------------------------------------------------------------- 

def play_view():

def keypres_play():
    
play_view()
root.bind('<Key>',keypress_play)
mainloop()
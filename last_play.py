from tkinter import *
from random import randrange as rnd, choice
 
root = Tk()
root.geometry('1500x800+0+0')
 
canv = Canvas(bg='white')
canv.pack(fill=BOTH,expand=1)

#---------------------------------------------------------------menu_itself------------------------------------------------------------------------------------------- 
def play_view():
	font = canv.create_rectangle(0,0,1500,800, fill='orange')
	road = canv.create_rectangle(300,0,1200,800, fill='gray')
	#car 1 red
	car_view(1)
	com_1 = canv.create_rectangle(0,700, 300,800, fill='gray', outline='red', width=4)
	com_text_1 = canv.create_text((0+300)/2, (700+800)/2-40, text="RED car's statistics:", justify=CENTER, font="Verdana 14", fill='black')
	com_fuel_1 = canv.create_text((0+300)/2-85, (700+800)/2-10, text="fuel level:", font="Verdana 14", fill='black')
	com_wheels_1 = canv.create_text((0+300)/2-50, (700+800)/2+20, text="wheel's hardness:", font="Verdana 14", fill='black') 
	#car 2 blue
	car_view(2)
	com_2 = canv.create_rectangle(1200,700,1500,800, fill='gray', outline='blue', width=4) 
	com_text_2 = canv.create_text((1200+1500)/2, (700+800)/2-40, text="BLUE car's statistics:", justify=CENTER, font="Verdana 14", fill='black')
	com_fuel_2 = canv.create_text((1200+1500)/2-85, (700+800)/2-10, text="fuel level:", justify=CENTER, font="Verdana 14", fill='black')
	com_wheels_2 = canv.create_text((1200+1500)/2-50, (700+800)/2+20, text="wheel's hardness:", justify=CENTER, font="Verdana 14", fill='black') 
	
def keypress_play(event):
	print(event.keycode)
	car_view(1)
	car_view(2)
	#----------car_class
def car_view(number):
	if number == 1:
		color = 'red'
		x_create = 450
		y_create = 640
	if number == 2:
		color = 'blue'
		x_create = 1050
		y_create = 640
	length = 100
	width = 50
	obj_car = canv.create_rectangle(x_create-width/2, y_create-length/2, x_create+width/2, y_create+length/2, fill=color)
	
play_view()
root.bind('<Key>',keypress_play)
mainloop()
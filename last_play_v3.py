# ---------------------------------------------------------------inicialising-------------------------------------------------------------------------------------------
from tkinter import *
from random import randrange as rnd, choice
root = Tk()
root.geometry('1500x600+0+0')
canv = Canvas(bg='white')
canv.pack(fill=BOTH, expand=1)
# ---------------------------------------------------------------creating characters and giving them their unics-------------------------------------------------------------------------------------------
class car:
	def __init__(self,color,x,y,v_x,v_y):
		self.x = x
		self.y = y
		self.color = color
		self.v_x = v_x
		self.v_y = v_y
		self.length = 100
		self.width = 50
		self.k_fuel = 0
		self.k_wheels = 0
		self.obj = canv.create_rectangle(self.x - self.width / 2, self.y - self.length / 2, 
										 self.x + self.width / 2, self.y + self.length / 2, 
										 fill=self.color)

	def motion(self, key_code, code_word):
		if code_word == 'wasd':    
			if key_code == 68 or key_code == 65: 
				if key_code == 68: #right
					self.v_x = 5
				if key_code == 65: #left
					self.v_x =-5
			else:
				self.v_x = 0
			if key_code == 87 or key_code == 83:
				if key_code == 87: # up
					self.v_y = -10
					#/((self.y-640)**2+1)
				if key_code == 83: # down
					self.v_y = 10
					#/((self.y-640)**2+1)
			else:
				self.v_y = 0
		if code_word == 'urdl':    
			if key_code == 39 or key_code == 37: 
				if key_code == 39: #right
					self.v_x = 5
				if key_code == 37: #left
					self.v_x =-5
			else:
				self.v_x = 0
			if key_code == 38 or key_code == 40:
				if key_code == 38: # up
					self.v_y = -10
					#/((self.y-640)**2+1)
				if key_code == 40: # down
					self.v_y = 10
					#/((self.y-640)**2+1)
			else:
				self.v_y = 0
		self.v_x = self.v_x/(self.k_wheels+1)
		self.v_y = self.v_y/(self.k_wheels+1)
		self.y += self.v_y
		self.x += self.v_x
		#print(self.x,self.y,"       ", self.v_x, self.v_y)
		canv.move(self.obj,self.v_x,self.v_y)
		
	def properties(self,decr_fuel,decr_wheels):
		self.k_fuel += decr_fuel
		self.k_wheels += decr_wheels

def hittest(obj_1, obj_2):
		if  (obj_1.x - obj_2.x)**2 <= ((obj_1.width+obj_2.width)/2)**2 and (obj_1.y - obj_2.y)**2 <= ((obj_1.length+obj_2.length)/2)**2:
			return True
		else:
			return False
	
# ---------------------------------------------------------------view of a background: road, font and two tables of statictics-------------------------------------------------------------------------------------------
def play_view():
	font = canv.create_rectangle(0, 0, 1500, 800, fill='orange')
	road = canv.create_rectangle(300, 0, 1200, 800, fill='gray')
	# car left
	com_1 = canv.create_rectangle(0, 700, 300, 800, fill='gray', outline='red', width=4)
	com_text_1 = canv.create_text((0 + 300) / 2, (700 + 800) / 2 - 40, text="RED car's statistics:", justify=CENTER,
								  font="Verdana 14", fill='black')
	com_fuel_1 = canv.create_text((0 + 300) / 2 - 85, (700 + 800) / 2 - 10, text="fuel level:", font="Verdana 14",
								  fill='black')
	com_wheels_1 = canv.create_text((0 + 300) / 2 - 50, (700 + 800) / 2 + 20, text="wheel's hardness:",
									font="Verdana 14", fill='black')
	# car right
#    com_2 = canv.create_rectangle(1200, 700, 1500, 800, fill='gray', outline='blue', width=4)
#    com_text_2 = canv.create_text((1200 + 1500) / 2, (700 + 800) / 2 - 40, text="BLUE car's statistics:",
#                                  justify=CENTER, font="Verdana 14", fill='black')
#    com_fuel_2 = canv.create_text((1200 + 1500) / 2 - 85, (700 + 800) / 2 - 10, text="fuel level:", justify=CENTER,
#                                  font="Verdana 14", fill='black')
#    com_wheels_2 = canv.create_text((1200 + 1500) / 2 - 50, (700 + 800) / 2 + 20, text="wheel's hardness:",
#                                    justify=CENTER, font="Verdana 14", fill='black')

# ---------------------------------------------------------------interaction with players: checking buuttons press, #moving cars and checking them touching each other and road border#-------------------------------------------------------------------------------------------
def keypress_play(event):
	#print(event.keycode)
	ex_touch = False
	car_left.motion(event.keycode,'wasd')
	#if hittest(car_left, car_right):
		#car_left.properties(0,0.5*10**(-4))
		#car_right.properties(0,0.5*10**(-4))
	#car_right.motion(event.keycode,'urdl')
	#if hittest(car_left, car_right):
		#car_left.properties(0,0.5*10**(-4))
		#car_right.properties(0,0.5*10**(-4))
	for car_ord in cars_ord:
		if hittest(car_left, car_ord):
			car_left.properties(0,0.5*10**(-4))
			print('touch')
		car_ord.x += car_ord.v_x
		car_ord.y += car_ord.v_y
		canv.move(car_ord,car_ord.v_x,car_ord.v_y)
		if hittest(car_left, car_ord):
			car_left.properties(0,0.5*10**(-4))
			print('touch')

	
# ---------------------------------------------------------------realising of game-------------------------------------------------------------------------------------------
play_view()
car_left = car('red', 450, 640, 0, 0)
#car_right = car('blue', 1050, 640, 0, 0)
cars_ord = [ car('brown', 750+(50+10)*rnd(-7,8), 0, 0, 10) for i in range(1, 100+1)]
root.bind('<Key>', keypress_play)
mainloop()
# ---------------------------------------------------------------inicialising-------------------------------------------------------------------------------------------
from tkinter import *
from random import randrange as rnd, choice
root = Tk()
root.geometry('1500x600+0+0')
canv = Canvas(bg='white')
canv.pack(fill=BOTH, expand=1)
# ---------------------------------------------------------------creating characters and giving them their unics-------------------------------------------------------------------------------------------
class out:
	def __init__(self, x, y, length, width):
		self.x = x
		self.y = y
		self.length = length
		self.width = width
		self.obj = canv.create_rectangle(self.x - self.width / 2, self.y - self.length / 2, 
										 self.x + self.width / 2, self.y + self.length / 2, 
										 fill='white')

class car:
	def __init__(self,color,x,y,v_x,v_y):
		self.x = x
		self.y = y
		self.color = color
		self.v_x = v_x
		self.v_y = v_y
		self.length = 100
		self.width = 50
		self.k_fuel = 1
		self.k_wheels = 1
		self.distance = 0
		self.obj = canv.create_rectangle(self.x - self.width / 2, self.y - self.length / 2, 
										 self.x + self.width / 2, self.y + self.length / 2, 
										 fill=self.color)

	def movement_control(self, key_code, code_word):
		if code_word == 'wasd':    #buttons w a s d
			if key_code == 68 or key_code == 65: 
				if key_code == 68: #right
					self.v_x += 1/4
				if key_code == 65: #left
					self.v_x += -1/4
			#else:
			#	self.v_x = 0
			if key_code == 87 or key_code == 83:
				if key_code == 87: # up
					self.v_y += -1/4
					#/((self.y-640)**2+1)
				if key_code == 83: # down
					self.v_y += 1/4
					#/((self.y-640)**2+1)
			#else:
			#	self.v_y = 0
		if code_word == 'urdl':    # buttons up right down left
			if key_code == 39 or key_code == 37: 
				if key_code == 39: #right
					self.v_x += 1/4
				if key_code == 37: #left
					self.v_x += -1/4
			#else:
			#	self.v_x = 0
			if key_code == 38 or key_code == 40:
				if key_code == 38: # up
					self.v_y += -1/4
					#/((self.y-640)**2+1)
				if key_code == 40: # down
					self.v_y += 1/4
					#/((self.y-640)**2+1)
			#else:
			#	self.v_y = 0
		self.v_x = self.v_x*(1-0.5)
		self.v_y = self.v_y*(1-0.5)
		self.y += self.v_y
		self.x += self.v_x
		#print(self.x,self.y,"       ", self.v_x, self.v_y)
		if self.k_fuel*self.k_wheels != 0 and (self.x>=out_left.x+self.width/2 and self.x<=out_right.x-self.width/2 and self.y>=self.length/2 and self.y<=800-self.length/2):
			canv.move(self.obj, self.v_x, self.v_y)

	def move_ordinary(self):
		self.v_x = 0
		self.v_y = 0.5
		self.y += self.v_y
		self.x += self.v_x
		#print(self.x,self.y,"       ", self.v_x, self.v_y)
		if self.y <= 800 + self.length/2:
			canv.move(self.obj,self.v_x,self.v_y)
		else:
			a = 1
			#car_ord = car('brown', 750+(50+10)*rnd(-7,8), 0, 0, 10)

	def properties(self,decr_fuel,decr_wheels):
		if self.k_fuel - decr_fuel == 0:
			self.k_fuel -= decr_fuel
		else:
			self.k_fuel = 0

		if self.k_wheels - decr_wheels == 0:
			self.k_wheels -= decr_wheels
		else:
			self.k_wheels = 0

def hit_test(obj_1, obj_2):
		if  (obj_1.x - obj_2.x)**2 <= ((obj_1.width+obj_2.width)/2)**2 and (obj_1.y - obj_2.y)**2 <= ((obj_1.length+obj_2.length)/2)**2:
			if (obj_1.v_y - obj_2.v_y)**2 != 0: #can be only two cars
				change = obj_1.v_y
				obj_1.v_y = obj_2.v_y
				obj_2.v_y = change
			if (obj_1.v_x - obj_2.v_x)**2 != 0:
				if obj_1 == car_left or obj_1 == car_right:
					change = obj_1.v_x
					obj_1.v_x = obj_2.v_x
					obj_2.v_x = change
				else:
					obj_2.v_x = - obj_2.v_x
			return True
		else:
			return False

def update(key_code):
	global kpr
	car_left.movement_control(key_code, 'wasd')
	car_right.movement_control(key_code, 'urdl')
	if hit_test(car_left, car_right):
			car_left.properties(0, 0)
			car_right.properties(0, 0)
	if car_left.k_fuel != 0:
		car_left.distance += 1
	if car_right.k_fuel != 0:
		car_right.distance += 1
	canv.update()

def key_pression(event):
	global kpr
	kpr = event.keycode
	print(event.keycode)
	eventing = event.keycode
	
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
	com_2 = canv.create_rectangle(1200, 700, 1500, 800, fill='gray', outline='blue', width=4)
	сom_text_2 = canv.create_text((1200 + 1500) / 2, (700 + 800) / 2 - 40, text="BLUE car's statistics:",
	                                  justify=CENTER, font="Verdana 14", fill='black')
	com_fuel_2 = canv.create_text((1200 + 1500) / 2 - 85, (700 + 800) / 2 - 10, text="fuel level:", justify=CENTER,
	                                  font="Verdana 14", fill='black')
	com_wheels_2 = canv.create_text((1200 + 1500) / 2 - 50, (700 + 800) / 2 + 20, text="wheel's hardness:",
	                                    justify=CENTER, font="Verdana 14", fill='black')

# ---------------------------------------------------------------interaction with players: checking buuttons press, #moving cars and checking them touching each other and road border#-------------------------------------------------------------------------------------------

def new_game():
	global kpr
	root.bind('<KeyPress>', key_pression)
	#while car_left.k_fuel*car_left.k_wheels + 
	while car_right.k_fuel*car_right.k_wheels != 0:
		for car_ord in cars_ord:
			car_ord.move_ordinary()
			if hit_test(car_ord, car_left): #полседовательность важна 
				car_left.properties(0, 0)
			if hit_test(car_ord, car_right): #полседовательность важна 
				car_right.properties(0, 0)
		update(kpr)
    
# ---------------------------------------------------------------realising of game-------------------------------------------------------------------------------------------

play_view()
kpr = None
car_left = car('red', 450, 640, 0, 0)
car_right = car('blue', 1050, 640, 0, 0)
cars_ord = [ car('brown', 330+60*rnd(1,15), -50-110*rnd(1,100), 0, 10) for i in range(1, 10+1)]
out_left = out(300, 400, 800, 4)
out_right = out(1200, 400, 800, 4)

new_game()

#результат

mainloop()
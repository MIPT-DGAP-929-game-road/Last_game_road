# ---------------------------------------------------------------inicialising-------------------------------------------------------------------------------------------
from tkinter import *
import time
from random import randrange as rnd, choice
root = Tk()
root.geometry('1500x800+0+0')
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
		self.distance = 0
		self.name = ''

	def movement_control(self, key_code):
		#left
		if key_code == 68 or key_code == 65: 
			if key_code == 68: #right
				self.v_x += 1/2
			if key_code == 65: #left
				self.v_x += -1/2
		#else:
		#	self.v_x = 0
		if key_code == 87 or key_code == 83:
			if key_code == 87: # up
				self.v_y += -1/2
				#/((self.y-640)**2+1)
			if key_code == 83: # down
				self.v_y += 1/2
				#/((self.y-640)**2+1)
		#else:
		#	self.v_y = 0
		#right
		if key_code == 39 or key_code == 37: 
			if key_code == 39: #right
				self.v_x += 1/2
			if key_code == 37: #left
				self.v_x += -1/2
		#else:
		#	self.v_x = 0
		if key_code == 38 or key_code == 40:
			if key_code == 38: # up
				self.v_y += -1/2
				#/((self.y-640)**2+1)
			if key_code == 40: # down
				self.v_y += 1/2
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
		if self.y < 800 + self.length + self.v_y:
			canv.move(self.obj,self.v_x,self.v_y)
		else:
			canv.delete(self.obj)
			self.obj = canv.create_oval(
                -100 - 0,
                -100 - 0,
                -100 - 0,
                -100 - 0,
                fill='black', width = 0)

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

def update(key_code_left, key_code_right):
	car_left.movement_control(key_code_left[0])
	car_right.movement_control(key_code_right[0])
	if hit_test(car_left, car_right):
			car_left.properties(0, 1)
			car_right.properties(0, 1)
	if car_left.k_wheels == 0:
		car_left.fuel = 0
		car_left.move_ordinary()
		if car_left.y > 800 + car_left.length:
			canv.delete(car_left.obj)
			car_left.obj = canv.create_oval(
                -100 - 0,
                -100 - 0,
                -100 - 0,
                -100 - 0,
                fill='black', width = 0)
	if car_right.k_wheels == 0:
		car_right.fuel = 0
		car_right.move_ordinary()
		if car_right.y > 800 + car_right.length:
			canv.delete(car_right.obj)
			car_right.obj = canv.create_oval(
                -100 - 0,
                -100 - 0,
                -100 - 0,
                -100 - 0,
                fill='black', width = 0)
	for i in range(0, len(key_code_left)-1):
		key_code_left[i] = key_code_left[i+1]
	canv.delete(key_code_left[len(key_code_left)-1])
	for i in range(0, len(key_code_right)-1):
		key_code_right[i] = key_code_right[i+1]
	#wsprint(key_code_left, key_code_right)
	canv.update()

def key_pression(event):
	key_code = event.keycode
	if key_code == 68 or key_code == 65 or key_code == 87 or key_code == 83:
		key_code_left.append(key_code)
	if key_code == 39 or key_code == 37 or key_code == 38 or key_code == 40:
		key_code_right.append(key_code)
# ---------------------------------------------------------------view of a background: road, font and two tables of statictics-------------------------------------------------------------------------------------------
def play_view():
	font = canv.create_rectangle(0, 0, 1500, 800, fill='orange')
	road = canv.create_rectangle(300, 0, 1200, 800, fill='gray')
	# car left
	com_1 = canv.create_rectangle(0, 650, 300, 800, fill='gray', outline='red', width=4)
	com_text_1 = canv.create_text((0 + 300) / 2, (700 + 800) / 2 - 70, text="RED car's statistics:", justify=CENTER,
								  font="Verdana 14", fill='black')
	com_distance_1 = canv.create_text((0 + 300) / 2 - 50, (700 + 800) / 2 - 40, text="reached distance:", font="Verdana 14",
								  fill='black')
	com_fuel_1 = canv.create_text((0 + 300) / 2 - 85, (700 + 800) / 2 - 10, text="fuel level:", font="Verdana 14",
								  fill='black')
	com_wheels_1 = canv.create_text((0 + 300) / 2 - 50, (700 + 800) / 2 + 20, text="wheel's hardness:",
									font="Verdana 14", fill='black')
	# car right
	com_2 = canv.create_rectangle(1200, 650, 1500, 800, fill='gray', outline='blue', width=4)
	сom_text_2 = canv.create_text((1200 + 1500) / 2, (700 + 800) / 2 - 70, text="BLUE car's statistics:",
	                                  justify=CENTER, font="Verdana 14", fill='black')
	com_distance_2 = canv.create_text((1200 + 1500) / 2 - 50, (700 + 800) / 2 - 40, text="reached distance:", font="Verdana 14",
								  fill='black')
	com_fuel_2 = canv.create_text((1200 + 1500) / 2 - 85, (700 + 800) / 2 - 10, text="fuel level:", justify=CENTER,
	                                  font="Verdana 14", fill='black')
	com_wheels_2 = canv.create_text((1200 + 1500) / 2 - 50, (700 + 800) / 2 + 20, text="wheel's hardness:",
	                                    justify=CENTER, font="Verdana 14", fill='black')

# ---------------------------------------------------------------interaction with players: checking buuttons press, moving cars and checking them touching each other and road border-------------------------------------------------------------------------------------------
key_code_left = []
key_code_left.append(0)
key_code_right = []
key_code_right.append(0)

def new_game():
	global com_text_distance_1, com_text_distance_2
	root.bind('<KeyPress>', key_pression)
	while car_left.k_fuel*car_left.k_wheels + car_right.k_fuel*car_right.k_wheels != 0:
		for car_ord in cars_ord:
			car_ord.move_ordinary()
			if hit_test(car_ord, car_left): #последовательность важна 
				car_left.properties(0, 1)
			if hit_test(car_ord, car_right): #последовательность важна 
				car_right.properties(0, 1)
		lost_time = int(time.time() - t0)
		velocity_sq_mid = 1
		if car_left.k_fuel != 0:
			car_left.distance = (lost_time * velocity_sq_mid) + (800 - car_left.y)/100
		if car_right.k_fuel != 0:
			car_right.distance = (lost_time * velocity_sq_mid) + (800 - car_right.y)/100
		if (car_left.distance*10)//1/10 == car_left.distance:
			canv.delete(com_text_distance_1)
			com_text_distance_1 = canv.create_text((0 + 300) / 2 + 70, (700 + 800) / 2 - 40, text=str((car_left.distance*10)//1/10), font="Verdana 14",
									  fill='black')
		if (car_right.distance*10)//1/10 == car_right.distance:
			canv.delete(com_text_distance_2)
			com_text_distance_2 = canv.create_text((1200 + 1500) / 2 + 70, (700 + 800) / 2 - 40, text=str((car_right.distance*10)//1/10), font="Verdana 14",
									  fill='black')
		update(key_code_left, key_code_right)
    
# ---------------------------------------------------------------realising of game-------------------------------------------------------------------------------------------

play_view()

car_left = car('red', 450, 640, 0, 0)
car_right = car('blue', 1050, 640, 0, 0)
cars_ord = [ car('brown', 330+60*rnd(1,15), -100-130*rnd(1,100), 0, 20) for i in range(1, 300+1)]
out_left = out(300, 400, 800, 4)
out_right = out(1200, 400, 800, 4)

#заставка
t0 = time.time()
lost_time = 0
car_left.distance = 0
car_right.distance = 0
com_text_distance_1 = canv.create_text((0 + 300) / 2 + 70, (700 + 800) / 2 - 40, text=str(car_left.distance), font="Verdana 14",
									  fill='black')
com_text_distance_2 = canv.create_text((1200 + 1500) / 2 + 70, (700 + 800) / 2 - 40, text=str(car_right.distance), font="Verdana 14",
									  fill='black')

new_game()

#результат
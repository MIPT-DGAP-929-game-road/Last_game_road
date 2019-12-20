from tkinter import *
from random import randrange as rnd, choice
 
root = Tk()
root.geometry('1500x800+0+0')
 
canv = Canvas(bg='white')
canv.pack(fill=BOTH,expand=1)

#---------------------------------------------------------------menu_itself------------------------------------------------------------------------------------------- 
enter_exam = 0
number = 1

def intro():
	print('intro')

def last_instruction():
	print('instruction')

def last_train():
	print('last_train')

def last_play():
	print('last_play')

def last_results():
	print('last_results')

def last_skins():
	print('last_skins')

def last_settings():
	print('last_settings')

def menu():
	global button, number, inf_num, button_exit, button_text, button_text_show, enter_exam
	font = canv.create_rectangle(0,0,1500,800, fill='orange')
	road = canv.create_rectangle(300,0,1200,800, fill='gray')

	menu_label = canv.create_rectangle(550,25,950,125, fill='orange')
	canv.create_text((550+950)/2, (25+125)/2, text='GAME STRUCTURE', justify=CENTER, font="Verdana 30", fill='black')

	button = []
	button_text = []
	button_text_show = ['instruction','alone training','two players game','table of results','skin changing','settings']
	inf_num = len(button_text_show)
	for i in range(0,inf_num+1): 
		button.append(0)
		button_text.append(0)
	for i in range(1,inf_num+1): 
		if i == number:
			button[i] = canv.create_rectangle(600,130+(i-1)*50,900,180+(i-1)*50, fill='blue', outline='orange')
			button_text[i] = canv.create_text((600+900)/2, (130+180)/2+(i-1)*50, text=button_text_show[i-1], justify=CENTER, font="Verdana 14", fill='orange')
		else:
			button[i] = canv.create_rectangle(600,130+(i-1)*50,900,180+(i-1)*50, fill='orange')
			button_text[i] = canv.create_text((600+900)/2, (130+180)/2+(i-1)*50, text=button_text_show[i-1], justify=CENTER, font="Verdana 14", fill='black')

	if number ==inf_num+1:
		button_exit = canv.create_rectangle(600,130+(inf_num)*50,900,180+(inf_num)*50, fill='purple', outline='white')
		text_exit = canv.create_text((600+900)/2, (130+180)/2+(inf_num)*50, text='exit', justify=CENTER, font="Verdana 14", fill='white')
	else:
		button_exit = canv.create_rectangle(600,130+(inf_num)*50,900,180+(inf_num)*50, fill='orange')
		text_exit = canv.create_text((600+900)/2, (130+180)/2+(inf_num)*50, text='exit', justify=CENTER, font="Verdana 14", fill='black')
	
def keypress_menu(event):
	global button, number, inf_num, button_exit, button_text, button_text_show, enter_exam, num_exit
	global window_exit, question_exit, exit_yes, exit_no
	print(event.keycode, number)

	if enter_exam == 0:
		if event.keycode == 38:
			number -= 1
		if event.keycode == 40:
			number += 1
		if number == 0:
			number = 1
		if number == inf_num+2:
			number = inf_num+1

		if number ==inf_num+1:
			button_exit = canv.create_rectangle(600,130+(inf_num)*50,900,180+(inf_num)*50, fill='purple', outline='white')
			text_exit = canv.create_text((600+900)/2, (130+180)/2+(inf_num)*50, text='exit', justify=CENTER, font="Verdana 14", fill='white')
		else:
			button_exit = canv.create_rectangle(600,130+(inf_num)*50,900,180+(inf_num)*50, fill='orange')
			text_exit = canv.create_text((600+900)/2, (130+180)/2+(inf_num)*50, text='exit', justify=CENTER, font="Verdana 14", fill='black')
		
		for i in range(1,inf_num+1): 
			if i == number:
				button[i] = canv.create_rectangle(600,130+(i-1)*50,900,180+(i-1)*50, fill='blue', outline='orange')
				button_text[i] = canv.create_text((600+900)/2, (130+180)/2+(i-1)*50, text=button_text_show[i-1], justify=CENTER, font="Verdana 14", fill='orange')
			else:
				button[i] = canv.create_rectangle(600,130+(i-1)*50,900,180+(i-1)*50, fill='orange')
				button_text[i] = canv.create_text((600+900)/2, (130+180)/2+(i-1)*50, text=button_text_show[i-1], justify=CENTER, font="Verdana 14", fill='black')
		
		if event.keycode == 13:
			print(number,"use enter")
			enter_exam = number
			if number < inf_num+1 and number >= 1:
				canv.create_text(50, 50+20*number, text=str(number)+'пока так', font="Verdana 16", fill='black')
				if number == 1:
					last_instruction()
				if number == 2:
					last_train()
				if number == 3:
					last_play()
				if number == 4:
					last_results()
				if number == 5:
					last_skins()
				if number == 6:
					last_settings()
			if number == inf_num+1:
				window_exit = canv.create_rectangle(500,200,1000,500, fill='purple', outline='white')
				question_exit = canv.create_text((500+1000)/2, 200+(500-200)/3, text='Are you sure wanna out?', justify=CENTER, font="Verdana 16", fill='white')
				exit_yes = canv.create_text(500+(-500+1000)/3, 200+(500-200)*2/3, text='YES', justify=CENTER, font="Verdana 16", fill='white')
				exit_no = canv.create_text(500+(-500+1000)*2/3, 200+(500-200)*2/3, text='NO', justify=CENTER, font="Verdana 16", fill='white')
				num_exit = 0
		event.keycode = 0
		print('enter_exam',enter_exam)
	if enter_exam != 0:
		if number < inf_num+1 and number >= 1:
			enter_exam = 0
		if number == inf_num+1:
			if event.keycode == 37:
				num_exit = 1
			if event.keycode == 39:
				num_exit = 2
			if num_exit == 1:
				exit_yes = canv.create_text(500+(-500+1000)/3, 200+(500-200)*2/3, text='YES', justify=CENTER, font="Verdana 16", fill='orange')
				exit_no = canv.create_text(500+(-500+1000)*2/3, 200+(500-200)*2/3, text='NO', justify=CENTER, font="Verdana 16", fill='white')
			if num_exit == 2:
				exit_yes = canv.create_text(500+(-500+1000)/3, 200+(500-200)*2/3, text='YES', justify=CENTER, font="Verdana 16", fill='white')
				exit_no = canv.create_text(500+(-500+1000)*2/3, 200+(500-200)*2/3, text='NO', justify=CENTER, font="Verdana 16", fill='orange')
			if event.keycode == 13:
				enter_exam = 2*enter_exam
				if num_exit == 1:
					root.quit()
				if num_exit == 2:
					number = inf_num + 1
					enter_exam = 0
					i = 6
					button[i] = canv.create_rectangle(600,130+(i-1)*50,900,180+(i-1)*50, fill='orange')
					button_text[i] = canv.create_text((600+900)/2, (130+180)/2+(i-1)*50, text=button_text_show[i-1], justify=CENTER, font="Verdana 14", fill='black')
					canv.delete(window_exit, question_exit, exit_yes, exit_no)	
		event.keycode = 0
		print('enter_exam', enter_exam)

#--------------------------------------------------------------------------------------------------------------------------
intro()	
menu()
root.bind('<Key>',keypress_menu)
mainloop()
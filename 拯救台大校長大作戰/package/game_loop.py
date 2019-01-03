import logging
import pygame
import time
import random  
import os
import math
##################################      for Stage1        #####################################
#def stage1():



##################################      for Stage2        #####################################
os.chdir('D:/PBC') #package資料夾所在目錄
from package.Class import mainCharacter,obstacle,special_obstacle,figure,text
from package.Functions import set_ColorBlock,set_River,collision,correction,set_to_origin
from package import OP_ED

display_width =  1280 
display_height = 960    
gameDisplay = pygame.display.set_mode((display_width, display_height))   
clock = pygame.time.Clock()
def stage2():
	#Opening_Trailer()
	## play song
	## https://nerdparadise.com/programming/pygame/part3
	print("play music")
	pygame.mixer.music.load("下一站茶山劉.mp3")
	wave=pygame.mixer.Sound("wave.wav")
	pygame.mixer.music.play(-1)
	riverDisplay = pygame.Surface((1280,960)) #建立一個river圖層
	black = (0, 0, 0)
	white = (255, 255,255)
	red = (255,0,0)
	blue0=(149,220,255)
	blue1=(138,208,255)
	blue2=(128,197,253)
	Colorlist=[blue0,blue1,blue2]

## load wave sound and background music in pygame
	pygame.mixer.music.load("下一站茶山劉.mp3")
	wave=pygame.mixer.Sound("wave.wav")
	##uploading image of boats
	boatImg0 = pygame.image.load("boat.png") 
	boatImg1 = pygame.image.load("boat1.png")
	boatImg2 = pygame.image.load("boat2.png")
	boatImgList=[boatImg0,boatImg1,boatImg2]
	
	# uploading other obstacles
	bikeImg = pygame.image.load("bike.png")
	peopleImg = pygame.image.load("people.png")	

	bike2Img = pygame.image.load("bike2.png")
	busImg = pygame.image.load("bus.png")
	catImg = pygame.image.load("cat.png")
	dogImg = pygame.image.load("dog.png")
	fishImg = pygame.image.load("fish.png")
	dinoImg = pygame.image.load("dino.png")
	rainbowcatImg = pygame.image.load("rainbowcat.png")  
	busImg = pygame.transform.scale(busImg, (192*3, 192))


	# uploading other Images
	gpaImg = pygame.image.load("GPA.png")
	hpbarImg = pygame.image.load("HPbar.png")
	endlineImg = pygame.image.load("endline.png")
	backgroundImg = pygame.image.load("background.png")
	backgroundImg = pygame.transform.scale(backgroundImg, (480, 320))
	startoImg = pygame.image.load("starto.png")
	startoImg = pygame.transform.scale(startoImg, (580, 240))

	# defining Objects

	#define background
	background = figure(0,0,480,320)
	background2 = figure(480,0,480,320)
	background3 = figure(960,0,480,320)
	background4 = figure(1440,0,480,320)
	# main character objects
	boat = mainCharacter(display_width*0.1 , display_height*0.75 , 96 , 96 )  #set status of object

	# obstacle objects
	# special_obstacle (self,x,y,width,height,movespeed_x,movespeed_y,damage):
	## setting initial velocity for x and y
	bike2 = special_obstacle(2500,random.randrange(display_height*320/960, display_height*1-96),96,96,-10,0,-0.1) # speed: -10
	people = special_obstacle(2000,random.randrange(display_height*320/960,display_height*1-96),96,96,-7,0,-0.4) # speed: -7
	bike = special_obstacle(1280,random.randrange(display_height*320/960,display_height*1-96),96,96,-14,0,-0.1)	
	bus = special_obstacle(7000,random.randrange(display_height*320/960,display_height*1-96),192*3,192,-20,0,-0.1)# 等等要設成頁面寬	
	cat = special_obstacle(3000,random.randrange(display_height*320/960,display_height*1-96),96,96,-14,0,-0.01)
	dog = special_obstacle(4000,random.randrange(display_height*320/960,display_height*1-96),96,96,-14,0,-0.01)
	fish = special_obstacle(5000,random.randrange(display_height*320/960,display_height*1-96),96,96,-10,random.choice([-25,25]),-0.05)# 往左移10，往上移10，等等可以設random
	dino = special_obstacle(6000,random.randrange(display_height*320/960,display_height*1-96),96,96,-14,random.choice([-20,20]),-0.2)
	rainbowcat = special_obstacle(30000,random.randrange(display_height*320/960,display_height*1-144),144,144,(-1280/10),0,0)
	# rainbow_cat 144*144


	# figure / text objects	
	gpa_icon=figure(30,50,96,96)
	GPA=4.3
	now_gpa=text(str(GPA),60,black,gpa_icon.width+96,gpa_icon.height) 	
	## create ending object
	ending_message=text("You have failed your semester!",80,red,display_width*(1/2),display_height*(2/3))
	
	## create clock now_time on right upper corner.
	now_time=text(str(0.0),60,black,display_width,0)


	## create ending object of game 
	endline=obstacle(display_width,display_height*(1/3),100,display_height*2/3,-4) # width 暫設50 px 

	#obstacle list	
	obstaclelist=[bike,bike2,people,bus,cat,dog,fish,dino,rainbowcat]   


	starto=figure(350,450,192,96)

	x_change = 0 #set constent
	y_change = 0	
	# dodged=0  ## dodged ; congratulating on dodge??	
	boatImgNum=0	#控制 boat gif fps
	frame=0 #初始幀數


	# for collision ; 預設flash 的狀態是false
	flash=False
	collision_time = 0
	for frame in range(6):
		background.set(backgroundImg)
		background2.set(backgroundImg)
		background3.set(backgroundImg)
		background4.set(backgroundImg)
		set_River(riverDisplay,20,20,Colorlist)
		gameDisplay.blit(riverDisplay, (0,320))
		boat.set(boatImg0)
		if frame % 2 == 0:
			starto.set(startoImg)
		pygame.display.update()	
		time.sleep(0.2)
	
### initial_time
	time_running=0
### game exit while loop
	gameExit = False
	
	while not gameExit:
		
		frame+=1 #每跑一次while迴圈幀數+1
		###########event handling loop###########
		for event in pygame.event.get():    #it gets any event that happens...movenment of mouse or clicking etc
			

			if event.type == pygame.QUIT:   # when we will click X it will quit the window
				logging.info("X is pressed, will quit")
				pygame.quit()
				quit()

			################This event will handle situation when ever any key will be pressed ##################################
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:#pressing left arrow will decrease x-axis coordinate
					x_change = -15
					wave.play()
					
				if event.key == pygame.K_RIGHT:#pressing right arrow will increase x-axis coordinate
					x_change = 15
					wave.play()
					
				if event.key == pygame.K_UP:#pressing UP arrow will decrease Y-axis coordinate
					y_change = -15
					wave.play()

				if event.key == pygame.K_DOWN:#pressing Down arrow will increase x-axis coordinate
					y_change = 15
					wave.play()
					
			################This event will handle situation when ever any key will be released ##################################
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					y_change = 0

		
		boat.x += x_change
		boat.y += y_change


		
		gameDisplay.fill(white)
		
		background.set(backgroundImg)
		background.x-=5
		if background.x < -480:
			background.x =1280
		background2.set(backgroundImg)
		background2.x-=5
		if background2.x < -480:
			background2.x =1280
		background3.set(backgroundImg)
		background3.x-=5
		if background3.x < -480:
			background3.x =1280
		background4.set(backgroundImg)
		background4.x-=5
		if background4.x < -480:
			background4.x =1280
			
		if frame % 20 == 1:				#將river set在 riverDisplay圖層上(每10幀改變一次riverDisplay樣貌)
			set_River(riverDisplay,20,20,Colorlist)	
		gameDisplay.blit(riverDisplay, (0,320)) #再將riverDisplay放在gameDisplay圖層
		
		'''
		#####################將boatImg 組成gif 並設定幾次畫面(frame)更新會換下一張###################
		if boatImgNum!=2:                                  
			set_MainCharacter(boat,boatImgList[boatImgNum])
			if frame % 10 == 0:     #每10幀數換下一張圖片
				boatImgNum += 1

		elif boatImgNum==2:
			set_MainCharacter(boat,boatImgList[boatImgNum])
			if frame % 10 == 0:
				boatImgNum = 0
		'''
		

		## setting obstacles moving speed and directions between each flip
		bike.set(bikeImg)
		bike.x += bike.movespeed
		bike.y += bike.movespeed_y

		people.set(peopleImg)
		people.x += people.movespeed
		people.y += people.movespeed_y

		## setting other objects
		bus.set(busImg)
		bus.x += bus.movespeed
		bus.y += bus.movespeed_y

		cat.set(catImg)		
		cat.x += cat.movespeed
		cat.y += cat.movespeed_y

		dog.set(dogImg)
		dog.x+= dog.movespeed
		dog.y+= dog.movespeed_y

		fish.set(fishImg)
		fish.x+= fish.movespeed
		fish.y+= fish.movespeed_y

		dino.set(dinoImg)
		dino.x += dino.movespeed
		dino.y += dino.movespeed_y

		rainbowcat.set(rainbowcatImg)
		rainbowcat.x += rainbowcat.movespeed
		rainbowcat.y += rainbowcat.movespeed_y



		##  correction of objects to adhere to boundaries ; 
		correction(boat,320/960)  ## 界線是設在1/3，太低可以之後再調



		if fish.y < display_height*320/960:
			fish.y = display_height*320/960
		elif fish.y > display_height:
			fish.y = display_height
		
		if dino.y < display_height*320/960:
			dino.y = display_height*320/960
		elif dino.y > display_height:
			dino.y = display_height

		## altering movespeed_x,movespeed_y for every loop
		## 每經過一輪的blit，speed要不要條整; x,y 都可以調整，現在還沒有調整

		# set_to_origin(objects,change_speed_x,change_speed_y)
		
		set_to_origin(bike,0.02,0)
		set_to_origin(people,0.01,0)
		set_to_origin(bus,0.07,0)
		set_to_origin(cat,0.01,0)
		set_to_origin(dog,0.01,0)
		set_to_origin(fish,0.01,0)
		set_to_origin(dino,0.1,0)


		#根據gpa 每0.5顯示一格hpbar
		# figure(self,x,y,width,height):
		for i in range(0,int(math.floor(float(now_gpa.content)/0.5))):
			hpbar = figure( gpa_icon.x+50*(i+1) , gpa_icon.y , 96 , 96)
			hpbar.set(hpbarImg)
			
		gpa_icon.set(gpaImg)			
		now_gpa.set("None")
		

		## flash setting when collide
		
		if flash == False: 
			if boatImgNum!=2:                                  
				boat.set(boatImgList[boatImgNum])
				if frame % 10 == 0:     #每10幀數換下一張圖片
					boatImgNum += 1

			elif boatImgNum==2:
				boat.set(boatImg0)
				if frame % 7 == 0:
					boatImgNum = 0

		elif flash == True:

			collision_time+=clock.get_time()

			if frame%10 == 0:
				boat.set(random.choice(boatImgList))

		if (collision_time/1000) >=3: ## if 超過3s
			flash = False
		



		## collision method 2 ; setting damage numbers
		for obstacles in obstaclelist:
			#def collision(object1,object2):
			if collision(boat,obstacles)==True:
				'''
				changed_gpa="%-10.2f"%(float(now_gpa.content)+obstacles.damage) ## damage目前是-0.1
				now_gpa.content=str(changed_gpa)
				flash = True
				'''
				if flash==False:
					changed_gpa="%-10.2f"%(float(now_gpa.content)+obstacles.damage) ## damage目前是-0.1
					now_gpa.content=str(changed_gpa)
				elif flash==True:
					continue

				flash = True				


				

		## GPA adjusting

		if float(now_gpa.content)<=0:
			## stop music
			now_gpa.content = 0
			pygame.mixer.music.stop()
			#display message
			ending_message.set("Center")
			pygame.display.update()
			print("printed ending message")
			time.sleep(2)
			OP_ED.Failure_screen()
			stage2()
			
		if float(now_gpa.content)<2.5:
			now_gpa.color=red
		else:
			now_gpa.color=black

		if float(now_gpa.content) > 4.3:
			now_gpa.content = 4.3
		


		## if crossed endline
		if collision(boat,endline):
			pygame.quit()
			quit()


		## set time on right upper field
		now_time.set("Right")
		dt=clock.tick(60)/1000
		time_running += dt
		now_time.content="%-10.1f"%(time_running)

		print("Game has run for ",time_running," seconds")
		#print("get_ticks is running for",float(pygame.time.get_ticks()/1000)," seconds")




		if time_running>50:
			now_time.color=red
			print("Clock turned red.......")

		now_time.set("Right")


		# endline=obstacle(display_width,display_height*(1/3),100,display_height*2/3,-4) # width 暫設50 px 
		if (time_running)>=30.0: # >60s 就讓最後一條線進來，撐過一分鐘就成功
			print("endline is appearing................")
			endline.set(endlineImg)
			#endline.x += endline.movespeed
			if endline.x <= display_width/2:
				endline.x = display_width/2
			else:
				endline.x += endline.movespeed



		## updating pygame display

		pygame.display.update()
		clock.tick(60)  ## update 60 frames per second

		
		
		
		
		
		
		
		
		
		
		
		
		
##################################      for Stage3        #####################################
#def stage3():




























import os
import logging
import pygame
import time
import random  
import os
import math
os.chdir('D:/PBC')
from package.Class import mainCharacter,obstacle,special_obstacle,figure,text
from package.game_loop import stage2

display_width =  1280 
display_height = 960    
gameDisplay = pygame.display.set_mode((display_width, display_height))    
black = (0, 0, 0)
white = (255, 255,255)
red = (255,0,0)
blue0=(149,220,255)
blue1=(138,208,255)
blue2=(128,197,253)
clock = pygame.time.Clock()
##################################      for Stage1        #####################################
def Opening_Trailer1():

	stage1 = obstacle(1280,180,192,96,-30)
	bellreal = obstacle (1280+500,265,192,96,-30)
	
	button2 = figure(720,510,192,96)
	OP_background = figure(0,0,1280,960)
	startText= text('press Space to start',20,red,640,780)
	introText=text('Press Space with the beat when the light turn on!',28,black,420,600)
	
	stage1Img = pygame.image.load("stage1.png") 
	stage1Img = pygame.transform.scale(stage1Img, (500, 400))
	bellImg = pygame.image.load("bell.png")
	bellImg = pygame.transform.scale(bellImg, (400, 240))
	button2Img = pygame.image.load("button2.png") 
	button2Img = pygame.transform.scale(button2Img, (450, 215))
	OP_backgroundImg = pygame.image.load("OP_background.png")
	OP_backgroundImg = pygame.transform.scale(OP_backgroundImg, (1280, 960))
	
	ExitOT = False
	Start_Play = True
	logging.info("start loop")
	
	while not ExitOT:	
	
		for event in pygame.event.get():    #it gets any event that happens...movenment of mouse or clicking etc
			
			if event.type == pygame.QUIT:   # when we will click X it will quit the window
				logging.info("X is pressed, will quit")
				pygame.quit()
				quit()

			################This event will handle situation when ever any key will be released ##################################
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					Start_Play = False


		
		OP_background.set(OP_backgroundImg)	
		
		stage1.set(stage1Img)
		bellreal.set(bellImg)
		stage1.x += stage1.movespeed
		bellreal.x += bellreal.movespeed

		if stage1.x < 200 and Start_Play == True:

			stage1.movespeed =0
			bellreal.movespeed=0
			button2.set(button2Img)
			startText.set('Center')
			introText.set('Center')
			
		elif Start_Play == False: #如果按下空白建 Start_Play 就會變成 False
			stage1.movespeed = -30
			bellreal.movespeed=-30
			if stage1.x  < -1280:
					ExitOT = True
		
		pygame.display.update()
		
def	Failure_screen1():
	failText = text('Try again? ',20,red,640,380)
	YNText = text('press Y/N',20,red,640,780)
	gameover = False
	gameReset = False
	while True:	
		gameDisplay.fill(black)	
		failText.set('Center')
		YNText.set('Center')
		for event in pygame.event.get():    #it gets any event that happens...movenment of mouse or clicking etc
			
			if event.type == pygame.QUIT:   # when we will click X it will quit the window
				logging.info("X is pressed, will quit")
				pygame.quit()
				quit()

			################This event will handle situation when ever any key will be released ##################################
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_n:
					gameover = True
				if event.key == pygame.K_y:
					gameReset = True
		if gameover == True:
			pygame.quit()
			quit()
		if gameReset == True:
			stage2()
			
		pygame.display.update()

##################################      for Stage2        #####################################

def Opening_Trailer2():

	stage2 = obstacle(1280,180,192,96,-30)
	ZhoushanRiver = obstacle (1280+500,265,192,96,-30)
	
	button = figure(720,510,192,96)
	OP_background = figure(0,0,1280,960)
	startText= text('press Space to start',20,red,640,780)
	introText=text('Dodge all the three treasures!',28,black,420,600)
	
	stage2Img = pygame.image.load("stage2.png") 
	stage2Img = pygame.transform.scale(stage2Img, (500, 400))
	ZhoushanRiverImg = pygame.image.load("ZhoushanRiver.png")
	ZhoushanRiverImg = pygame.transform.scale(ZhoushanRiverImg, (400, 240))
	buttonImg = pygame.image.load("button.png") 
	buttonImg = pygame.transform.scale(buttonImg, (450, 215))
	OP_backgroundImg = pygame.image.load("OP_background.png")
	OP_backgroundImg = pygame.transform.scale(OP_backgroundImg, (1280, 960))
	
	ExitOT = False
	Start_Play = True
	logging.info("start loop")
	
	while not ExitOT:	
	
		for event in pygame.event.get():    #it gets any event that happens...movenment of mouse or clicking etc
			
			if event.type == pygame.QUIT:   # when we will click X it will quit the window
				logging.info("X is pressed, will quit")
				pygame.quit()
				quit()

			################This event will handle situation when ever any key will be released ##################################
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					Start_Play = False


		
		OP_background.set(OP_backgroundImg)	
		
		stage2.set(stage2Img)
		ZhoushanRiver.set(ZhoushanRiverImg)
		stage2.x += stage2.movespeed
		ZhoushanRiver.x += ZhoushanRiver.movespeed

		if stage2.x < 200 and Start_Play == True:

			stage2.movespeed =0
			ZhoushanRiver.movespeed=0
			button.set(buttonImg)
			startText.set('Center')
			introText.set('Center')
			
		elif Start_Play == False: #如果按下空白建 Start_Play 就會變成 False
			stage2.movespeed = -30
			ZhoushanRiver.movespeed=-30
			if stage2.x  < -1280:
					ExitOT = True
		
		pygame.display.update()
		
def	Failure_screen():
	failText = text('Try again? ',20,red,640,380)
	YNText = text('press Y/N',20,red,640,780)
	gameover = False
	gameReset = False
	while True:	
		gameDisplay.fill(black)	
		failText.set('Center')
		YNText.set('Center')
		for event in pygame.event.get():    #it gets any event that happens...movenment of mouse or clicking etc
			
			if event.type == pygame.QUIT:   # when we will click X it will quit the window
				logging.info("X is pressed, will quit")
				pygame.quit()
				quit()

			################This event will handle situation when ever any key will be released ##################################
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_n:
					gameover = True
				if event.key == pygame.K_y:
					gameReset = True
		if gameover == True:
			pygame.quit()
			quit()
		if gameReset == True:
			stage2()
			
		pygame.display.update()

##################################      for Stage3        #####################################		
def Opening_Trailer3():

	stage3 = obstacle(1280,180,192,96,-30)
	ZhoushanRiver = obstacle (1280+500,265,192,96,-30)
	
	button = figure(720,510,192,96)
	OP_background = figure(0,0,1280,960)
	startText= text('press Space to start',20,red,640,780)
	introText=text('Dodge all the three treasures!',28,black,420,600)
	
	stage3Img = pygame.image.load("stage3.png") 
	stage3Img = pygame.transform.scale(stage3Img, (500, 400))
	ZhoushanRiverImg = pygame.image.load("ZhoushanRiver.png")
	ZhoushanRiverImg = pygame.transform.scale(ZhoushanRiverImg, (400, 240))
	buttonImg = pygame.image.load("button.png") 
	buttonImg = pygame.transform.scale(buttonImg, (450, 215))
	OP_backgroundImg = pygame.image.load("OP_background.png")
	OP_backgroundImg = pygame.transform.scale(OP_backgroundImg, (1280, 960))
	
	ExitOT = False
	Start_Play = True
	logging.info("start loop")
	
	while not ExitOT:	
	
		for event in pygame.event.get():    #it gets any event that happens...movenment of mouse or clicking etc
			
			if event.type == pygame.QUIT:   # when we will click X it will quit the window
				logging.info("X is pressed, will quit")
				pygame.quit()
				quit()

			################This event will handle situation when ever any key will be released ##################################
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					Start_Play = False


		
		OP_background.set(OP_backgroundImg)	
		
		stage3.set(stage3Img)
		ZhoushanRiver.set(ZhoushanRiverImg)
		stage3.x += stage3.movespeed
		ZhoushanRiver.x += ZhoushanRiver.movespeed

		if stage3.x < 200 and Start_Play == True:

			stage3.movespeed =0
			ZhoushanRiver.movespeed=0
			button.set(buttonImg)
			startText.set('Center')
			introText.set('Center')
			
		elif Start_Play == False: #如果按下空白建 Start_Play 就會變成 False
			stage3.movespeed = -30
			ZhoushanRiver.movespeed=-30
			if stage3.x  < -1280:
					ExitOT = True
		
		pygame.display.update()
		
def	Failure_screen3():
	failText = text('Try again? ',20,red,640,380)
	YNText = text('press Y/N',20,red,640,780)
	gameover = False
	gameReset = False
	while True:	
		gameDisplay.fill(black)	
		failText.set('Center')
		YNText.set('Center')
		for event in pygame.event.get():    #it gets any event that happens...movenment of mouse or clicking etc
			
			if event.type == pygame.QUIT:   # when we will click X it will quit the window
				logging.info("X is pressed, will quit")
				pygame.quit()
				quit()

			################This event will handle situation when ever any key will be released ##################################
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_n:
					gameover = True
				if event.key == pygame.K_y:
					gameReset = True
		if gameover == True:
			pygame.quit()
			quit()
		if gameReset == True:
			stage2()
			
		pygame.display.update()

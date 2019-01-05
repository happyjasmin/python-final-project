

import os
import pygame
from pygame.locals import *
import time
import numpy
import sched
import threading


os.chdir('/Volumes/drive/course/107winter/商管程式設計/final progect/python-final-project/Stage1-music')

pygame.init()

width,height = 1280, 960
screen = pygame.display.set_mode((width,height))

	
pygame.mixer.init()


# 物件圖片
bell  	= pygame.image.load("object/bell.png")
bell = pygame.transform.scale(bell,(250,250))

bell_m 	= pygame.image.load("object/bell_miss.png")
bell_g 	= pygame.image.load("object/bell_good.png")
play	= pygame.image.load("object/play.png")
#
space 	= pygame.image.load("object/space.png")
press	= pygame.image.load("object/press.png")

#fail	= pygame.image.load("object/gameover.png")

pas	    = pygame.image.load("object/pass.png")

sky 	= pygame.image.load("object/sky.png")
background 	= pygame.image.load("object/fubell.png")


#調整大小
#fail = pygame.transform.scale(fail,(100,100))

bell_m = pygame.transform.scale(bell_m,(250,250))
bell_g = pygame.transform.scale(bell_g,(250,250))

play = pygame.transform.scale(play,(500,500))
space = pygame.transform.scale(space,(400,50))
press = pygame.transform.scale(press,(400,50))

#gpa
gpapic = pygame.image.load("object/GPA.png")
hpbar = pygame.image.load("object/HPbar_2.png")

#加聲音
hit  = pygame.mixer.Sound("sound/correct.wav")
crash = pygame.mixer.Sound("sound/wrong.wav")
song = pygame.mixer.music.load("sound/ntu.mp3")


hit.set_volume(50)
crash.set_volume(50)

#WASD按鍵狀況記錄
keys = False


#hint
def HINT():
	screen.fill(0)
	music = press
	screen.blit(sky, (0,0))
	screen.blit(background, (100,65))
	screen.blit(button,(540,158))
	screen.blit(music, (474,530))
	screen.blit(life, (30,100))
	screen.blit(hpbar,(20,10))
	screen.blit(gpapic,(0,0))
	pygame.display.flip()

def HINT2():
	screen.fill(0)
	music = space
	screen.blit(sky, (0,0))
	screen.blit(background, (100,65))
	screen.blit(button,(540,158))
	screen.blit(music, (474,530))
	screen.blit(life, (30,100))
	screen.blit(hpbar,(20,10))
	screen.blit(gpapic,(0,0))
	pygame.display.flip()


		
#要按的秒數
mints = [30.68,33.48,36.23,39.28,42.18,45.08,47.43,49.28,51.08,54.93,57.73,60.18,63.53,66.03,68.43,70.98,74.23,77.33,79.93,82.83,85.43]

mints = numpy.array(mints)

		
# 歌詞
lyric =("　　　　　　　　　　　　　　　　　　　　　"

		"　　　　　　　　　　　　　　　　　　　　　"
		
		"　　　　　　　　　　　　　　　　　　　　　"
		"""
		"　　　　　　　　　　　　　　　　　　　　　"
		
		"　　　　　　　　　　　　　　　　　　　　　"

		"　　　　　　　　　　　　　　　　　　　　　"
		
		"　　　　　　　　　　　　　　　　　　　　　"
		"""
		"　　　　　　　　　　　　　　　　　　　　　"
		
		"臺大的環境　鬱鬱蔥蔥　臺大的氣象　勃勃蓬蓬 "

		"遠望那玉山突出雲表　正象徵我們目標的高崇 "

		"近看蜿蜒的淡水　他不捨晝夜地流動 "

		"正顯示我們百折不撓的作風　這百折不撓的作風 "

		"定使我們　一切事業都成功")

fin = False
	
while not(fin):

	#使用者未按任何按鍵的預設狀態
	music 	= play
	gamestart = False
	makechoice=0
	hpbarlen=430
	hpbar = pygame.transform.scale(hpbar,(hpbarlen,50))
	fin = False

	#是否點擊play/stop
	clickbutton = False
	
	#是否在撥放音樂 
	playing = False
	
	#gpa
	gpa = 4.3
	font = pygame.font.Font(None, 50)
	life = font.render(str("GPA :")+str("%.1f" %gpa),True,  (255, 255, 255))
	textRect = life.get_rect()
	
	
	#指定中文字體
	fontc = pygame.font.Font("/System/Library/Fonts/STHeiti Medium.ttc",50)
	runninglyr = fontc.render(lyric, True, (0, 0, 0))
	#字開始出現的位置
	x = 480

	#偵測玩家是否按下play
	while not(gamestart):
	
		button = bell
		screen.fill(0)		
		screen.blit(sky, (0,0))
		screen.blit(background, (100,65))
		screen.blit(button,(540,158))
		screen.blit(music, (378,303))
			

		pygame.display.flip()
		
		
			
		for event in pygame.event.get() :
			
			if event.type == pygame.QUIT :
				
				pygame.quit()
				exit()
					
			#偵測是否有按滑鼠，與是否有按在"play"上		
			if event.type == pygame.MOUSEBUTTONDOWN and 378 <= event.pos[0] <= (500+378) and 303 <= event.pos[1] <= (500+303) :
				
				clickbutton = True
				playing = True

				
		#如果點play，則遊戲要開始了
		if clickbutton and playing:	

			pygame.mixer.music.play()

			music = space
			clickbutton = False
			playing = False
			gamestart = True

			start = time.time()

			break

			
	#hint設定
	if gamestart and gpa >0:
		
		screen.fill(0)
		screen.blit(sky, (0,0))
		screen.blit(background, (100,65))
		screen.blit(button,(540,158))
		screen.blit(music, (474,530))
		screen.blit(life, (30,100))
		screen.blit(hpbar,(20,10))
		screen.blit(gpapic,(0,0))
		pygame.display.flip()

		schedule = mints - 0.5

		for i in schedule:
			T = threading.Timer(i , HINT)
			T.start()
			

		schedule_end = mints + 1
		
		for i in schedule_end:
			T_b = threading.Timer(i , HINT2)
			T_b.start()



	while gamestart and gpa > 0:
	
	
		#偵測玩家是否按按鍵，按了就記錄按下的time
		for event in pygame.event.get() :
			
			#遊戲開始字幕就開始跑
			x -= 40
		
			screen.blit(runninglyr, (x, 300))
			screen.blit(runninglyr, (x + runninglyr.get_width(), 300))
		
			pygame.display.flip()
		
			if event.type == pygame.QUIT :
				
				pygame.quit()
				exit()
			
			#space按鍵狀況
			if event.type == pygame.KEYDOWN :
			
				if event.key == pygame.K_SPACE :
					keys = True

					time_click = time.time() - start
					
					time_diff = time_click - mints
					upper = set(time_diff[time_diff <= 0.25])
					lower = set(time_diff[time_diff >= -0.15])

					if len(upper & lower) == 1:
						screen.fill(0)
						life = font.render(str("GPA :")+str("%.1f" %gpa),True,  (255, 255, 255))

				
						button = bell_g
						gpa += 0.1
						hit.play()
						
						screen.blit(sky, (0,0))
						screen.blit(background, (100,65))
						screen.blit(button,(540,158))
						screen.blit(music, (474,530))
						screen.blit(life, (30,100))
						screen.blit(hpbar,(20,10))
						screen.blit(gpapic,(0,0))
			
						pygame.display.flip()

						screen.fill(0)
						life = font.render(str("GPA :")+str("%.1f" %gpa),True,  (255, 255, 255))

		
						button = bell
										
						screen.blit(sky, (0,0))
						screen.blit(background, (100,65))
						screen.blit(button,(540,158))
						screen.blit(music, (474,530))	
						screen.blit(life, (30,100))
						screen.blit(hpbar,(20,10))
						screen.blit(gpapic,(0,0))
						
						pygame.display.flip()
					
					else :
						screen.fill(0)
				
						button = bell_m
						crash.play()
						gpa -= 0.1	
						hpbarlen -= 10
						hpbar = pygame.transform.scale(hpbar,(hpbarlen,50))
						life = font.render(str("GPA :")+str("%.1f" %gpa),True,  (255, 255, 255))

						screen.blit(sky, (0,0))
						screen.blit(background, (100,65))
						screen.blit(button,(540,158))
						screen.blit(music, (474,530))
						screen.blit(life, (30,100))
						screen.blit(hpbar,(20,10))
						screen.blit(gpapic,(0,0))
						
						pygame.display.flip()

						screen.fill(0)
		
						button = bell
										
						screen.blit(sky, (0,0))
						screen.blit(background, (100,65))
						screen.blit(button,(540,158))
						screen.blit(music, (474,530))	
						screen.blit(life, (30,100))
						screen.blit(hpbar,(20,10))
						screen.blit(gpapic,(0,0))
						
						pygame.display.flip()

								
			if event.type == pygame.KEYUP :
				if event.key == pygame.K_SPACE :
					keys = False

					time_click = time.time() - start

					time_diff = time_click - mints
					upper = set(time_diff[time_diff <= 0.25])
					lower = set(time_diff[time_diff >= -0.15])

					if len(upper & lower) == 1:
							
							gpa -= 0.1
		
		if gpa < 0 :
				
			while not(makechoice) :
				for event in pygame.event.get(): 
						
					pygame.mixer.music.stop()
					fail = font.render(str("You have failed the semester, do you want to try again? (y/n)"),True,  (255, 255, 255))
						
					textRect = fail.get_rect()
					screen.fill(0)
					screen.blit(fail, (100,400))
					pygame.display.flip()
						
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_n:
							pygame.quit()
							quit()
								
						if event.key == pygame.K_y:
							makechoice = True
							gamestart = False
			
		#如果完成遊戲且gpa大於0
		if gpa > 0 and 89 <=time.time() - start <= 95:		
			fin = True
		
			gamestart = False

			
screen.fill(0)
pas = font.render(str("You have finish the semester!"),True,  (255, 255, 255))			
textRect = pas.get_rect()
screen.blit(life, (100,300))

					
life = font.render(str("GPA :")+str("%.1f" %gpa),True,  (255, 255, 255))
textRect = life.get_rect()
screen.blit(pas, (100,400))

pygame.display.flip()		
time.sleep(10)
			



screen.fill(0)				
screen.blit(pas, (500,400))
pygame.display.flip()

# music

import pygame
import time

pygame.init()

width,height=1280,960
screen = pygame.display.set_mode((width,height))

	
pygame.mixer.init()


# 物件圖片
blue  	= pygame.image.load("C:\\Users\\user\\Documents\\GitHub\\test\\Stage1-music\\blue.png")
red   	= pygame.image.load("C:\\Users\\user\\Documents\\GitHub\\test\\Stage1-music\\orange.png")
green 	= pygame.image.load("C:\\Users\\user\\Documents\\GitHub\\test\\Stage1-music\\green.png")
play	= pygame.image.load("C:\\Users\\user\\Documents\\GitHub\\test\\Stage1-music\\play.png")
stop 	= pygame.image.load("C:\\Users\\user\\Documents\\GitHub\\test\\Stage1-music\\stop.png")


#加聲音
hit  = pygame.mixer.Sound("C:\\Users\\user\\Documents\\GitHub\\test\\Stage1-music\\Air_Woosh_Underwater.wav")
song = pygame.mixer.music.load("C:\\Users\\user\\Documents\\GitHub\\test\\Stage1-music\\ntu.wav")

hit.set_volume(1)


# WASD按鍵狀況記錄
keys = [False,False,False,False]

#是否點擊play/stop
clickbutton = False

#是否在撥放音樂 
playing = False


#使用者未按任何按鍵的預設狀態
button 	= blue
music 	= play


while 1 :
	
	screen.fill(0)
	
	screen.blit(button,(0,100))
	screen.blit(button,(300,100))
	screen.blit(music, (500,500))
	
	pygame.display.flip()
	time.sleep(0.2)
	
	
	
	for event in pygame.event.get() :
		
		if event.type == pygame.QUIT :
			
			pygame.quit()
			exit()
			
		#wasd按鍵狀況
		if event.type == pygame.KEYDOWN :
		
			if event.key == pygame.K_w :
				keys[0] = True
			elif event.key ==  pygame.K_a :
				keys[1] = True
			elif event.key ==  pygame.K_s :
				keys[2] = True
			elif event.key ==  pygame.K_d :
				keys[3] = True
			
		if event.type == pygame.KEYUP :
			if event.key == pygame.K_w :
				keys[0] = False
			elif event.key == pygame.K_a :
				keys[1] = False
			elif event.key == pygame.K_s :
				keys[2] = False
			elif event.key == pygame.K_d :
				keys[3] = False

				
		#偵測是否有按滑鼠，與是否有按在"play"上		
		if event.type == pygame.MOUSEBUTTONDOWN and 500 <= event.pos[0] <= (500+351) and 500 <= event.pos[1] <= (500+153) :
			
			clickbutton = True
			playing = not(playing)
			
		
	#如果按下w			
	if keys[0] :		
	
		hit.play()
		button=red
		
	else :
		button = blue
		
	#如果點play/stop
	if clickbutton and playing:	
	
		pygame.mixer.music.play()
		music = stop
		clickbutton = False 	
	
	elif clickbutton and not(playing) :
		
		pygame.mixer.music.stop()		
		music = play
		clickbutton = False
		
		

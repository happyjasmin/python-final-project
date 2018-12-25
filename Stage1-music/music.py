# music

import pygame
import time

pygame.init()

width,height=1280,960
screen = pygame.display.set_mode((width,height))

	
pygame.mixer.init()

# WASD按鍵狀況記錄
keys = [False,False,False,False]

# 物件圖片
blue = pygame.image.load("C:\\Users\\user\\Documents\\GitHub\\test\\Stage1-music\\blue.png")
red = pygame.image.load("C:\\Users\\user\\Documents\\GitHub\\test\\Stage1-music\\orange.png")
green = pygame.image.load("C:\\Users\\user\\Documents\\GitHub\\test\\Stage1-music\\green.png")

#加聲音
hit = pygame.mixer.Sound("C:\\Users\\user\\Documents\\GitHub\\test\\Stage1-music\\Air_Woosh_Underwater.wav")
hit.set_volume(0.05)


button = blue

while 1 :
	
	screen.fill(0)
	
	screen.blit(button,(0,100))
	screen.blit(button,(300,100))
	
		
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
				
	if keys[0] :
		
		hit.play()
		button=red
	else :
		button = blue
		
		

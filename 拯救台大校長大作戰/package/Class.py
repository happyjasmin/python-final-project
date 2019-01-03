import logging
import pygame
import time
import random  
import os
import math
display_width =  1280 
display_height = 960   
gameDisplay = pygame.display.set_mode((display_width, display_height)) 
##################################      class for Stage1        #####################################


##################################      class for Stage2        #####################################  
class mainCharacter():
	def __init__(self,x,y,width,height):
		self.x=x
		self.y=y
		self.width=width
		self.height=height
	def set(self,img):
		gameDisplay.blit(img,(self.x,self.y))
		
class obstacle():
	def __init__(self,x,y,width,height,movespeed):
		self.x=x
		self.y=y
		self.width=width
		self.height=height
		self.movespeed=movespeed
	def set(self,img):
		gameDisplay.blit(img,(self.x,self.y))	

class special_obstacle(obstacle):
	def __init__(self,x,y,width,height,movespeed,movespeed_y,damage):
		super().__init__(x,y,width,height,movespeed)
		self.movespeed_y=movespeed_y
		self.damage=damage
	def set(self,img):
		gameDisplay.blit(img,(self.x,self.y))

class figure():
	def __init__(self,x,y,width,height):
		self.x=x
		self.y=y
		self.width=width
		self.height=height
	def set(self,img):
		gameDisplay.blit(img,(self.x,self.y))

## this is to display numbers in text, in this case GPA. 
class text():
	def __init__(self,content,size,color,x,y):

		self.content=content
		self.size=size
		self.color=color
		self.x=x
		self.y=y

	def set(self,position):
		now_text=pygame.font.Font("freesansbold.ttf",self.size)
		now_text=now_text.render(self.content,True,self.color)
		now_text_rect=now_text.get_rect()

		if position=="Center": ## 置中
			now_text_rect.center=(self.x-(1/2)*now_text_rect.width,self.y)
		elif position=="Right": ##如果text是在最右邊的話，要把它自己的長度扣掉，完整顯現
			now_text_rect.center=(self.x-now_text_rect.width,self.y)
		elif position=="None":  #不用管，左上角即代表x,y coordinate
			now_text_rect.center=(self.x,self.y)

		gameDisplay.blit(now_text,now_text_rect.center)
		
		
		
##################################     class for Stage3       #####################################
import logging
import pygame
import time
import random  

pygame.init()

display_width = 1280
display_height = 960
gameDisplay = pygame.display.set_mode((display_width, display_height))    #Displays(width,length)
pygame.display.set_caption('拯救台大校長大作戰')
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255,255)
block_color = ( 53, 115, 255)


class mainCharacter():
	def __init__(self,x,y,width,height,img):
		self.x=x
		self.y=y
		self.width=width
		self.height=height
		self.img=img
		
class obstacle():
	def __init__(self,x,y,width,height,movespeed,img):
		self.x=x
		self.y=y
		self.width=width
		self.height=height
		self.movespeed=movespeed
		self.img=img

def things_dodged(count):
	font = pygame.font.SysFont(None, 25)
	text = font.render("dodged" + str(count), True, black)
	gameDisplay.blit(text,(0,0))

def setObject(object):
	
	gameDisplay.blit(object.img,(object.x,object.y))

def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()
def message_display(text):
	largeText = pygame.font.Font("freesansbold.ttf", 115)#font type and size
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width/2), (display_height/2))
	gameDisplay.blit(TextSurf, TextRect)
	pygame.display.update()

	time.sleep(2)
	game_loop()


def hit(GPA):
	GPA-=0.1
	if GPA ==0 :
		message_display("Your GPA is 0")

def end():
	message_display("Your GPA is 0")





def game_loop():

	boatImg = pygame.image.load("D:/SkySpiriT/NTU/PBC/Project/boat.png")  ##uploading image
	bikeImg=pygame.image.load("D:/SkySpiriT/NTU/PBC/Project/bike.png")
	
	boat = mainCharacter(display_width*0.1 , display_height*0.75 , 10 , 10 , boatImg)  #set status of object
	bike = obstacle(500,random.randrange(display_height*280/960, display_height*1),100,100,-10,bikeImg)
	
	x_change = 0 #set constent
	y_change = 0	
	GPA=4.3
	dodged=0

	gameExit = False
	
	while not gameExit:
	###########event handling loop###########

		for event in pygame.event.get():    #it gets any event that happens...movenment of mouse or clicking etc
			if event.type == pygame.QUIT:   # when we will click X it will quit the window
				logging.info("X is pressed")
				pygame.quit()
				quit()

			################This event will handle situation when ever any key will be pressed ##################################
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:#pressing left arrow will decrease x-axis coordinate
					x_change = -7
					
				if event.key == pygame.K_RIGHT:#pressing right arrow will increase x-axis coordinate
					x_change = 7
					
				if event.key == pygame.K_UP:#pressing UP arrow will decrease Y-axis coordinate
					y_change = -7
					
				if event.key == pygame.K_DOWN:#pressing Down arrow will increase x-axis coordinate
					y_change = 7
					
			################This event will handle situation when ever any key will be released ##################################
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					logging.info("left or right arrow is pressed up")
					x_change = 0
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					logging.info("up or down arrow is pressed up")
					y_change = 0

		
		boat.x += x_change
		boat.y += y_change

		gameDisplay.fill(white)


		setObject(bike)
		bike.x += bike.movespeed
		
		setObject(boat)
		
		things_dodged(dodged)

		if boat.x > display_width - boat.width or boat.x < 0:
			end()
		if boat.y > display_height - boat.height or boat.y < 0:
			end()
			
		if bike.x < 0:
			bike.y = random.randrange(display_height*280/960, display_height)
			bike.x = 1280
			bike.movespeed -= 0.5

		###if x < bike.x + bike.width:
			
			###if y> bike.y and y< bike.y+ bike.height or y+boat_height>thing_starty and y+boat_height<thing_starty+thing_height:
				###crash()
		pygame.display.update()
		clock.tick(60)  ## it will just make thing move faster
logging.info("calling the game loop")
game_loop()
logging.info("calling the quit function")
pygame.quit()
logging.info("I am the last line of the code")
quit()
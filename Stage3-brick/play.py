# encoding: utf-8
 
import os, sys, random
import pygame 
from pygame.locals import *
 
from drew import *

from time import sleep
 
# 視窗大小.
canvas_width = 1280
canvas_height = 650
 
# 顏色.
block = (255,250,240)
 
# 磚塊數量串列.
bricks_list = []
 
# 移動速度.
dx =  7
dy = -7
 
# 遊戲狀態.
# 0:等待開球
# 1:遊戲進行中
game_mode = 0
 
#-------------------------------------------------------------------------
# 函數:秀字.
#-------------------------------------------------------------------------
def showFont( text, x, y):
    global canvas    
    text = font.render(text, 1, (255, 0, 0)) 
    canvas.blit( text, (x,y))
 
#-------------------------------------------------------------------------
# 函數:碰撞判斷.
#   x       : x 
#   y       : y 
#   boxRect : 矩形
#-------------------------------------------------------------------------
def isCollision( x, y, boxRect):
    if (x >= boxRect[0] and x <= boxRect[0] + boxRect[2] and y >= boxRect[1] and y <= boxRect[1] + boxRect[3]):
        return True;          
    return False;  
 
#-------------------------------------------------------------------------
# 函數:初始遊戲.
#-------------------------------------------------------------------------
def resetGame():
    # 宣告使用全域變數.
    global game_mode, brick_num, bricks_list, dx, dy
 
    # 磚塊
    for bricks in bricks_list:
        # 亂數磚塊顏色
        bricks.color = [227,23,13]        
        # 開啟磚塊.
        bricks.visivle = True
    # 0:等待開球
    game_mode = 0
    # 磚塊數量.
    brick_num = 120  
    # 移動速度.
    dx =  7
    dy = -7
 
# 初始.
pygame.init()
# 顯示Title.
pygame.display.set_caption(u"打磚塊遊戲")
# 建立畫佈大小.
canvas = pygame.display.set_mode((canvas_width, canvas_height))
# 時脈.
clock = pygame.time.Clock()
 
# 設定字型-黑體.
font = pygame.font.SysFont('simhei', 30)
 
# 底板.
paddle_x = 0
paddle_y = (canvas_height - 48)
paddle = Box(pygame, canvas, "paddle", [paddle_x, paddle_y, 100, 24], (0,0,0))
 
# 球.
ball_x = paddle_x
ball_y = paddle_y
ball   = Circle(pygame, canvas, "ball", [ball_x, ball_x], 8, (0,0,0))
 
# 建立磚塊
brick_num = 0
brick_x = 70
brick_y = 70
brick_w = 0
brick_h = 0
for i in range( 0, 120):
    if((i % 12)==0):
        brick_w = 0
        brick_h = brick_h + 30       
    bricks_list.append (Box(pygame, canvas, "brick_"+str(i), [  brick_w + brick_x, brick_h+ brick_y, 90, 25], [255,255,255]))
    brick_w = brick_w + 95

#初始分數
gpa=4.3
# 初始遊戲.
resetGame()

#計時
time_keep=600
 
#-------------------------------------------------------------------------    
# 主迴圈.
#-------------------------------------------------------------------------

running = True

while running:
	#---------------------------------------------------------------------
    # 判斷輸入.
    #---------------------------------------------------------------------
    for event in pygame.event.get():
        # 離開遊戲.
        if event.type == pygame.QUIT:
            running = False
        # 判斷按下按鈕
        if event.type == pygame.KEYDOWN:
            # 判斷按下ESC按鈕
            if event.key == pygame.K_ESCAPE:
                running = False
                
        # 判斷Mouse.
        if event.type == pygame.MOUSEMOTION:
            paddle_x = pygame.mouse.get_pos()[0] - 50
        if event.type == pygame.MOUSEBUTTONDOWN:
            if(game_mode == 0):
                game_mode = 1
 
    #---------------------------------------------------------------------    
    # 清除畫面.
    canvas.fill(block)
    
    # 磚塊
    for bricks in bricks_list:
        # 球碰磚塊.
        if(isCollision( ball.pos[0], ball.pos[1], bricks.rect)):
            if(bricks.visivle):                
                # 扣除磚塊.
                brick_num = brick_num -1
                # 初始遊戲.
                if(brick_num <= 0):
                    resetGame()
                    break
                # 球反彈.
                dy = -dy; 
            # 關閉磚塊.
            bricks.visivle = False
 
        # 更新磚塊.        
        bricks.update()
            
    #顯示磚塊數量.
    showFont( u"You Still Have"+str(brick_num)+u" blocks",   8, 20)
    # 秀板子.
    paddle.rect[0] = paddle_x
    paddle.update()
 
    # 碰撞判斷-球碰板子.
    if(isCollision( ball.pos[0], ball.pos[1], paddle.rect)):        
        # 球反彈.
        dy = -dy;         
            
    # 球.
    # 0:等待開球
    if(game_mode == 0):
        ball.pos[0] = ball_x = paddle.rect[0] + ( (paddle.rect[2] - ball.radius) >> 1 )
        ball.pos[1] = ball_y = paddle.rect[1] - ball.radius        
    # 1:遊戲進行中
    elif(game_mode == 1):
        ball_x += dx
        ball_y += dy
        #判斷死亡.
        if(ball_y + dy > canvas_height - ball.radius):
            game_mode = 0        
        # 右牆或左牆碰撞.
        if(ball_x + dx > canvas_width - ball.radius or ball_x + dx < ball.radius):
            dx = -dx
        # 下牆或上牆碰撞
        if(ball_y + dy > canvas_height - ball.radius or ball_y + dy < ball.radius):        
            dy = -dy
        ball.pos[0] = ball_x
        ball.pos[1] = ball_y
 
    if (time_keep>0):
	    time_keep += -1
    elif (time_keep==0):
	    gpa += (-0.1)
	    time_keep=600
	# 更新球.
    ball.update()
	#更新分數
 
    # 顯示中文.
    showFont( u"GPA "+str(round(gpa,1)), 8, 2)    
    # 更新畫面.
    pygame.display.update()
    clock.tick(60)
	
	
 
# 離開遊戲.
pygame.quit()
quit()

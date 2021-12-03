import pygame
import sys
import random
from pygame.locals import *
import time

g_interface_x = 640
g_interface_y = 480  
fpsClock = pygame.time.Clock()
gameinterface = pygame.display.set_mode((g_interface_x, g_interface_y))  
pygame.display.set_caption('Greedy Snake game')  


black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
grey = pygame.Color(150, 150, 150)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue  = pygame.Color(0, 0, 255)

snake_head = [300,300]
snake_body = [[300,300],[290,300],[280,300]]
direction = 'RIGHT'
change_to = direction
speed = 5
food_pos = [random.randrange(1, (g_interface_x//10)) * 10, random.randrange(1, (g_interface_y//10)) * 10] 
food_flag = 1
score = 0

def show_Score(choice, color, font, size):

    global score
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (g_interface_x/10, 15)
    else:
        score_rect.midtop = (g_interface_x/2, g_interface_y/2)
    gameinterface.blit(score_surface, score_rect)

def restart(color, font, size):
        restart_font = pygame.font.SysFont(font, size)
        restart_surface = restart_font.render('press SPACE to restart', True, color)
        restart_rect = restart_surface.get_rect()
        restart_rect.midtop = (g_interface_x/2, g_interface_y/1.4)
        gameinterface.blit(restart_surface, restart_rect)

def gameover():
        global score
        global red
        gameoverFont = pygame.font.SysFont('arial.ttf',54)
        gameoverSurf = gameoverFont.render('Game Over!',True,red)
        gameoverRect = gameoverSurf.get_rect()
        gameoverRect.midtop = (g_interface_x/2, g_interface_y/4)
        gameinterface.fill(black)
        gameinterface.blit(gameoverSurf, gameoverRect)
        show_Score(0,red,'times',20)
        restart(blue,'times',30)
        pygame.display.flip() # 更新視窗
        
        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    time.sleep(1) # 停留一秒
                    pygame.quit()
                

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        # 更新全域變數到初始狀態
                        global snake_head
                        global snake_body
                        global direction
                        global change_to
                        global speed
                        speed = 5
                        score = 0
                        snake_head = [300,300]
                        snake_body = [[300,300],[290,300],[280,300]]
                        direction = 'UP'
                        change_to = direction
                        time.sleep(1) # 停留一秒
                        pygame.display.update()
                        main()
                        break

class Snake():
    def __init__(self):
        pass

    def turn_around(self):
        global direction 
        global change_to 
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'
            
    
    def growing(self):
        global snake_body
        global score
        global food_flag
        snake_body.insert(0, list(snake_head))
        if snake_head[0] == food_pos[0] and snake_head[1] == food_pos[1]:
           score += 1
           food_flag = 0
        else:
           snake_body.pop()

    def moving(self):
        global direction
        global snack_pos
        if direction == 'UP':
           snake_head[1] -= 10
        if direction == 'DOWN':
           snake_head[1] += 10
        if direction == 'LEFT':
           snake_head[0] -= 10
        if direction == 'RIGHT':
           snake_head[0] += 10

class Foodandaccelerate():

    def __init__(self):
        pass

    def spawing(self):
        global food_flag
        global food_pos
        if food_flag == 0:
            food_pos = [random.randrange(1, (g_interface_x//10)) * 10, random.randrange(1, (g_interface_y//10)) * 10] 
    def accelerate(self):
        global score
        global speed
        global food_flag
        if speed <= 27 and food_flag == 0 :
        
            speed += 100
    def reset(self):
        global food_flag
        food_flag = 1

def main():
    pygame.init() # 初始化
    global change_to
    global snake_body
    global snake_head
    global food_flag

    while True:   
        gameinterface.fill(black) # 視窗顏色

        for event in pygame.event.get():   # 事件
            if  event.type == pygame.QUIT: # 按叉離開
                pygame.display.quit()
                pygame.quit()
                
            elif event.type == pygame.KEYDOWN: # 其餘按鍵
                # 按 esc 跳出遊戲
                if event.key == pygame.K_ESCAPE: 
                    pygame.quit()
                    exit(0)

            # w s a d 或 ↑ ↓ ← → 移動
                if event.key == pygame.K_UP or event.key == ord('w'):
                    change_to = 'UP'                                    # 先儲存到預計移動方向
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    change_to = 'RIGHT'
                
        snake = Snake()
        food = Foodandaccelerate()
        # 呼叫函示(確認方向、移動、吃到點伸長、更新點點位置)
        snake.turn_around()
        snake.moving()
        snake.growing()
        food.spawing()
        
        food.reset()

      
        for i in snake_body:
            pygame.draw.rect(gameinterface, white, Rect(i[0], i[1], 10, 10))


    
        pygame.draw.rect(gameinterface, red, Rect(food_pos[0], food_pos[1], 10, 10))


        # Game Over 情況
        # 撞到邊界
        if snake_head[0] < 0 or snake_head[0] > g_interface_x-10:
            gameover()
        if snake_head[1] < 0 or snake_head[1] > g_interface_y-10:
            gameover()
        # 撞到蛇身
        for block in snake_body[1:]:
            if snake_head[0] == block[0] and snake_head[1] == block[1]:
                gameover()
            show_Score(1, white, 'consolas', 20)

        # 更新視窗
        pygame.display.update()

        # 偵數( 控制難度用 )
        global speed
        food.accelerate()
        fpsClock.tick(speed)

      
if __name__ == '__main__':
    main()
    pygame.quit()
   



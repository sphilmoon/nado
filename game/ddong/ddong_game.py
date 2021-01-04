import pygame
import random
##############################################################

pygame.init()

screen_width = 640 # 
screen_height = 480 # 
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("DDONG Game")

# FPS
fps = pygame.time.Clock()
##############################################################
 
background = pygame.image.load("/Users/phil/Documents/Python/nado/game/ddong/background.png")

character = pygame.image.load("/Users/phil/Documents/Python/nado/game/ddong/mj.png")
character_rect = character.get_rect()
character_size = character_rect.size
character_width = character_size[0] # width is always 0
character_height = character_size[1] # height is always 1
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height
character_speed = 0.5

ddong = pygame.image.load("/Users/phil/Documents/Python/nado/game/ddong/ddong.png")
ddong_rect = ddong.get_rect()
ddong_size = ddong_rect.size
ddong_width = ddong_size[0] # width is always 0
ddong_height = ddong_size[1] # height is always 1
ddong_x_pos = 0
ddong_y_pos = 0
ddong_speed = 0.2

to_x = 0

running = True
while running:
    dt = fps.tick(60)
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                to_x = 0

    character_x_pos += to_x * dt 

    ddong_x_pos = random.randint(0, screen_width - ddong_width)
    ddong_y_pos += ddong_speed * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if ddong_y_pos > screen_height:
        ddong_y_pos = 0
    else:
        ddong_x_pos = random.randint(0, screen_width - ddong_width)

    # if character_x_pos > screen_width:
    #     character_x_pos = 0
    # elif character_x_pos < 0:
    #     character_x_pos = screen_width - character_width

    # collision conditions
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

    if character_rect.colliderect(ddong_rect):
    	print("You stinks, MJ! Shower time!")
    	running = False
    	
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos))
    
    pygame.display.update()

pygame.quit()
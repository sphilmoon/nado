import pygame
import random
##############################################################
# must have this parameter to run the GUI.

pygame.init()

screen_width = 640 # 
screen_height = 480 # 
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("DDONG Game")

# FPS setting.
fps = pygame.time.Clock()
##############################################################

# loading the bg image file.
background = pygame.image.load("/Users/phil/Documents/python_tutorial/nado/game/ddong/background.png")

# loading the character image file and setting the default x, y positions.
character = pygame.image.load("/Users/phil/Documents/python_tutorial/nado/game/ddong/mj.png")
character_rect = character.get_rect()
character_size = character_rect.size
character_width = character_size[0] # width is always 0
character_height = character_size[1] # height is always 1
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height
character_speed = 0.5

# loading the obstacle image file and setting the default x, y positions.
ddong = pygame.image.load("/Users/phil/Documents/python_tutorial/nado/game/ddong/ddong.png")
ddong_rect = ddong.get_rect()
ddong_size = ddong_rect.size
ddong_width = ddong_size[0] # width is always 0
ddong_height = ddong_size[1] # height is always 1
ddong_x_pos = 0
ddong_y_pos = 0
ddong_speed = 0.2

# character's movement parameter.
to_x = 0

# defining the game conditions.
running = True
while running:
    dt = fps.tick(60) # 60 ms FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

        # moves the character with user input pressing L or R arrow buttons.
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        # moves the character with user input releasing L or R arrow buttons.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                to_x = 0

    # applying FPS to the movement of character.
    character_x_pos += to_x * dt 
    
    # random x poistion of obstacle within the screen width
    # and applying FPS to the movement of obstacle.
    ddong_x_pos = random.randint(0, screen_width - ddong_width)
    ddong_y_pos += ddong_speed * dt

    # ensuring the character stays within the screen width.
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # ensuring the obstacle stays within the screen width and height.
    if ddong_y_pos > screen_height:
        ddong_y_pos = 0
    else:
        ddong_x_pos = random.randint(0, screen_width - ddong_width)

    # character is teleporting from one end to the other. 
    # if character_x_pos > screen_width:
    #     character_x_pos = 0
    # elif character_x_pos < 0:
    #     character_x_pos = screen_width - character_width

    # collision conditions.
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

    # ending the while loop if the collision occurs.
    if character_rect.colliderect(ddong_rect):
        print("You stinks, MJ! Shower time!")
        running = False
        
    # canvas conditions.
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos))
    
    pygame.display.update()

pygame.quit()
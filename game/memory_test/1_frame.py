import pygame

'''
# decompose:
1. default
2. start game
3. quit game

'''

# default
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Chimp Game")

# start game
running = True
while running:
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT:
			running = False

# quit game
pygame.quit()
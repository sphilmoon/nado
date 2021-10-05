import pygame

'''
# decompose:
1. default
2. start button
3. start game
4. quit game
'''

# colors
BLACK = (0, 0, 0) # RGB
WHITE = (255, 255, 255)

# default
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Chimp Game")

# start button
start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120)

def display_start_screen():
	# drawing a circle on the screen.
	# located at the center of the start button.
	# color is white, radius is 60, thickness is 5.
	pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)  

# start game
running = True
while running:
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT:
			running = False
	
	# background
	screen.fill(BLACK)

	# screen display
	display_start_screen()

	# updating display
	pygame.display.update()

# quit game
pygame.quit()
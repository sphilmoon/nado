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

# initiating the game
start_game = False

# default
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Chimp Game")

# start button
start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120)

def display_game_screen():
	print("Starting game...")

def display_start_screen():
	# drawing a circle on the screen.
	# located at the center of the start button.
	# color is white, radius is 60, thickness is 5.
	pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)  

def check_buttons(pos):
	global start_game
	# checking if user hit the start button.
	if start_button.collidepoint(pos):
		start_game = True # starting the game play

# start game
running = True
while running:
	click_pos = None

	# user input events
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.MOUSEBUTTONUP:
			click_pos = pygame.mouse.get_pos()
			print(click_pos)
	
	# background
	screen.fill(BLACK)

	# only displyaing the game screen when the start button is hit
	if start_game: 
		display_game_screen()
	else:
		# screen display
		display_start_screen()

	# if user clicks the any button
	if click_pos:
		check_buttons(click_pos)

	# updating display
	pygame.display.update()

# quit game
pygame.quit()

	# if click_pos:
	# 	check_buttons(click_pos)
	# 	display_start_screen()
	# 	display_game_screen()
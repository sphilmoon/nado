import pygame
from random import *

'''
# decompose:
1. default
2. start button
3. start game
4. quit game
'''

# what is global?
# what enumerate?
# what is for x, y in enumerate?
# I don't understand the elapsed time variable.

# suffle grid 5 x 9
ROWS = 5
COLUMNS = 9

# colors
BLACK = (0, 0, 0) # RGB
WHITE = (255, 255, 255) # RGB
GRAY = (50, 50, 50) # RGB

number_buttons = []
display_time = None
start_ticks = None

# setting the levels
def setup(level):
	# how long should I display?
	global display_time
	display_time = 6 - (level // 3)
	display_time = max(display_time, 3) # the max time is 3 seconds.

	# how many numbers?
	number_count = (level // 3) + 2
	number_count = min(number_count, 20) # the minimum number count is 20.

	# set up grid based on the level
	shuffle_grid(number_count)

def shuffle_grid(num_count):

	cell_size = 130 # rectangular shape for the cell
	button_size = 110 # the actual size of the numbers
	screen_left_margin = 55
	screen_top_margin = 20

	grid = [[0 for col in range(COLUMNS)] for row in range(ROWS)]

	number = 1
	while number <= num_count:
		row_idx = randrange(0, ROWS)
		col_indx = randrange(0, COLUMNS)

		if grid[row_idx][col_indx] == 0:
			grid[row_idx][col_indx] = number
			number += 1 # starting with 1.

			# x, y based on the current location.
			center_x = screen_left_margin + (col_indx * cell_size) + (cell_size / 2)
			center_y = screen_top_margin + (row_idx * cell_size) + (cell_size / 2)

			# drawing the button
			button = pygame.Rect(0, 0, button_size, button_size)
			button.center = (center_x, center_y)

			number_buttons.append(button)

	print(grid)

# initiating the game
start_game = False
# first showing numbers
hidden = False

# default
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Chimp Game")
game_font = pygame.font.Font(None, 120) # default font. 120 size.

# start button
start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120)

def display_game_screen():
	global hidden
	if hidden is False:
		elapsed_time = (pygame.time.get_ticks() - start_ticks) /1000 # ms to s.
		if elapsed_time > display_time:
			hidden = True

	# print("Starting game...")
	for idx, rect in enumerate(number_buttons, start=1):
		# drawing the rectagular buttons
		if hidden: # when hidden in True, hide the numbers
			pygame.draw.rect(screen, WHITE, rect)
		else:
		# drawing the number in the center of the cell.
			cell_text = game_font.render(str(idx), True, WHITE)
			text_rect = cell_text.get_rect(center=rect.center)
			screen.blit(cell_text, text_rect)

def display_start_screen():
	# drawing a circle on the screen.
	# located at the center of the start button.
	# color is white, radius is 60, thickness is 5.
	pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)  

def check_buttons(pos):
	global start_game, start_ticks
	# checking if user hit the start button.
	if start_game:
		check_number_buttons(pos)
	elif start_button.collidepoint(pos):
		start_game = True # starting the game play
		start_ticks = pygame.time.get_ticks() # starting the timer as saving the ticking time

def check_number_buttons(position):
	global hidden
	for button in number_buttons:
		if button.collidepoint(position):
			if button == number_buttons[0]: # selecting the right number of order
				print("Correct 😀")
				del number_buttons[0]
				if hidden is False: # if hidden is False, then hide numbers
					hidden = True
			else:
				print("Wrong 🙁")

# level
setup(10)

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
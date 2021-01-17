import os
import random
import pygame

##############################################################

pygame.init()

screen_width = 640 # 
screen_height = 480 # 
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Pang Pang")

# FPS
fps = pygame.time.Clock()
##############################################################

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

background = pygame.image.load(os.path.join(image_path, "background.png"))
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
lara = pygame.image.load(os.path.join(image_path, "lara.png"))
spear = pygame.image.load(os.path.join(image_path, "spear.png"))

stage_rect = stage.get_rect()
stage_size = stage_rect.size
stage_height = stage_size[1]

lara_rect = lara.get_rect()
lara_size = lara_rect.size
lara_width = lara_size[0]
lara_height = lara_size[1]
lara_x_pos = (screen_width/2) - (lara_width/2)
lara_y_pos = (screen_height - (stage_height+lara_height))

lara_to_x = 0
lara_speed = 0.2

spear_rect = spear.get_rect()
spear_size = spear_rect.size
spear_width = spear_size[0]
spear_height = spear_size[1]
spear_x_pos = lara_x_pos - (spear_width)
spear_y_pos = (screen_height) - (stage_height + spear_height)
spear_speed = 0.25

# Game over messages will be defined in various if loops for each scenario. 
# a. When Lara is hit by the ball.
# b. Time out!
# c. When all the ball is cleared. 

# Loading the font. 
game_font = pygame.font.Font(None, 40)
# defining game over messages
gameover_msg = "Game Over!"
# timeout_msg = "Time Out!"
# mission_msg = "Mission Clear!"

total_time = int(60) # sec
# defining starting the time
start_ticking = pygame.time.get_ticks()

# LOADING FIREBALL IMAGES:
fireball_images = [
	pygame.image.load(os.path.join(image_path, "fireball.png")),
	pygame.image.load(os.path.join(image_path, "fireball2.png")),
	pygame.image.load(os.path.join(image_path, "fireball3.png")),
	pygame.image.load(os.path.join(image_path, "fireball4.png"))
	]

fireball_speed_y = [-18, 15, -12, -9] # index 0, 1, 2, 3

fireballs =[]

# Defining the disappearnce of spears and fireballs.

removing_spears = -1
removing_fireballs = -1


# creating the 1st ball. 
fireballs.append({
	"x_pos" : 50,
	"y_pos" : 50,
	"index" : 0, # to load the 1st fireball image. 
	"to_x" : 3,
	"to_y" : -6,
	"initial_y_speed" : fireball_speed_y[0]
	})

spears = []

running = True
while running:
	dt = fps.tick(60)

	# USER KEY INPUTS:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				lara_to_x += lara_speed
			elif event.key == pygame.K_LEFT:
				lara_to_x -= lara_speed
			elif event.key == pygame.K_SPACE:
				spear_x_pos = (lara_x_pos - spear_width)
				spear_y_pos = (screen_height - (stage_height+lara_height/2))
				spears.append([spear_x_pos, spear_y_pos])

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
				lara_to_x == 0

	# SETTING THE CHARACTER'S POSITION:
	lara_x_pos += lara_to_x * dt

	if lara_x_pos < 0:
		lara_x_pos = 0 
	elif lara_x_pos > screen_width - lara_width:
		lara_x_pos = screen_width - lara_width

	# SETTING THE WEAPON'S POSITION:
	# x-position stay still, while the y-position shoots up to the ceiling, 
	# hence the "HEIGHT - speed".
	spears = [ [sp[0], sp[1] - spear_speed*dt] for sp in spears]

	# shows the spears when they only are within the screen_height.
	spears = [[sp[0], sp[1] - spear_speed*dt] for sp in spears if sp[1] > 0]

	# DEFINING BALL'S POSITION: 
	## CONFUSING !!!
	# use 'enumerate' funciton bc there're multiple fireballs and their index in the list. 
	for index, values in enumerate(fireballs): 

		fireball_x_pos = values["x_pos"]
		fireball_y_pos = values["y_pos"]
		fireball_img_index = values["index"]

		fireball_size = fireball_images[fireball_img_index].get_rect().size
		fireball_width = fireball_size[0]
		fireball_height = fireball_size[1]

		# keeping the ball within the screen, then bounce back with the same speed.
		if fireball_x_pos < 0 or fireball_x_pos > screen_width - fireball_width:
			values["to_x"] = values["to_x"] * -1
		# bouncing the ball.
		if fireball_y_pos >= screen_height - stage_height - fireball_height:
			values["to_y"] = values["initial_y_speed"]
		# drawing the parabola.
		else:
			values["to_y"] += 0.5

		# NOW, FINALLY, SETTING THE FIREBALL'S IMAGE POSITION:
		values["x_pos"] += values["to_x"]
		values["y_pos"] += values["to_y"]

	#4 Defining COLLISION CONDITIONS:
		# Lara vs Fireball
	lara_rect.left = lara_x_pos
	lara_rect.top = lara_y_pos

	for index, values in enumerate(fireballs): 

		fireball_x_pos = values["x_pos"]
		fireball_y_pos = values["y_pos"]
		fireball_img_index = values["index"]

		fireball_rect= fireball_images[fireball_img_index].get_rect()
		fireball_rect.left = fireball_x_pos 
		fireball_rect.top = fireball_y_pos

		# collide check.
		if lara_rect.colliderect(fireball_rect):
			running = False
			break

		# Spear vs Fireball

		for spear_index, values in enumerate(spears):
			spear_x_pos = values[0] 
			spear_y_pos = values[1] 
	
			spear_rect.left = spear_x_pos
			spear_rect.top = spear_y_pos
	
			# collide check. #### WHY REMOVING SPEARS is -1?
			if spear_rect.colliderect(fireball_rect):
				removing_spears = spear_index
				removing_fireballs = index
				
				# if the ball is not the smallest, move to the next index. 
				if fireball_img_index < 3: # Total 4 fireball images.
					# the current fireball's position
					fireball_width = fireball_rect.size[0]
					fireball_height = fireball_rect.size[1]

					# next fireballs w/ "+1"
					next_fireball_rect = fireball_images[fireball_img_index + 1].get_rect()
					next_fireball_width = next_fireball_rect.size[0]
					next_fireball_height = next_fireball_rect.size[1]

					# bouncing to the left.
					fireballs.append({
						"x_pos" : fireball_x_pos + (fireball_width/2) - (next_fireball_width/2),
						"y_pos" : fireball_y_pos + (fireball_height/2) - (next_fireball_height/2),
						"index" : fireball_img_index + 1, # to load the 1st fireball image. 
						"to_x" : -3, # to the left
						"to_y" : -6,
						"initial_y_speed" : fireball_speed_y[fireball_img_index + 1]
						})
					# bouncing to the right.
					fireballs.append({
						"x_pos" : fireball_x_pos + (fireball_width/2) - (next_fireball_width/2),
						"y_pos" : fireball_y_pos + (fireball_height/2) - (next_fireball_height/2),
						"index" : fireball_img_index + 1, # to load the 1st fireball image. 
						"to_x" : 3, # to the right
						"to_y" : -6,
						"initial_y_speed" : fireball_speed_y[fireball_img_index + 1]
						})

				break
		else:
			continue # continue to the outter for loop, enumerate(fireballs):
		break

		# REMOVING the spears or fireball
	if removing_fireballs > -1:
		del fireballs[removing_fireballs]
		removing_fireballs = -1

	if removing_spears > -1:
		del spears[removing_spears]
		removing_spears = -1

	if len(fireballs) == 0:					
		gameover_msg = "Mission Complete!"
		running = False

	# DRAWING IMAGES ON THE SCREEN:
	screen.blit(background, (0, 0))

		# UPDATING THE SPEAR POSITION
	for spear_x_pos, spear_y_pos in spears:
		screen.blit(spear, (spear_x_pos, spear_y_pos))

		# UPDATING THE FIREBALL POSITION
	for index, values in enumerate(fireballs):
		fireball_x_pos = values["x_pos"]
		fireball_y_pos = values["y_pos"]
		fireball_img_index = values["index"]
		screen.blit(fireball_images[fireball_img_index], 
					(fireball_x_pos, fireball_y_pos))

	screen.blit(stage, (0, screen_height - stage_height))
	screen.blit(lara, (lara_x_pos, lara_y_pos))

	# calculating elapsed time
	elapsed_time = (pygame.time.get_ticks() - start_ticking) / 1000 # ms -> s 
	timer = game_font.render("Time: {}".format(int(total_time - elapsed_time)), True, (0, 255, 255))
	screen.blit(timer, (10, 10))

	# time out # DOESNT' WORK!!
	if total_time - elapsed_time <= 0:
		gameover_msg = "Time out!"
		running = False

	pygame.display.update()

gameover = game_font.render(gameover_msg, True, (0, 255, 255))
gameover_rect = gameover.get_rect(center=(int(screen_width/2), int(screen_height/2)))
screen.blit(gameover, gameover_rect)

pygame.display.update() # another update. 
pygame.time.delay(2000) # delaying 2 sec before the window shuts. 

pygame.quit()
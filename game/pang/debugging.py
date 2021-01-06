# learn how enumerate works.
# understanding inner and outter for loop.
# "else: continue" works as breaking both loops at the same time. 

balls = [1, 2, 3, 4]
weapons = [11, 22, 3, 44]

for balls_index, balls_value in enumerate(balls):
	print("Ball: ", balls_value)
	for weapons_index, weapons_value in enumerate(weapons):
		print("Weapon: ", weapons_value)
		if balls_value == weapons_value:
			print("Weapon has struck the ball")
			break
	else:
		continue
	print("exiting the 1st for loop.")
	break
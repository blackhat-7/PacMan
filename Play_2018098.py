#Name : Shaunak Pal
#Roll Number : 2018098
#Section : A
#Group : 2

import pygame
from pygame.locals import *
from numpy import loadtxt
import time
import random


#Constants for the game
WIDTH = 32
HEIGHT = 32
COIN_COLOR = pygame.Color(255, 255, 255, 255) # WHITE
PASUE_COLOR = pygame.Color(0, 0, 0, 128) # Trans Black
STILL = (0.0,0.0)
DOWN = (0.0,0.1)
RIGHT = (0.1,0.0)
TOP = (0.0,-0.1)
LEFT = (-0.1,0.0)

#Pacman character images

moveRight = [pygame.image.load('Pics/1.png'), pygame.image.load('Pics/2right.png'), pygame.image.load('Pics/3right.png')]
moveLeft = [pygame.image.load('Pics/1.png'), pygame.image.load('Pics/2left.png'), pygame.image.load('Pics/3left.png')]
moveTop = [pygame.image.load('Pics/1.png'), pygame.image.load('Pics/2up.png'), pygame.image.load('Pics/3up.png')]
moveDown = [pygame.image.load('Pics/1.png'), pygame.image.load('Pics/2down.png'), pygame.image.load('Pics/3down.png')]

TrollFace = pygame.image.load('Pics/Troll.png')
HappyFace = pygame.image.load('Pics/Happy.png')
KiddingMeFace = pygame.image.load('Pics/KiddingMe.png')
LolFace = pygame.image.load('Pics/Lol.png')

TrollFaceEdible = pygame.image.load('Pics/TrollEdible.png')
HappyFaceEdible = pygame.image.load('Pics/HappyEdible.png')
KiddingMeFaceEdible = pygame.image.load('Pics/KiddingMeEdible.png')
LolFaceEdible = pygame.image.load('Pics/LolEdible.png')

wall = pygame.image.load('Pics/wall2.png')
Lives = pygame.image.load('Pics/2left.png')
GameOver = pygame.image.load('Pics/GameOver.png')

#Draws a rectangle for the wall
def draw_wall(screen, pos, texture):
	pixels = pixels_from_points(pos)
	screen.blit(texture, pixels)

#Draws a rectangle for the player
def draw_pacman(screen, pos, face, walkCount):
	global moveRight
	global moveLeft
	global moveTop
	global moveDown
	pixels = pixels_from_points(pos)

	if face == RIGHT:
		screen.blit(moveRight[int(walkCount//8)], pixels)

	elif face == LEFT:
		screen.blit(moveLeft[int(walkCount//8)], pixels)

	elif face == TOP:
		screen.blit(moveTop[int(walkCount//8)], pixels)

	elif face == DOWN:
		screen.blit(moveDown[int(walkCount//8)], pixels)

def respawn():
	pacman_position = (12,14)
	Troll.enemy_position = (12,10)
	Happy.enemy_position = (12,10)
	KiddingMe.enemy_position = (12,10)
	Lol.enemy_position = (12,10)

	return pacman_position, Troll.enemy_position, Happy.enemy_position, KiddingMe.enemy_position, Lol.enemy_position

def caught():
	global gameOver
	global lives
	global pacman_position

	lives -= 1
	Troll.isEdible = False
	Happy.isEdible = False
	KiddingMe.isEdible = False
	Lol.isEdible = False

	if lives == -1:
		gameOver = True
	else:
		pacman_position, Troll.enemy_position, Happy.enemy_position, KiddingMe.enemy_position, Lol.enemy_position = respawn()

def showLives(lives):
	if lives>0:
		pixels = pixels_from_points((23,25))
		screen.blit(Lives, pixels)
	if lives>1:
		pixels = pixels_from_points((22,25))
		screen.blit(Lives, pixels)
	if lives>2:
		pixels = pixels_from_points((21,25))
		screen.blit(Lives, pixels)
	if lives>3:
		pixels = pixels_from_points((20,25))
		screen.blit(Lives, pixels)

	pygame.display.update()

#Draws a rectangle for the coin
def draw_coin(screen, pos):
	pixels = pixels_from_points(pos)
	pygame.draw.circle(screen, COIN_COLOR, (int(pixels[0]+WIDTH/2),int(pixels[1] + HEIGHT/2)), 3)

def draw_powerUp(screen, pos):
	pixels = pixels_from_points(pos)
	pygame.draw.circle(screen, COIN_COLOR, (int(pixels[0]+WIDTH/2),int(pixels[1] + HEIGHT/2)), 9)

#Uitlity functions
def add_to_pos(pos, pos2):
	return (pos[0]+pos2[0], pos[1]+pos2[1])
def pixels_from_points(pos):
	return (pos[0]*WIDTH, pos[1]*HEIGHT)


#Initializing pygame
pygame.init()
screen = pygame.display.set_mode((25*WIDTH,26*HEIGHT), 0, 32)
background = pygame.surface.Surface((25*WIDTH,26*HEIGHT)).convert()


#Initializing variables
def game_initialize():
	global layout
	global rows
	global cols
	global pacman_position
	global clock
	global score
	global walkCount
	global lives
	global start
	global move_direction
	global Troll_move_direction
	global Happy_move_direction
	global KiddingMe_move_direction
	global Lol_move_direction

	layout = loadtxt('layout.txt', dtype=str)
	rows, cols = layout.shape

	pacman_position = (12,14)
	background.fill((0,0,0))
	clock = pygame.time.Clock()
	score = 0
	walkCount = 0
	lives = 4
	start = 0

	move_direction = STILL
	Troll_move_direction = STILL
	Happy_move_direction = STILL
	KiddingMe_move_direction = STILL
	Lol_move_direction = STILL

	Troll.enemy_position = (12,10)
	Happy.enemy_position = (12,10)
	KiddingMe.enemy_position = (12,10)
	Lol.enemy_position = (12,10)

	face = LEFT



layout = loadtxt('layout.txt', dtype=str)
rows, cols = layout.shape

pacman_position = (12,14)
background.fill((0,0,0))
clock = pygame.time.Clock()
score = 0
walkCount = 0
lives = 4
start = 0
edibleTime = 0

move_direction = STILL
Troll_move_direction = STILL
Happy_move_direction = STILL
KiddingMe_move_direction = STILL
Lol_move_direction = STILL

face = LEFT
gameOver = True
gameExit = False

scoreFont = pygame.font.Font('Fonts/crackman front.ttf', 25)
gameOverFont = pygame.font.Font('Fonts/crackman front.ttf', 40)









#EEEEEEEEEEEEENNNNNNNNNNNNNNNNNNNNEEEEEEEEEEEMMMMMMMMMMMMYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY

class Enemy:

	def __init__(self, pos):
		self.enemy_position = pos
		self.possible_paths = [False, False, False, False]
		self.isEdible = False

	def draw(self, screen, EnemyFace, EdibleFace):
		pixels = pixels_from_points(self.enemy_position)
		if not self.isEdible:
			screen.blit(EnemyFace, pixels)
		else:
			screen.blit(EdibleFace, pixels)

	def add_to_pos(self, pos2):
		if (self.enemy_position[0]+pos2[0], self.enemy_position[1]+pos2[1]):
			self.enemy_position = (round(self.enemy_position[0]+pos2[0],1), round(self.enemy_position[1]+pos2[1],1))

		return self.enemy_position

	def isWall(self, enemy_move_direction, start):
		if self.enemy_position == (12,10) and start !=0:
			enemy_move_direction = TOP

		if enemy_move_direction == TOP:
			if layout[int(self.enemy_position[1])][round(self.enemy_position[0])] != 'w':
				enemy_move_direction = TOP

			else:
				enemy_move_direction = self.isJunction(enemy_move_direction, start)

		elif enemy_move_direction == DOWN:
			if layout[int(self.enemy_position[1])+1][round(self.enemy_position[0])] != 'w':
				enemy_move_direction = DOWN

			else:
				enemy_move_direction = self.isJunction(enemy_move_direction, start)

		elif enemy_move_direction == LEFT:
			if (round(self.enemy_position[0]),self.enemy_position[1]) == (0.0, 12.0):
				self.enemy_position = (24.0, 12.0)
			elif layout[round(self.enemy_position[1])][int(self.enemy_position[0])] != 'w':
				enemy_move_direction = LEFT

			else:
				enemy_move_direction = self.isJunction(enemy_move_direction, start)

		elif enemy_move_direction == RIGHT:
			if (round(self.enemy_position[0]),self.enemy_position[1]) == (24.0, 12.0):
				self.enemy_position = (0.0, 12.0)
			elif layout[round(self.enemy_position[1])][int(self.enemy_position[0])+1] != 'w':
				enemy_move_direction = RIGHT

			else:
				enemy_move_direction = self.isJunction(enemy_move_direction, start)


		if enemy_move_direction == TOP or enemy_move_direction == DOWN:
			self.enemy_position = (round(self.enemy_position[0]), self.enemy_position[1])

		elif enemy_move_direction == LEFT or enemy_move_direction == RIGHT:
			self.enemy_position = (self.enemy_position[0], round(self.enemy_position[1]))

		return enemy_move_direction, self.enemy_position

	def isJunction(self, enemy_move_direction, start):

			paths = []

			if enemy_move_direction == TOP and self.enemy_position == (self.enemy_position[0],round(self.enemy_position[1])):

				if layout[round(self.enemy_position[1])-1][round(self.enemy_position[0])] != 'w':
					self.possible_paths[0] = True

				if layout[round(self.enemy_position[1])][int(self.enemy_position[0])-1] != 'w':
					self.possible_paths[2] = True

				if layout[round(self.enemy_position[1])][int(self.enemy_position[0])+1] != 'w':
					self.possible_paths[3] = True
				self.possible_paths[1] = False

			elif enemy_move_direction == DOWN and self.enemy_position == (self.enemy_position[0],round(self.enemy_position[1])):

				if layout[round(self.enemy_position[1])+1][round(self.enemy_position[0])] != 'w':
					self.possible_paths[1] = True

				if layout[round(self.enemy_position[1])][int(self.enemy_position[0])-1] != 'w':
					self.possible_paths[2] = True

				if layout[round(self.enemy_position[1])][int(self.enemy_position[0])+1] != 'w':
					self.possible_paths[3] = True
				self.possible_paths[0] = False

			elif enemy_move_direction == LEFT and  self.enemy_position == (round(self.enemy_position[0]),self.enemy_position[1]):

				if layout[round(self.enemy_position[1])][int(self.enemy_position[0])-1] != 'w':
					self.possible_paths[2] = True

				if layout[round(self.enemy_position[1])-1][round(self.enemy_position[0])] != 'w':
					self.possible_paths[0] = True

				if layout[round(self.enemy_position[1])+1][round(self.enemy_position[0])] != 'w':
					self.possible_paths[1] = True
				self.possible_paths[3] = False

			elif enemy_move_direction == RIGHT and  self.enemy_position == (round(self.enemy_position[0]),self.enemy_position[1]):

				if layout[round(self.enemy_position[1])][int(self.enemy_position[0])+1] != 'w':
					self.possible_paths[3] = True

				if layout[round(self.enemy_position[1])-1][round(self.enemy_position[0])] != 'w':
					self.possible_paths[0] = True

				if layout[round(self.enemy_position[1])+1][round(self.enemy_position[0])] != 'w':
					self.possible_paths[1] = True
				self.possible_paths[2] = False


			if self.possible_paths[0] == True and start!=0:
				paths.append(TOP)
				if pacman_position[1] < self.enemy_position[1]:
					paths.append(TOP)
					paths.append(TOP)
					paths.append(TOP)

			if self.possible_paths[1] == True and start!=0:
				paths.append(DOWN)
				if pacman_position[1] > self.enemy_position[1]:
					paths.append(DOWN)
					paths.append(DOWN)
					paths.append(DOWN)

			if self.possible_paths[2] == True and start!=0:
				paths.append(LEFT)
				if pacman_position[0] < self.enemy_position[0]:
					paths.append(LEFT)
					paths.append(LEFT)
					paths.append(LEFT)

			if self.possible_paths[3] == True and start!=0:
				paths.append(RIGHT)
				if pacman_position[0] > self.enemy_position[0]:
					paths.append(RIGHT)
					paths.append(RIGHT)
					paths.append(RIGHT)


			if len(paths) > 0:
				path_choice = random.randint(0,len(paths)-1)
				enemy_move_direction = paths[path_choice]

			self.possible_paths = [False,False,False,False]
			return enemy_move_direction

	def respawn_enemy(self):
		self.enemy_position = (12,12)


Troll = Enemy((12,10))
Happy = Enemy((12,10))
KiddingMe = Enemy((12,10))
Lol = Enemy((12,10))

game_initialize()
#GameLoop
while gameExit == False:
	clock.tick(50)
	coins = 0
	while gameOver:

		screen.blit(GameOver, (0,0))

		finalScoreText = gameOverFont.render('FINAL SCORE : {}'.format(score), True, (255, 255, 255))
		actionText1 = gameOverFont.render('Press \"P\" to play', True, (255, 255, 255))
		actionText2 = gameOverFont.render('Press \"Q\" to Quit', True, (255, 255, 255))
		screen.blit(finalScoreText, [220, 380])
		screen.blit(actionText1, [200, 420])
		screen.blit(actionText2, [200, 460])

		for event in pygame.event.get():
			if event.type == QUIT:
				exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					gameOver = False
					game_initialize()

					for col in range(cols):
						for row in range(rows):
							value = layout[row][col]
							pos = (col, row)
							if value == 'w':
								draw_wall(screen, pos, wall)
							elif value == '.':
								draw_coin(screen, pos)
							elif value == 'p':
								draw_powerUp(screen, pos)

				elif event.key == pygame.K_q:
					gameOver = False
					gameExit = True


		pygame.display.update()

	for event in pygame.event.get():
		if event.type == QUIT:
			exit()

	screen.blit(background, (0,0))

	#Draw board from the 2d layout array.
  	#In the board, 's' denote the empty space, 'w' are the walls, '.' are the coins

	for col in range(cols):
		for row in range(rows):
			value = layout[row][col]
			pos = (col, row)
			if value == 'w':
				draw_wall(screen, pos, wall)
			elif value == '.':
				coins += 1
				draw_coin(screen, pos)
			elif value == 'p':
				draw_powerUp(screen, pos)

	#Draw the player and enemy
	if walkCount == 15:
		walkCount = 0
	walkCount += 1

	draw_pacman(screen, pacman_position, face, walkCount)
	Troll.draw(screen, TrollFace, TrollFaceEdible)
	Happy.draw(screen, HappyFace, HappyFaceEdible)
	KiddingMe.draw(screen, KiddingMeFace, KiddingMeFaceEdible)
	Lol.draw(screen, LolFace, LolFaceEdible)

	#Take input from the user and update pacman moving direction

	keys = pygame.key.get_pressed()

	if keys[pygame.K_w] or keys[pygame.K_UP] or move_direction==TOP:
		face = TOP
		if layout[int(pacman_position[1])][round(pacman_position[0])] != 'w':
			move_direction = TOP
		else:
			move_direction = STILL

	if keys[pygame.K_s] or keys[pygame.K_DOWN] or move_direction==DOWN:
		face = DOWN
		if layout[int(pacman_position[1])+1][round(pacman_position[0])] != 'w':
			move_direction = DOWN
		else:
			move_direction = STILL

	if keys[pygame.K_a] or keys[pygame.K_LEFT] or move_direction==LEFT:
		face = LEFT
		start = 1 if start == 0 else 2
		if (round(pacman_position[0]),pacman_position[1]) == (0.0, 12.0):
			pacman_position = (24.0, 12.0)
		elif layout[round(pacman_position[1])][int(pacman_position[0])] != 'w':
			move_direction = LEFT
		else:
			move_direction = STILL

	if keys[pygame.K_d] or keys[pygame.K_RIGHT] or move_direction==RIGHT:
		face = RIGHT
		start = 1 if start == 0 else 2
		if (round(pacman_position[0]),pacman_position[1]) == (24.0, 12.0):
			pacman_position = (0.0, 12.0)
		elif layout[round(pacman_position[1])][int(pacman_position[0])+1] != 'w':
			move_direction = RIGHT
		else:
			move_direction = STILL


	if move_direction == TOP or move_direction == DOWN:
		pacman_position = (round(pacman_position[0]), pacman_position[1])

	elif move_direction == LEFT or move_direction == RIGHT:
		pacman_position = (pacman_position[0], round(pacman_position[1]))


	#Update player position based on movement.

	pacman_position = add_to_pos(pacman_position, move_direction)
	Troll.enemy_position = Troll.add_to_pos(Troll_move_direction)
	Happy.enemy_position = Happy.add_to_pos(Happy_move_direction)
	KiddingMe.enemy_position = KiddingMe.add_to_pos(KiddingMe_move_direction)
	Lol.enemy_position = Lol.add_to_pos(Lol_move_direction)

	if start ==1:
		Troll_move_direction = TOP
		Happy_move_direction = LEFT
		KiddingMe_move_direction = RIGHT
		start = 2

	Troll_move_direction, Troll.enemy_position = Troll.isWall(Troll_move_direction, start)
	Happy_move_direction, Happy.enemy_position = Happy.isWall(Happy_move_direction, start)
	KiddingMe_move_direction, KiddingMe.enemy_position = KiddingMe.isWall(KiddingMe_move_direction, start)
	Lol_move_direction, Lol.enemy_position = Lol.isWall(Lol_move_direction, start)

	Troll_move_direction = Troll.isJunction(Troll_move_direction, start)
	Happy_move_direction = Happy.isJunction(Happy_move_direction, start)
	KiddingMe_move_direction = KiddingMe.isJunction(KiddingMe_move_direction, start)
	Lol_move_direction = Lol.isJunction(Lol_move_direction, start)


	#Updates Score

	scoreText = scoreFont.render('SCORE : {}'.format(score), True, (0, 255, 0))
	screen.blit(scoreText, [35, 0])
	if layout[round(pacman_position[1])][round(pacman_position[0])] == '.':
		layout[round(pacman_position[1])][round(pacman_position[0])] = ' '
		score += 10

	if layout[round(pacman_position[1])][round(pacman_position[0])] == 'p':
		layout[round(pacman_position[1])][round(pacman_position[0])] = ' '
		edibleTime = int(time.time())
		Troll.isEdible = True
		Happy.isEdible = True
		KiddingMe.isEdible = True
		Lol.isEdible = True

	if int(time.time())-edibleTime == 10:
		edibleTime = 0
		Troll.isEdible = False
		Happy.isEdible = False
		KiddingMe.isEdible = False
		Lol.isEdible = False

	#gameOver Conditions

	if (round(pacman_position[0]),round(pacman_position[1])) == (round(Troll.enemy_position[0]), round(Troll.enemy_position[1])) or (round(pacman_position[0]),round(pacman_position[1])) == (round(Happy.enemy_position[0]), round(Happy.enemy_position[1])) or (round(pacman_position[0]),round(pacman_position[1])) == (round(KiddingMe.enemy_position[0]),round(KiddingMe.enemy_position[1])) or (round(pacman_position[0]),round(pacman_position[1])) == (round(Lol.enemy_position[0]), round(Lol.enemy_position[1])):

		if Troll.isEdible or Happy.isEdible or KiddingMe.isEdible or Lol.isEdible:
			if (round(pacman_position[0]),round(pacman_position[1])) == (round(Troll.enemy_position[0]), round(Troll.enemy_position[1])):
				if Troll.isEdible:
					Troll.respawn_enemy()
					Troll.isEdible = False
				else:
					caught()

			if (round(pacman_position[0]),round(pacman_position[1])) == (round(Happy.enemy_position[0]), round(Happy.enemy_position[1])):
				if Happy.isEdible:
					Happy.respawn_enemy()
					Happy.isEdible = False
				else:
					caught()

			if (round(pacman_position[0]),round(pacman_position[1])) == (round(KiddingMe.enemy_position[0]),round(KiddingMe.enemy_position[1])):
				if KiddingMe.isEdible:
					KiddingMe.respawn_enemy()
					KiddingMe.isEdible = False
				else:
					caught()

			if (round(pacman_position[0]),round(pacman_position[1])) == (round(Lol.enemy_position[0]), round(Lol.enemy_position[1])):
				if Lol.isEdible:
					Lol.respawn_enemy()
					Lol.isEdible = False
				else:
					caught()

				score += 200
		else:
			caught()
	showLives(lives)

	if coins == 0:
		gameOver = True

	#Update the display
	pygame.display.update()

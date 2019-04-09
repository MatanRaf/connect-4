from colors import *
import pygame
import sys

height = 600
width = 700
screen = pygame.display.set_mode((width,height+100))
spaces = []
player = red
arrow = pygame.image.load('arrow.png')
arrow_column = 0
key_pressed = False
clock = pygame.time.Clock()

class spot:
	def __init__(self, column, row): #properties of the spot
		self.column = column
		self.row = row
		self.width = 15
		self.height = 15
		self.player = white


for s in range(0,42):
	#creating all the spaces
	spaces.append("space%d"%s)
	spaces[s] = spot(s%7,s//7)





def test_for_players( column_input):
	global spaces
	lowest_spot = None
	for s in spaces:
		if s.column == column_input:
			if s.player == white:
				lowest_spot = s
	return lowest_spot



def turn(column_input):
	global player
	markerplace = test_for_players(column_input)
	markerplace.player = player
	if player == red:
		player = gold
	elif player == gold:
		player = red
	
	

def redraw_display():
	screen.fill(white)
	for s in spaces:
		pygame.draw.rect(screen, s.player, (s.column * 100,s.row * 100, 100 , 100))
	screen.blit(arrow, (arrow_column * 100,height))
	pygame.display.update()


def test_for_winner():
	for idx, s in enumerate(spaces):
		#print (idx)
		if idx < 39:
			if spaces[idx].player == spaces[idx+1].player == spaces[idx+2].player == spaces[idx+3].player and spaces[idx].row == spaces[idx + 3].row:
				if spaces[idx].player != white:
					return True
		if idx < 21:
			if spaces[idx].player == spaces[idx+7].player == spaces[idx+14].player == spaces[idx+21].player:
				if spaces[idx].player != white:
					return True
		if idx < 24:
			if spaces[idx].player == spaces[idx+6].player == spaces[idx+12].player == spaces[idx+18].player and spaces[idx].column == spaces[idx+18].column + 3:
				if spaces[idx].player != white:
					return True
		if idx < 18:
			if spaces[idx].player == spaces[idx+8].player == spaces[idx+16].player == spaces[idx+24].player and spaces[idx].column == spaces[idx+24].column - 3:
				if spaces[idx].player != white:
					return True
	else:
		return False







redraw_display()
game_running = True
while game_running:
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			sys.exit()
	

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT and arrow_column < 6:
				arrow_column += 1
			if event.key == pygame.K_LEFT and arrow_column > 0:
				arrow_column -= 1
			if event.key == pygame.K_SPACE:
				turn (arrow_column)

	
	redraw_display()
	clock.tick(50)
	if test_for_winner():
		game_running = False
		for i in range(40):
			clock.tick(10)
	

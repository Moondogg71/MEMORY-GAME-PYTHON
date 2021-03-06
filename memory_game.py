import random, pygame, sys
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
REVEALSPEED = 8
BOXSIZE = 40
GAPSIZE = 10
BOARDWIDTH = 10 
BOARDHEIGHT = 7
assert(BOARDWIDTH * BOARDHEIGHT) % 2 == 0 
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int(WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)

GRAY = (100, 100, 100)
NAVYBLUE = (60 ,60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)

BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE

DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

ALLCOLORS = (RED, GREEN, BLUE YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES =(DONUT, SQUARE, DIAMOND, LINES, OVAL)
assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT, "Board is too big for shapes"


def main():
	global FPSCLOCK, DISPLAYSURF
	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

	mousex = 0
	mousey = 0
	pygame.display.set_caption('Memory Game')

	mainBoard = getRandomizedBoard()
	revealedBoxes = generateRevealedBoxesData(False)

	firstSelection = None #Stores X, Y of first box clicked

	DISPLAYSURF.fill(BGCOLOR)
	startGameAnimation(mainBoard)

	while True:
		mouseclicked = False

		DISPLAYSURF.fill(BGCOLOR)#drawing the window
		drawBoard(mainBoard, revealedBoxes)

		for event in pygame.event.get(): #event handling loop
			if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()
			elif event.type == MOUSEMOTION:
				mousex, mousey = event.pos
			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				mouseClicked = True	

		boxx, boxy = getBoxAtPixel(mousex, mousey)
		if boxx != None and boxy != None:
			if not revealedBoxes[boxx][boxy]:
				drawHighlightBox(boxx, boxy)
			if not revealedBoxes[boxx][boxy] and mouseClicked:
				revealBoxesAnimation(mainBoard, [(boxx, boxy)])
				revealedBoxes[boxx][boxy]	











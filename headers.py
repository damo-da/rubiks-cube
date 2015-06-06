'''HEADERS for the project.'''

from colors import *
from copy import deepcopy

FRONT_SIDE="front"
BACK_SIDE="back"
TOP_SIDE="up"
BOTTOM_SIDE="down"
LEFT_SIDE="left"
RIGHT_SIDE="right"

CORNER_BOX='corner_box'
CENTER_BOX='center_box'
SIDE_BOX='side_box'



CORNER_PIECES=[(0,0,0),(0,0,2),(0,2,0),(0,2,2),(2,0,0),(2,0,2),(2,2,0),(2,2,2)]
SIDE_PIECES=   [(0,0,1),(0,2,1),(2,0,1),(2,2,1),
				(1,0,0),(1,0,2),(1,2,0),(1,2,2),
				(0,1,0),(0,1,2),(2,1,0),(2,1,2)]
CENTER_PIECES=[(1,0,1),(1,2,1),(2,1,1),(0,1,1),(1,1,0),(1,1,2)]

F2L=50
OLL=51
CROSS=52
PLL=53

def getIdFromPos(pos):
	'''Get id of box from pos.'''
	return (pos[0]+pos[1]*3+pos[2]*9)
	
def getPosFromId(myId):
	'''opposite of getIDFromPos(pos).'''
	pos=[0,0,0]
	while myId>8:
		pos[2] += 1
		myId -= 9
	while myId>2:
		pos[1] += 1
		myId -= 3
	pos[0]=myId
	return (pos[0],pos[1],pos[2])

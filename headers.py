'''HEADERS for the project.'''

from colors import *
from copy import deepcopy
from time import sleep

from utilities import *


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

class FaceObject(object):
    def __init__(self):
        self.front=GREEN
        self.back=GREEN.getOpposite()
        self.left=ORANGE
        self.right=ORANGE.getOpposite()
        self.top=WHITE
        self.bottom=WHITE.getOpposite()
        
    def all(self):
        return deepcopy([self.front,self.back,self.left,self.right,self.top,self.bottom])
        
    def getSideForColor(self,color):
        if str(color)==str(self.front):
            return "front"
        elif str(color)==str(self.back):
            return "back"
        elif str(color)==str(self.right):
            return "right"
        elif str(color)==str(self.left):
            return "left"
        elif str(color)==str(self.top):
            return "top"
        elif str(color)==str(self.bottom):
            return "bottom"
        else:
            return Exception("Exception thrown by FaceColor.getSideForColor")
    def update(self,values):
        self.front=values["front"]
        self.top=values["top"]
        self.left=values["left"]
        self.back=self.front.getOpposite()
        self.bottom=self.top.getOpposite()
        self.right=self.left.getOpposite()
        
    def getSidesExcludingColor(self,color):
        allColors=["front","back","left","right","top","bottom"]
        colorName=self.getSideForColor(color)
        allColors.remove(colorName)
        return allColors

FaceColor=FaceObject()

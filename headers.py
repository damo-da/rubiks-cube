'''The global settings for the project.'''

from colors import *
from copy import deepcopy
from time import sleep


#some globak constants declared
FRONT_SIDE="front"
BACK_SIDE="back"
TOP_SIDE="up"
BOTTOM_SIDE="down"
LEFT_SIDE="left"
RIGHT_SIDE="right"

CORNER_BOX='corner_box'
CENTER_BOX='center_box'
SIDE_BOX='side_box'


#where boxes can lie
CORNER_BOXES=[(0,0,0),(0,0,2),(0,2,0),(0,2,2),(2,0,0),(2,0,2),(2,2,0),(2,2,2)]

SIDE_BOXES=   [(0,0,1),(0,2,1),(2,0,1),(2,2,1),
                (1,0,0),(1,0,2),(1,2,0),(1,2,2), 
                (0,1,0),(0,1,2),(2,1,0),(2,1,2)]
CENTER_BOXES=[(1,0,1),(1,2,1),(2,1,1),(0,1,1),(1,1,0),(1,1,2)]

def getIdFromPos(pos):
    '''Get id of box from pos.'''
    #every position in box has an ID and vice versa. ID can be decoded to position and vice versa

    box_id=pos[0]+pos[1]*3+pos[2]*9

    return box_id
    
def getPosFromId(box_id):
    '''Get position of box from its Id.'''
    #opposite of getIDFromPos(pos).

    pos=[0,0,0]

    while box_id>8:
        pos[2] += 1
        box_id -= 9

    while box_id>2:
        pos[1] += 1
        box_id -= 3

    pos[0]=box_id

    return (pos[0],pos[1],pos[2])


class FaceObject(object):
    '''The object to convert face into respective colors.

    If I want to know what color lies at the centre of bottom of cube, 
        it becomes easier to call this funcction.
    '''

    def __init__(self):
        self.front=GREEN
        self.back=GREEN.getOpposite()
        self.left=ORANGE
        self.right=ORANGE.getOpposite()
        self.top=WHITE
        self.bottom=WHITE.getOpposite()
        
    def all(self):
        '''Returns a clone of all FaceColors.'''
        return deepcopy([self.front,self.back,self.left,self.right,self.top,self.bottom])
        
    def getSideForColor(self,color):
        '''Detects the face where a color natively belongs to.'''

        if str(color)==str(self.front):
            return FRONT_SIDE
        elif str(color)==str(self.back):
            return BACK_SIDE
        elif str(color)==str(self.right):
            return RIGHT_SIDE
        elif str(color)==str(self.left):
            return LEFT_SIDE
        elif str(color)==str(self.top):
            return TOP_SIDE
        elif str(color)==str(self.bottom):
            return BOTTOM_SIDE
        else:
            raise SystemError("Error raised by FaceColor.getSideForColor:\
             can not say where the color belongs to");

    def update(self,values):
        '''Upate the variables.'''

        self.front=values["front"]
        self.top=values["top"]
        self.left=values["left"]
        self.back=self.front.getOpposite()
        self.bottom=self.top.getOpposite()
        self.right=self.left.getOpposite()
        
    def getSidesExcludingColor(self,color):
        allSides=[FRONT_SIDE,BACK_SIDE,LEFT_SIDE,TOP_SIDE,RIGHT_SIDE,BOTTOM_SIDE]

        colorName=self.getSideForColor(color)


        allSides.remove(colorName)
        return allSides

FaceColor=FaceObject()

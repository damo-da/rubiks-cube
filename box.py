'''The class for the boxes of the cube.
Coordinates start with 0 and end with 2.
coordinates are currently calculated with green on front, red on left and white on bottom.
box of position (0,0,0) goes for the corner box of front-left-bottom.'''

from headers import *
from colors import *
        
class Box(object):
    '''The base class for boxes.'''
    def __init__(self,boxType):
        self.pos=(0,0,0)
        self.boxType=boxType

        #these are the "boxes" of the graphics library. 
        #The cube does not mess up with them.
        self.xzBox=None
        self.xyBox=None
        self.yzBox=None
        
    def getType(self):
        return self.boxType
        
    def setPos(self,x,y,z):
        self.pos=(x,y,z)

    def getPos(self):
        return self.pos

    def getSides(self):
        # returns all of the sides of box that are not None. 
        # ie, sides that have colour
        # a corner box would return three sides, a side box would return two

        ret=[]
        if self.xz:
            ret.append(self.xz)
        if self.yz:
            ret.append(self.yz)
        if self.xy:
            ret.append(self.xy)
        return ret

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return "%s at %s , xz= %s , yz= %s , xy= %s "%(
            self.boxType,
            self.pos,
            self.xz,
            self.yz,
            self.xy)

    def hasColor(self,*colors):
        #returns true if the box has each color in colors

        ret=True
        for color in colors:
            colorFound=False
            if self.xy is not None and self.xy.color==color.color:
                colorFound=True
            if self.xz is not None and self.xz.color==color.color:
                colorFound=True
            if self.yz is not None and self.yz.color==color.color:
                colorFound=True
            if not colorFound:
                ret=False
                break
        #print ret
        return ret
            
        return False
        
class CornerBox(Box):
    '''A corner box of Rubik's cube.
    
    A corner box has three faces. Its xz, xy and yz are ALWAYS not None, no matter what.'''

    def __init__(self):
        Box.__init__(self,CORNER_BOX);
        
        self.xy=FaceColor.bottom        #the colors of the box
        self.yz=FaceColor.left
        self.xz=FaceColor.front

        self.pos=(0,0,0)
        
class SideBox(Box):
    '''A side box of Rubik's cube.
    
    Note: the naming of SideBox may be inappropriate. But, to understand, it is the box between
    two corner boxes.

    A side box has three faces. One of it's xy, xz or yz is ALWAYS None.'''

    def __init__(self):
        Box.__init__(self,SIDE_BOX)
        
        #some random default values
        self.xy=None
        self.yz=FaceColor.left
        self.xz=FaceColor.front
        
        self.pos=(0,0,1)
        
class CenterBox(Box):
    '''A center box of Rubik's cube.
    
    A center box has three faces. Two of it's xy, xz or yz are ALWAYS None.'''
    def __init__(self):
        Box.__init__(self,CENTER_BOX)
        
        #some random default values
        self.xz=FaceColor.front
        self.yz=None
        self.xy=None
    
if __name__=="__main__":
    import main
    

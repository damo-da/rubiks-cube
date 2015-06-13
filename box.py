'''The class for the cells of the cube to lie.
Cells are also referred as pieces or boxes in this project.
Coordinates start with 0 and end with 2.
coordinates are currently calculated with green on front, red on left and white on bottom.
Currently, (0,0,0) goes for the corner Cell of front-left-bottom.'''
from headers import *
from colors import *
        
class Box(object):
    '''The base class for boxes.'''
    def __init__(self,boxType):
        self.pos=(0,0,0)
        self.boxType=boxType

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
        return "%s at "%(self.boxType)+str(self.pos)+" , xz= "+str(self.xz)+" , yz= "+str(self.yz)+" , xy= "+str(self.xy)+"\n"
    def hasColor(self,*colors):
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
    '''A corner box. has 3 faces.'''
    def __init__(self):
        Box.__init__(self,CORNER_BOX)
        
        self.xy=FaceColor.bottom        #the colors of the box
        self.yz=FaceColor.left
        self.xz=FaceColor.front

        self.pos=(0,0,0)
        
class SideBox(Box):
    '''A side box. has 2 faces.'''
    def __init__(self):
        Box.__init__(self,SIDE_BOX)
        
        self.xy=None
        self.yz=FaceColor.left
        self.xz=FaceColor.front
        
        self.pos=(0,0,1)
        
class CenterBox(Box):
    '''A center box. has 1 face.'''
    def __init__(self):
        Box.__init__(self,CENTER_BOX)
        
        self.xz=FaceColor.front
        self.yz=None
        self.xy=None
    
if __name__=="__main__":
    import main
    

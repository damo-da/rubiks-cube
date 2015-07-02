'''The colors in the rubik's cube.'''

from visual import color

class ColorItem(object):
    '''Each specific color.'''

    def __init__(self,name="red",color=color.red):
        self.name=name
        self.color=color

        #initially, the opposite of this color is none.
        #By opposite, I mean,
        #let's consider a fully solved original rubik's cube.
        #It has white in the base and yellow in the top.
        #this opposite property gives us, white.opposite=yellow and vice versa.
        self.opposite=None
        
    def setColor(self,color):
        self.color=color
        
    def getColor(self):
        return self.color
        
    def getOpposite(self):
        return self.opposite
    
    def __str__(self):
        return self.name
        
    def __repr__(self):
        return str(self)
        
    def setOpposite(self,opposite):
        self.opposite=opposite
        
        if(opposite):
            opposite.opposite=self

#yeah, create the instances
RED=ColorItem("red",color.red);
BLUE=ColorItem("blue",color.blue);
GREEN=ColorItem("green",color.green);
ORANGE=ColorItem("orange",color.orange);
WHITE=ColorItem("white",color.white);
YELLOW=ColorItem("yellow",color.yellow);

#set their opposites.
#note: only 3 are required. The opposite of these 3 are autogerenarated
RED.setOpposite(ORANGE)
BLUE.setOpposite(GREEN)
WHITE.setOpposite(YELLOW)


def decodeColorFromText(color):
    '''Converts text to color and returns its instance.'''
    color=color.lower()

    if(not color): return;
    if color.startswith(str(RED)): return RED
    elif color.startswith(str(GREEN)): return GREEN
    elif color.startswith(str(YELLOW)): return YELLOW
    elif color.startswith(str(WHITE)): return WHITE
    elif color.startswith(str(BLUE)): return BLUE
    elif color.startswith(str(ORANGE)): return ORANGE
    
    raise SystemError("unknown color: "+color);

if __name__=="__main__":
    pass

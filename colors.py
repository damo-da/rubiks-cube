'''For representing color of the rubik's cube.'''
from pygame.locals import Color

class ColorItem(object):
	'''WHITE,RED,BLUE,etc are all instances of this class.'''
	def __init__(self,name="red"):
		self.name=name
		self.color=Color('red')
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
		opposite.opposite=self

RED=ColorItem("red");
BLUE=ColorItem("blue");
GREEN=ColorItem("green");
ORANGE=ColorItem("orange");
WHITE=ColorItem("white");
YELLOW=ColorItem("yellow");

RED.setColor(Color("red"))
GREEN.setColor(Color("green"))
YELLOW.setColor(Color("yellow"))
BLUE.setColor(Color("blue"))
WHITE.setColor(Color("white"))
ORANGE.setColor(Color("orange"))

RED.setOpposite(ORANGE)
BLUE.setOpposite(GREEN)
WHITE.setOpposite(YELLOW)

def decodeColorFromText(color):
	'''Converts text and returns its instance.'''
	color=color.upper()
	if color.startswith('RED'): return RED
	elif color.startswith('GREEN'): return GREEN
	elif color.startswith('YELLOW'): return YELLOW
	elif color.startswith('WHITE'): return WHITE
	elif color.startswith('BLUE'): return BLUE
	elif color.startswith('ORANGE'): return ORANGE
	return None
	
if __name__=="__main__":
	pass

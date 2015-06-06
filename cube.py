'''The class for the cube.'''

from box import *
from headers import *
from loader import loadCubeFromFile
from rotation import *
from AI import *
import random

class Cube(object):
	'''The Cube Class.'''
	def __init__(self):
		self.reset()
		
	def reset(self):
		'''Reset the cube.'''
		self.boxes=loadCubeFromFile("cube.txt")
		self.solved=deepcopy(self.boxes)
		self.resetMoves()
		
	def randomAlgorithm(self,count=20):
		'''Generates a random algorithm of length=count.'''
		chars=["F","Fi","R","Ri","B","Bi","L","Li", "D", "Di"] 
		string=""
		index=len(chars)-1
		for i in range(count):
			string += chars[random.randint(0,index)] + " "
		return string
	def isSolvedAt(self,pos):
		'''Check if a pos has its native colors, flipped properly.'''
		box=self.boxAt(pos[0],pos[1],pos[2])
		for solved in self.solved:
			if box.pos==solved.pos:
				break;
				solved=box
		C1=str(box.xz)==str(solved.xz)
		C2=str(box.yz)==str(solved.yz)
		C3=str(box.xy)==str(solved.xy)
		return ( C1 and C2 and C3)
		#return C1
	def isSolved(self):
		'''Chech if the cube is solved.'''
		for box in self.boxes:
			if not self.isSolvedAt(box.pos):
				return False
		return True
	def getSide(self,side):
		'''Returns cells of a specific side.'''
		ret=[]
		a=self.boxes
		for box in self.boxes:
			pos=box.getPos()
			if side==FRONT_SIDE and pos[1]==0:
				ret.append(box)
			elif side==BACK_SIDE and pos[1]==2:
				ret.append(box)
			elif side==TOP_SIDE and pos[2]==2:
				ret.append(box)
			elif side==BOTTOM_SIDE and pos[2]==0:
				ret.append(box)
			elif side==LEFT_SIDE and pos[0]==0:
				ret.append(box)
			elif side==RIGHT_SIDE and pos[0]==2:
				ret.append(box)
		return ret
	def resetMoves(self):
		'''Empty moves.'''
		self.move=""
	def action(self,word):
		'''Apply algorithm to the cube.'''
		self.move += word+ " "
		keys=word.split(" ")
		for key in keys:
			reverse=False
			if "'" in key or "i" in key:
				reverse=True
			key=key.replace("'",'')
			key=key.replace("i","")
			if key=="":
				continue
			if key not in ["F","R","U","D","B","L"]:
				print "key %s doesnot exist"%key
				continue
			count=1
			if reverse:
				count=3
			while count:
				if key=='F':
					rotateFrontSide(self);
				elif key=='B':
					rotateBackSide(self);
				elif key=='L':
					rotateLeftSide(self);
				elif key=='R':
					rotateRightSide(self);
				elif key=='U':
					rotateTopSide(self);
				elif key=='D':
					rotateBottomSide(self);
				count -= 1
	def findAll(self,array,color):
		'''Returns all box with color from the array.'''
		ret=[]
		for box in self.boxes:
			if box.pos in array:
				if box.hasColor(color):
					ret.append(box)
		return ret
	def findAllWithout(self,array,color):
		'''Returns all box without color from the array.'''
		ret=[]
		for box in self.boxes:
			if box.pos in array:
				if not box.hasColor(color):
					ret.append(box)
		return ret
	def f2lSecondPhaseComplete(self):
		'''Checks if f2l is complete.'''
		C1=self.boxAt(0,0,1).xz.color==GREEN.color and self.boxAt(2,0,1).xz.color==GREEN.color
		C2=self.boxAt(0,0,1).yz.color==RED.color and self.boxAt(0,2,1).yz.color==RED.color
		C3=self.boxAt(0,2,1).xz.color==BLUE.color and self.boxAt(2,2,1).xz.color==BLUE.color
		C4=self.boxAt(2,2,1).yz.color==ORANGE.color and self.boxAt(2,0,1).yz.color==ORANGE.color
		return (C1 and C2 and C3 and C4)
	def boxAt(self,x,y,z):
		for box in self.boxes:
			if box.pos==(x,y,z):
				return box
	
	def solve(self):
		return solveTheCube(self)
		
if __name__=="__main__":
	import main

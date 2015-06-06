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
	def getMoves(self):
		return optimizeMoves(self.move)
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
	
	def getFaceUpdater(self):
		return {"front":self.boxAt(1,0,1).xz,"left":self.boxAt(0,1,1).yz,"top":self.boxAt(1,1,2).xy}
		
	def action(self,word):
		'''Apply algorithm to the cube.'''
		word=word.replace("'","i")
		
		self.move += word+ " "
		
		keys=word.split(" ")
		for key in keys:
			if len(key)>1:
				key=key[0].upper()+key[1:]
			else:
				key=key.upper()
			if key=="": continue
			
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
			elif key=='Fi':
				rotateFrontSide(self);
				rotateFrontSide(self);
				rotateFrontSide(self);
			elif key=='Bi':
				rotateBackSide(self);
				rotateBackSide(self);
				rotateBackSide(self);
			elif key=='Li':
				rotateLeftSide(self);
				rotateLeftSide(self);
				rotateLeftSide(self);
			elif key=='Ri':
				rotateRightSide(self);
				rotateRightSide(self);
				rotateRightSide(self);
			elif key=='Ui':
				rotateTopSide(self);
				rotateTopSide(self);
				rotateTopSide(self);
			elif key=='Di':
				rotateBottomSide(self);
				rotateBottomSide(self);
				rotateBottomSide(self);
			elif key=='F2':
				rotateFrontSide(self);
				rotateFrontSide(self);
			elif key=='B2':
				rotateBackSide(self);
				rotateBackSide(self);
			elif key=='L2':
				rotateLeftSide(self);
				rotateLeftSide(self);
			elif key=='R2':
				rotateRightSide(self);
				rotateRightSide(self);
			elif key=='U2':
				rotateTopSide(self);
				rotateTopSide(self);
			elif key=='D2':
				rotateBottomSide(self);
				rotateBottomSide(self);
			elif key=="M":
				rotateM(self);
			elif key=="E":
				rotateE(self)
			elif key=="S":
				rotateS(self)
			elif key=="M2":
				rotateM(self);
				rotateM(self);
			elif key=="E2":
				rotateE(self)
				rotateE(self)
			elif key=="S2":
				rotateS(self)
				rotateS(self)
			elif key=="Mi":
				rotateM(self);
				rotateM(self);
				rotateM(self);
			elif key=="Ei":
				rotateE(self)
				rotateE(self)
				rotateE(self)
			elif key=="Si":
				rotateS(self)
				rotateS(self)
				rotateS(self)
			elif key=="X":
				rotateRightSide(self)
				rotateLeftSide(self)
				rotateLeftSide(self)
				rotateLeftSide(self)
				rotateM(self)
				rotateM(self)
				rotateM(self)
			elif key=="Xi":
				rotateRightSide(self)
				rotateRightSide(self)
				rotateRightSide(self)
				rotateLeftSide(self)
				rotateM(self)
				
			elif key=="X2":
				rotateM(self)
				rotateM(self)
				rotateRightSide(self)
				rotateRightSide(self)
				rotateLeftSide(self)
				rotateLeftSide(self)
				
			elif key=="Y":
				rotateTopSide(self)
				rotateBottomSide(self)
				rotateBottomSide(self)
				rotateBottomSide(self)
				rotateE(self)
				rotateE(self)
				rotateE(self)
			elif key=="Yi":
				rotateTopSide(self)
				rotateTopSide(self)
				rotateTopSide(self)
				rotateBottomSide(self)
				rotateE(self)
			elif key=="Y2":
				rotateTopSide(self)
				rotateTopSide(self)
				rotateBottomSide(self)
				rotateBottomSide(self)
				rotateE(self)
				rotateE(self)
			elif key=="Z":
				rotateFrontSide(self)
				rotateFrontSide(self)
				rotateFrontSide(self)
				rotateBackSide(self)
				rotateS(self)
				rotateS(self)
				rotateS(self)
			elif key=="Zi":
				rotateFrontSide(self)
				rotateBackSide(self)
				rotateBackSide(self)
				rotateBackSide(self)
				rotateS(self)
			elif key=="Z2":
				rotateFrontSide(self)
				rotateFrontSide(self)
				rotateBackSide(self)
				rotateBackSide(self)
				rotateS(self)
				rotateS(self)
			else:
				print "unknown character : "+key
				
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
		C1=self.boxAt(0,0,1).xz.color==FaceColor.front.color and self.boxAt(2,0,1).xz.color==FaceColor.front.color
		C2=self.boxAt(0,0,1).yz.color==FaceColor.left.color and self.boxAt(0,2,1).yz.color==FaceColor.left.color
		C3=self.boxAt(0,2,1).xz.color==FaceColor.back.color and self.boxAt(2,2,1).xz.color==FaceColor.back.color
		C4=self.boxAt(2,2,1).yz.color==FaceColor.right.color and self.boxAt(2,0,1).yz.color==FaceColor.right.color
		return (C1 and C2 and C3 and C4)
	def boxAt(self,x,y,z):
		for box in self.boxes:
			if box.pos==(x,y,z):
				return box
	
	def solve(self):
		return solveTheCube(self)
		
if __name__=="__main__":
	import main

'''Supplies the artificial intelligence for the cube solver'''
from headers import *
from referenceToAlgorithm import Algorithm
from box import *
Algo=Algorithm()
import time

def optimizeMoves(moves):
	chars=["F","B","L","R","U","D","X","Y","Z","M","E","S"]
	opps=["Fi",'Bi','Li','Ri','Ui','Di',"Xi","Yi","Zi","Mi","Ei","Si"]
	moves=moves.replace("'","i")
	moves=" "+moves+" " #add space in front and last, so the spaces are not ommited
	initial=moves
	
	while "  " in  moves:
		moves=moves.replace("  ","")
	
	#remove 2s from the text
	if "2" in moves:
		for i in range(len(chars)):
			moves=moves.replace(" {0}2 ".format(chars[i])," {0} {0} ".format(chars[i]))
			
	for i in range(len(chars)):
		cor=chars[i]
		opp=opps[i]
		
		#remove DDDD
		moves=moves.replace(" {0} {0} {0} {0} ".format(cor) ," ")
		moves=moves.replace(" {0} {0} {0} {0} ".format(opp) ,"")
		
		#remove FFi and FiF
		moves=moves.replace(" {0} {1} ".format(cor,opp), " ")
		moves=moves.replace(" {1} {0} ".format(cor,opp), " ")
		
		#change DDD to Di
		moves=moves.replace(" {0} {0} {0} ".format(opp)," {0} ".format(cor))
		moves=moves.replace(" {0} {0} {0} ".format(cor)," {0} ".format(opp))
	
	if moves != initial:#change has been made, recursion goes now
		moves=optimizeMoves(moves)
	
	#if no change, now go for adding 2s for FF,etc
	for i in range(len(chars)):
		cor=chars[i]
		opp=opps[i]
		
		#change FiFi and FF to F2 
		moves=moves.replace(" {0} {0} ".format(opp), " {0}2 ".format(cor))
		moves=moves.replace(" {0} {0} ".format(cor), " {0}2 ".format(cor))
	
	#trim moves
	moves=moves.lstrip().rstrip()
	
	return moves
	
def solveTheCube(cube):
	'''Solves the scrambled cube.
	Also returns the answer.
	The method of solving: solve base cross, solve base corners, solve second layer, 
	solve top cross, solve top plane,
	solve center pieces of the side of top plane, colve the corner pieces of top plane and DONE!!!
	'''
	ini=time.time()
	cube.original=deepcopy(cube.boxes)
	
	cube.resetMoves()
	initial= time.time()
	
	print "getting best solved side"
	bestSide=chooseBestSolvedSide(cube)
	
	print "orienting the cube to %s as base"%str(bestSide)
	orientCube(cube,bestSide)
	FaceColor.update(cube.getFaceUpdater())
	
	print "getting base cross"
	bringCrossPiecesInPositon(cube)
	
	print "matching them with their respective sides"
	solveBaseCross(cube)
	
	print "getting the base corner pieces in position"
	bringBaseCornersInPosition(cube)
	
	
	print "Solving second level"
	solveSecondLevel(cube)
	
	print "Solving OLL cross"
	solveOllCross(cube)
	
	print "solving OLL plane"
	solveOllPlane(cube)
	
	
	print "solving PLL centre pieces"
	solvePLLCenterPieces(cube)
	
	print "solving PLL corner pieces"
	solvePLLCornerPieces(cube)
	
	print "BAAM !!!"
	print "SOLVED in %0.2f seconds"%(time.time()-ini)

	moves=cube.getMoves()	
	cube.resetMoves()
	cube.boxes=cube.original
	return moves
def getCrossCellsCount(cube,side):
	'''Returns the number of same boxes in the given side, respective to the middle color.'''
	boxes=cube.getSide(side)
	
	#get the color of the centre box
	for box in boxes:
		if box.pos[0]==1 and box.pos[1]==1:
			color=box.xy
			
	count=0	#count of the number of boxes in cross including the middle piece
	
	#now count the boxes of the cross that match to their boss(centre)
	for box in boxes:
		if box.pos[0]==1 or box.pos[1]==1:
			if box.xy.color==color.color:
				count += 1
	return count
	
def chooseBestSolvedSide(cube):
	'''Chooses the best side fit to be the base.'''
	array=[]
	actions=["","Xi","Xi","Xi","Z","Z2"]
	for action in actions:
		cube.action(action)
		array.append([str(cube.boxAt(1,1,0).xy),getCrossCellsCount(cube,BOTTOM_SIDE)])
			
	highest=["green",0]
	for item in array:
		if item[1]>highest[1]:
			highest=[item[0],item[1]]

	return highest[0]
	
def orientCube(cube,side):
	count=0
	while not str(cube.boxAt(1,1,0).xy)==side:
		if count >=4: break
		count += 1
		cube.action("Z")
	
	while not str(cube.boxAt(1,1,0).xy)==side:
		cube.action("Xi")	
	
def solvePLLCornerPieces(cube):
	'''Solves the 4 center pieces of top layer(PLL).
	The OLL is solved. now the PLL center pieces are solved. 
	Remember: the pieces of corner pieces in PLL are affected.'''	
	corners=cube.getSide(TOP_SIDE)
	
	#position the front-left-top box
	#find front-left-top piece
	for item in corners:
		if item.hasColor(FaceColor.left,FaceColor.front):
			break
	#positioning
	
	if not item.pos==(0,0,2):
		#get the item in (2,0,2)
		while not cube.boxAt(2,0,2).hasColor(FaceColor.left,FaceColor.front):
			cube.action("Ri F Ri B B R Fi Ri B B R R")
		
		cube.action("Ui")
		cube.action("Ri F Ri B B R Fi Ri B B R R")
		cube.action("U")
	#solved the piece of (0,0,2)
	
	while not cube.boxAt(2,0,2).xz.color==FaceColor.front.color:
		cube.action("Ri F Ri B B R Fi Ri B B R R")

def solvePLLCenterPieces(cube):
	'''Solves the 4 last remaining corner boxes of PLL.'''
	
	#rotate top so that front comes to the centre
	while not(cube.boxAt(1,0,2).xz.color==FaceColor.front.color):
		cube.action("U")
	
	while True:
		#get the remaining centre pieces
		left=cube.boxAt(0,1,2).yz
		right=cube.boxAt(2,1,2).yz
		back=cube.boxAt(1,2,2).xz
		if left.color==FaceColor.left.color and right.color==FaceColor.right.color:
			break
		elif left.color==FaceColor.left.color:
			#flip back and right
			cube.action("R' U R' U' B' D B' D' B B R' B' R B R")
			continue
		elif right.color==FaceColor.right.color:
			#flip back and left
			cube.action("F R U' R' U' R U R' F' R U R' U' R' F R F'")
		elif right.color==FaceColor.left.color and left.color==FaceColor.right.color:
			#flip left and right
			cube.action("R U R' U' R' F R R U' R' U' R U R' F'")
		elif right.color==FaceColor.left.color and left.color==FaceColor.back.color:
			#back->right, right->left, left->back
			cube.action("R' U R' U' R' U' R' U R U R R")
		elif right.color==FaceColor.back.color and left.color==FaceColor.right.color:
			#back->left, left->right, right-> back
			cube.action("R R U' R' U' R U R U R U' R ")
		else:
			raise SystemError("PLL ERROR")

def solveOllPlane(cube):
	'''Solves the oll layer given that the OLL cross is already formed.
	Is computed before PLL and after F2L.'''
	answer=""
	#read the 4 corner pieces
	pieces=[(0,0,2),(2,0,2),(0,2,2),(2,2,2)]
	
	while True:#check if solved
		boxes=[]
		for box in cube.boxes:
			if box.pos in pieces:
				boxes.append(box);
			
		count=0
		for box in boxes:
			if box.xy.color==FaceColor.top.color:
				count += 1
		if count==4: break
		
		#solve if it is just plus, no other cells above
		if count==0:
			while True:
				if cube.boxAt(2,0,2).yz.color==FaceColor.top.color and not(cube.boxAt(0,0,2).xz.color==FaceColor.top.color):
					cube.action("R U Ri U R U U Ri")
					break
				else:
					cube.action("U")
			continue

		if count==1: #my best part of OLL. only one piece at top, so bring it to the right-bottom corner
			
			while not (cube.boxAt(2,0,2).xy.color==FaceColor.top.color):
				cube.action("U")
			
			if cube.boxAt(0,0,2).xz.color==FaceColor.top.color:
				#the piece at its left is facing us
				
				cube.action("Li U R Ui L U Ri")
				
			else:
				cube.action("Ri U U R U Ri U R")
				cube.action("R' F' L F R F' L' F")
			continue#update the count
		elif count==2:
			#check if 1 or 2 or 3 from (3rd last)http://www.solve-the-cube.com/advanced
			#Section(Cross)
			unmatched=[]
			for box in boxes:
				if box.xy.color==FaceColor.top.color:
					pass
				else:
					unmatched.append(box)
			xDiff=abs(unmatched[0].pos[0]-unmatched[1].pos[0])
			yDiff=abs(unmatched[0].pos[1]-unmatched[1].pos[1])
			if xDiff+yDiff==4:
				#condition 2
				while not(cube.boxAt(0,0,2).yz.color==FaceColor.top.color):
					cube.action("U")
				cube.action("R' F' L' F R F' L F")
			else:
				while not (cube.boxAt(2,0,2).xz.color==FaceColor.top.color):
					cube.action("U")
				#check if condition 1 or condition 3
				if cube.boxAt(0,0,2).xz.color==FaceColor.top.color:
					#condition 3
					cube.action("R R D R' U U R D' R' U U R'")
				else:
					#condition 1
					cube.action("R' F' L F R F' L' F")
		else:
			raise SystemError("error. DONOT IGNORE")
		break
		
	return answer

def getOLLCrossShape(cube):
	'''Returns the current shape if OLL.
	Given that F2l is complete and all top items are in the top layer.'''

	solved=getCrossCellsCount(cube,TOP_SIDE)
	if solved==1:
		return "."
	elif solved==5:
		return "+"
	else:
		return "- or L"
		
def solveOllCross(cube):
	'''Solves the OLL cross.'''
	shape=getOLLCrossShape(cube)
	if shape=="+":
		return ""
	if shape==".":
		cube.action(Algo.getOllPointSolver())
	elif "-" in shape or "L" in shape:
		answer=Algo.getOllMinusOrPlusSolver(cube)
		cube.action(answer)#solves the L in OLL
		
def solveSecondLevel(self):
	'''Solves the second layer.
	Given that the base corner pieces are already in their correct position.'''
	piecesThatCanHold=[(0,0,1),(0,2,1),(2,0,1),(2,2,1),(1,0,2),(1,2,2),(0,1,2),(2,1,2)]
	#solve the pieces that are in the top position
	#if f2l-second phase complete:break
	#else:
		#bring the pieces of the corners which are unmatched to the top
	sides=[(0,0,1),(0,2,1),(2,0,1),(2,2,1)]
	while True:
		
		pieces=self.findAllWithout(piecesThatCanHold,FaceColor.top)
		
		assert(len(pieces)==4);
		i=0
		while i<len(pieces):
			
			box=pieces[i]
			pos=box.pos
			if pos[2]==1:
				i=i+1
				continue#lies on the first line
			
			answer=Algo.getAnswerForf2lSecondLineTransformation("f2l-secondLineSolve",box)
			
			
			self.action(answer)
			
			pieces=self.findAllWithout(piecesThatCanHold,FaceColor.top)
			
			i=0
		if self.f2lSecondPhaseComplete():
			break
		else:
			for side in sides:
				if not self.isSolvedAt(side):
					answer= Algo.getAnswerForF2lSecondLineBringBoxToTopTransformation(side)
					self.action(answer)
				

def bringCrossPiecesInPositon(self):
	'''Brings cross pieces of base layer in position.
	Are flipped correctly too.'''
	while True:
		boxes=[]
		for	box in self.boxes:
			if box.hasColor(FaceColor.bottom) and box.getType()==SIDE_BOX:
				boxes.append(box)
		
		assert(len(boxes)==4)
		#boxes has the 4 white side_piece boxes
	
		update=False
		for box in boxes:
			pos=box.pos
			if pos[2]==0:
				#print "base"
				pass
			elif pos[2]==2:
				#bring to (1,0,2)
				while not self.boxAt(1,0,2).hasColor(FaceColor.bottom):
					self.action("U")
				#empty at (1,0,0)
				while self.boxAt(1,0,0).hasColor(FaceColor.bottom):
					self.action("D")
				self.action("F F")
				#bring the cube from top to bottom line
				update=True
				break
			else:
				update=True
				if box.pos[0]==0 and box.pos[1]==0:
					self.action("F U Fi")
				elif box.pos[0]==0 and box.pos[1]==2:
					self.action("L U Li")
				elif box.pos[0]==2 and box.pos[1]==0:
					self.action("R U Ri")
				elif box.pos[0]==2 and box.pos[1]==2:
					self.action("Ri U R")
				else:
					raise SystemError("INVALID EXCEPTION")
				break
		
		if update: continue
		boxes=self.getSide(BOTTOM_SIDE)
		centers=[]
		for item in boxes:
			if item.getType()==SIDE_BOX:
				centers.append(item)
		
		for item in centers:
			while not item.pos==(1,0,0):
				self.action("D")
			if not(self.boxAt(1,0,0).xy.color==FaceColor.bottom.color):
				self.action("F Di L")
		break
						
def solveBaseCross(self):
	'''Solves the side pairs of the cross with their centre pieces.
	Given that the cross is formed and all the base pieces in the cross are of the same color.'''
	
	a1=self.boxAt(0,1,0).yz
	

	while not self.boxAt(0,1,0).yz.color==FaceColor.left.color:
		self.action("D")
	# piece 1 solved: FaceColor.left matched
	
	#front piece
	if self.boxAt(1,0,0).xz.color==FaceColor.front.color:
		pass
	else:
		if self.boxAt(2,1,0).yz.color==FaceColor.front.color:
			self.action("F F U' R R U F F")
		else:
			self.action("F F U' U' B B U U F F")
	#front matched
	
	#right piece
	if self.boxAt(2,1,0).yz.color==FaceColor.right.color:
		pass
	else:
		self.action("R R U' B B U R R")
	#the back piece is automatically correct since the others are correct
	return
	
def bringBaseCornersInPosition(self):
	'''Brings the base corners in position and also flips them correctly.'''
	#get the corner pieces with white in them
	corners=self.findAll(CORNER_PIECES,FaceColor.bottom)
	assert(len(corners)==4);
	
	
	#piece of (0,0,0) as corner, process it
	for corner in corners:
		if corner.hasColor(FaceColor.left,FaceColor.front):
			break
	pos=corner.pos
	if pos == (0,0,0):
		#already on place
		pass
	else:
		
		#misplaced, bring it to (0,0,2), above the line
		if pos[2]==0: #lies on another corner
			if pos[0]==0:
				#lies on (0,2,0)
				
				self.action("L U' L' U'")
				#brings on above the line
			else:
				#lies on either of the right base corners of the cube
				if pos[1]==2:#lies on (2,2,0)
					self.action("R' U' R U'")
				else:
					#lies on (2,0,0)
					self.action("F' U F U")
		else:
			while not self.boxAt(0,0,2).hasColor(FaceColor.left,FaceColor.front,FaceColor.bottom):
				self.action("U")
			#came above the line
			#now send it down
		self.action("L' U' L")
	assert(self.boxAt(0,0,0).hasColor(FaceColor.bottom,FaceColor.front,FaceColor.left))
	#now flip it to the right orientation
	while not (self.boxAt(0,0,0).xy.color == FaceColor.bottom.color and self.boxAt(0,0,0).hasColor(FaceColor.front,FaceColor.left)):
		self.action("L' U' L U")
	assert(self.boxAt(0,0,0).hasColor(FaceColor.bottom,FaceColor.front,FaceColor.left))
	#solved of (0,0,0)
	
	
	
	#piece of (0,2,0) as corner, process it
	
	for corner in corners:
		if corner.hasColor(FaceColor.left,FaceColor.back):
			#print corner.pos
			break
	pos=corner.pos
	if pos == (0,2,0):
		#already on place
		pass
	else:
		#misplaced, bring it to (0,2,2), above the line
		if pos[2]==0: #lies on either of the corners
			if pos[1]==2:#lies on (2,2,0)
				self.action("R' U' R")
			else:
				#lies on (2,0,0)
				self.action("F' U U F")
		else:
			while not self.boxAt(0,2,2).hasColor(FaceColor.left,FaceColor.back,FaceColor.bottom):
				self.action("U")
		#came above the line
		#now send it down
		self.action("L U L'")
	
	assert(self.boxAt(0,2,0).hasColor(FaceColor.bottom,FaceColor.left,FaceColor.back))
	#now flip it to the right orientation
	while not (self.boxAt(0,2,0).xy.color == FaceColor.bottom.color and self.boxAt(0,2,0).hasColor(FaceColor.back,FaceColor.left)):
		self.action("L U L' U'")
	#solved of (0,2,0)
	assert(self.boxAt(0,2,0).hasColor(FaceColor.bottom,FaceColor.left,FaceColor.back))
	
	
	for corner in corners:
		if corner.hasColor(FaceColor.right,FaceColor.back):
			break
	#piece of (2,2,0) as corner, process it
	pos=corner.pos
	if pos == (2,2,0):
		#already on place
		pass
	else:
		#misplaced, bring it to (2,2,2), above the line
		if pos[2]==0: #lies on (2,0,0)
			self.action("F' U' F")
		else:
			while not self.boxAt(2,2,2).hasColor(FaceColor.right,FaceColor.back,FaceColor.bottom):
				self.action("U")
		#came above the line
		#now send it down
		self.action("R' U' R")
	assert(self.boxAt(2,2,0).hasColor(FaceColor.bottom,FaceColor.back,FaceColor.right))
	#now flip it to the right orientation
	while not (self.boxAt(2,2,0).xy.color == FaceColor.bottom.color and self.boxAt(2,2,0).hasColor(FaceColor.back,FaceColor.right)):
		self.action("R' U R U'")
	assert(self.boxAt(2,2,0).hasColor(FaceColor.bottom,FaceColor.back,FaceColor.right))
	#solved of (2,2,0)
	
	
	for corner in corners:
		if corner.hasColor(FaceColor.right,FaceColor.front):
			break
	#piece of (2,0,0) as corner, process it
	pos=corner.pos
	
	if pos==(2,0,0):
		#alread on place
		pass
	else:
		while not self.boxAt(2,0,2).hasColor(FaceColor.bottom):
			self.action("U")
		self.action("R U R'")
	
	assert(self.boxAt(2,0,0).hasColor(FaceColor.bottom,FaceColor.right,FaceColor.front))
	while not (self.boxAt(2,0,0).xy.color == FaceColor.bottom.color and self.boxAt(2,0,0).hasColor(FaceColor.front,FaceColor.right)):
		self.action("R U R' U'")
	assert(self.boxAt(2,0,0).hasColor(FaceColor.bottom,FaceColor.right,FaceColor.front))
	#solved of (2,0,0)
	return
	
if __name__=="__main__":
	import main

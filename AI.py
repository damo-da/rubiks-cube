'''Supplies the artificial intelligence for the cube solver'''
from headers import *
from referenceToAlgorithm import Algorithm
from box import *
Algo=Algorithm()
import time

def optimizeMoves(moves,recursion=True):
	chars=["F","B","L","R","U","D"]
	opps=["f",'b','l','r','u','d']
	moves=moves.replace("'","i")
	moves=moves.replace(" ","")
	for i in range(len(chars)):moves=moves.replace(chars[i]+"i",opps[i])
	
	for i in range(len(chars)):
		cor=chars[i]
		opp=opps[i]
		
		#remove DDDD
		moves=moves.replace(cor*4,"")
		moves=moves.replace(opp*4,"")
		
		#change DDD to Di
		moves=moves.replace(cor*3,opp)
		moves=moves.replace(opp*3,cor)
		
		
		#remove FFi and FiF
		moves=moves.replace(cor+opp,"")
		moves=moves.replace(opp+cor,"")
		
		#UU into U2
		moves=moves.replace(opp*2,opp+"2")
		moves=moves.replace(cor*2,cor+"2")
	
	ret=""
	index=0
	while index<len(moves):
		char=moves[index]
		repeat=""
		if index!=len(moves)-1: #check for 2
			if moves[index+1] == "2":
				repeat="2"
				index += 1
		
		if char in opps :
			#print chars[opps.index(char)-1]
			char=chars[opps.index(char)]
			if not repeat:
				char += "i"
		ret += char+repeat+ " "
		index += 1
	if recursion:
		ret1=optimizeMoves(ret,recursion=False)
		while not ret==ret1:
			ret=ret1
			ret1=optimizeMoves(ret,recursion=False)
	return ret
	
def z(cube):
	print cube.move
	move=cube.getMoves()
	print move
	cube.resetMoves()
	raw_input()
	
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
	print "getting cross of white"
	bringCrossPiecesInPositon(cube)
	
	print "matching them with their respective sides"
	solveBaseCross(cube)
	
	print "getting the corner pieces in position"
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

def solvePLLCornerPieces(cube):
	'''Solves the 4 center pieces of top layer(PLL).
	The OLL is solved. now the PLL center pieces are solved. 
	Remember: the pieces of corner pieces in PLL are affected.'''	
	corners=cube.getSide(TOP_SIDE)
	
	#position the green,red,yellow box
	#find green,red,yellow piece
	for item in corners:
		if item.hasColor(RED,GREEN):
			break
	#positioning
	
	if not item.pos==(0,0,2):
		#get the item in (2,0,2)
		while not cube.boxAt(2,0,2).hasColor(RED,GREEN):
			cube.action("Ri F Ri B B R Fi Ri B B R R")
		
		cube.action("Ui")
		cube.action("Ri F Ri B B R Fi Ri B B R R")
		cube.action("U")
	#solved the piece of (0,0,2)
	
	while not cube.boxAt(2,0,2).xz.color==GREEN.color:
		cube.action("Ri F Ri B B R Fi Ri B B R R")

def solvePLLCenterPieces(cube):
	'''Solves the 4 last remaining corner boxes of PLL.'''
	
	#rotate top so that green centre comes to the centre
	while not(cube.boxAt(1,0,2).xz.color==GREEN.color):
		cube.action("U")
	
	while True:
		#get the remaining centre pieces
		left=cube.boxAt(0,1,2).yz
		right=cube.boxAt(2,1,2).yz
		back=cube.boxAt(1,2,2).xz
		if left.color==RED.color and right.color==ORANGE.color:
			break
		elif left.color==RED.color:
			#flip blue and orange
			cube.action("R' U R' U' B' D B' D' B B R' B' R B R")
			continue
		elif right.color==ORANGE.color:
			#flip blue and red
			cube.action("F R U' R' U' R U R' F' R U R' U' R' F R F'")
		elif right.color==RED.color and left.color==ORANGE.color:
			#flip red and orange
			cube.action("R U R' U' R' F R R U' R' U' R U R' F'")
		elif right.color==RED.color and left.color==BLUE.color:
			#back->right, right->left, left->back
			cube.action("R' U R' U' R' U' R' U R U R R")
		elif right.color==BLUE.color and left.color==ORANGE.color:
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
			if box.xy.color==YELLOW.color:
				count += 1
		if count==4: break
		
		#solve if it is just plus, no other cells above
		if count==0:
			while True:
				if cube.boxAt(2,0,2).yz.color==YELLOW.color and not(cube.boxAt(0,0,2).xz.color==YELLOW.color):
					cube.action("R U Ri U R U U Ri")
					break
				else:
					cube.action("U")
			continue

		if count==1: #my best part of OLL. only one piece at top, so bring it to the right-bottom corner
			
			while not (cube.boxAt(2,0,2).xy.color==YELLOW.color):
				cube.action("U")
			
			if cube.boxAt(0,0,2).xz.color==YELLOW.color:
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
				if box.xy.color==YELLOW.color:
					pass
				else:
					unmatched.append(box)
			xDiff=abs(unmatched[0].pos[0]-unmatched[1].pos[0])
			yDiff=abs(unmatched[0].pos[1]-unmatched[1].pos[1])
			if xDiff+yDiff==4:
				#condition 2
				while not(cube.boxAt(0,0,2).yz.color==YELLOW.color):
					cube.action("U")
				cube.action("R' F' L' F R F' L F")
			else:
				while not (cube.boxAt(2,0,2).xz.color==YELLOW.color):
					cube.action("U")
				#check if condition 1 or condition 3
				if cube.boxAt(0,0,2).xz.color==YELLOW.color:
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
	Given that F2l is complete and all yellow items are in the top layer.'''
	
	boxes=cube.getSide(TOP_SIDE)
	solved=0
	for box in boxes:
		if box.xy.color==YELLOW.color and (isinstance(box,SideBox) or isinstance(box,CenterBox)):
			solved += 1
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
		
		pieces=self.findAllWithout(piecesThatCanHold,YELLOW)
		
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
			
			pieces=self.findAllWithout(piecesThatCanHold,YELLOW)
			
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
			if box.hasColor(WHITE) and box.getType()==SIDE_BOX:
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
				while not self.boxAt(1,0,2).hasColor(WHITE):
					self.action("U")
				#empty at (1,0,0)
				while self.boxAt(1,0,0).hasColor(WHITE):
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
			if not(self.boxAt(1,0,0).xy.color==WHITE.color):
				self.action("F Di L")
		break
						
def solveBaseCross(self):
	'''Solves the side pairs of the cross with their centre pieces.
	Given that the cross is formed and all the base pieces in the cross are of the same color.'''
	
	a1=self.boxAt(0,1,0).yz
	

	while not self.boxAt(0,1,0).yz.color==RED.color:
		self.action("D")
	# piece 1 solved: RED matched
	
	#green piece
	if self.boxAt(1,0,0).xz.color==GREEN.color:
		pass
	else:
		if self.boxAt(2,1,0).yz.color==GREEN.color:
			self.action("F F U' R R U F F")
		else:
			self.action("F F U' U' B B U U F F")
	#green matched
	
	#orange piece
	if self.boxAt(2,1,0).yz.color==ORANGE.color:
		pass
	else:
		self.action("R R U' B B U R R")
	#the blue piece is automatically correct since the others are correct
	return
	
def bringBaseCornersInPosition(self):
	'''Brings the base corners in position and also flips them correctly.'''
	#get the corner pieces with white in them
	corners=self.findAll(CORNER_PIECES,WHITE)
	assert(len(corners)==4);
	
	
	#piece of (0,0,0) as corner, process it
	for corner in corners:
		if corner.hasColor(RED,GREEN):
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
			while not self.boxAt(0,0,2).hasColor(RED,GREEN,WHITE):
				self.action("U")
			#came above the line
			#now send it down
		self.action("L' U' L")
	assert(self.boxAt(0,0,0).hasColor(WHITE,GREEN,RED))
	#now flip it to the right orientation
	while not (self.boxAt(0,0,0).xy.color == WHITE.color and self.boxAt(0,0,0).hasColor(GREEN,RED)):
		self.action("L' U' L U")
	assert(self.boxAt(0,0,0).hasColor(WHITE,GREEN,RED))
	#solved of (0,0,0)
	
	
	
	#piece of (0,2,0) as corner, process it
	
	for corner in corners:
		if corner.hasColor(RED,BLUE):
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
			while not self.boxAt(0,2,2).hasColor(RED,BLUE,WHITE):
				self.action("U")
		#came above the line
		#now send it down
		self.action("L U L'")
	
	assert(self.boxAt(0,2,0).hasColor(WHITE,RED,BLUE))
	#now flip it to the right orientation
	while not (self.boxAt(0,2,0).xy.color == WHITE.color and self.boxAt(0,2,0).hasColor(BLUE,RED)):
		self.action("L U L' U'")
	#solved of (0,2,0)
	assert(self.boxAt(0,2,0).hasColor(WHITE,RED,BLUE))
	
	
	for corner in corners:
		if corner.hasColor(ORANGE,BLUE):
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
			while not self.boxAt(2,2,2).hasColor(ORANGE,BLUE,WHITE):
				self.action("U")
		#came above the line
		#now send it down
		self.action("R' U' R")
	assert(self.boxAt(2,2,0).hasColor(WHITE,BLUE,ORANGE))
	#now flip it to the right orientation
	while not (self.boxAt(2,2,0).xy.color == WHITE.color and self.boxAt(2,2,0).hasColor(BLUE,ORANGE)):
		self.action("R' U R U'")
	assert(self.boxAt(2,2,0).hasColor(WHITE,BLUE,ORANGE))
	#solved of (2,2,0)
	
	
	
	for corner in corners:
		if corner.hasColor(ORANGE,GREEN):
			break
	#piece of (2,0,0) as corner, process it
	pos=corner.pos
	
	if pos==(2,0,0):
		#alread on place
		pass
	else:
		while not self.boxAt(2,0,2).hasColor(WHITE):
			self.action("U")
		self.action("R U R'")
	
	assert(self.boxAt(2,0,0).hasColor(WHITE,ORANGE,GREEN))
	while not (self.boxAt(2,0,0).xy.color == WHITE.color and self.boxAt(2,0,0).hasColor(GREEN,ORANGE)):
		self.action("R U R' U'")
	assert(self.boxAt(2,0,0).hasColor(WHITE,ORANGE,GREEN))
	#solved of (2,0,0)
	return
	
if __name__=="__main__":
	import main

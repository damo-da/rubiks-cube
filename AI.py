'''Supplies the artificial intelligence for the cube solver'''
from headers import *
from referenceToAlgorithm import Algorithm
from box import *
Algo=Algorithm()
import time

    
def solveTheCube(cube):
    '''Returns the algorithm for solving the cube.'''
    cube.stopRecording()
    cube.original=copyCube(cube.boxes)
    cube.resetMoves()
    
    initial= time.time()
    cube.updateFaceColors();
    chooseBestSide(cube);
    solveCross(cube)
    solveF2L(cube)
    solveOLL(cube)
    solvePLL(cube)
    
    print "BAAM !!!"
    timeTaken=time.time()-initial
    with open("time.txt","a") as f:
        f.write("%s\n"%timeTaken)
    print "SOLVED in %0.2f seconds"%(timeTaken)
    
    moves=cube.getMoves()    
    cube.resetMoves()
    cube.boxes=cube.original
    cube.startRecording()
    
    return moves
    
def chooseBestSide(cube):
    print "getting best solved side"
    bestSide=chooseBestSolvedSide(cube)

    print "orienting the cube to %s as base"%str(bestSide)
    orientCube(cube,bestSide)
    cube.updateFaceColors();
    
def solveCross(cube):
    print "getting base cross"
    bringCrossPiecesInPositon(cube)
    
    print "matching them with their respective sides"
    solveBaseCross(cube)
def solveF2L(cube):
    print "getting the base corner pieces in position"
    bringBaseCornersInPosition(cube)
    
    print "Solving second level"
    solveSecondLevel(cube)
def solveOLL(cube):
    #get the structure of the oll cross.
    
    #coded from solve-the-cube.com, advanced.html
    #structuremode
        #point 
            #all_corners
            #line
                #T
                #Z
                #C
                #bigL
            #littleL
                #cross
                #W
                #P
    
    if cube.OLLsolved(): return
    top=FaceColor.top    
    
    C1=cube.boxAt(0,0,2).xy.color==top.color;
    C1=C1 and cube.boxAt(2,0,2).xy.color==top.color;
    C1=C1 and cube.boxAt(0,2,2).xy.color==top.color;
    C1=C1 and cube.boxAt(2,2,2).xy.color==top.color;
    
    if C1:
        #all corners solved
        print "CORNER MODE";
        
        unsolved_side_pieces=0
        for box in cube.getSide(TOP_SIDE):
            if box.getType()=="side_box":
                if not(box.xy.color==top.color):
                    unsolved_side_pieces += 1;
        if unsolved_side_pieces==4:
            #type(27)
            cube.action("M' U2 M U2 M' U M U2 M' U2 M");
            return;
        C2=cube.boxAt(1,0,2).xy.color==top.color
        C2= C2 and cube.boxAt(1,2,2).xy.color==top.color
        if C2:
            cube.action("U");
        
        C3=cube.boxAt(0,1,2).xy.color==top.color
        C3= C3 and cube.boxAt(2,1,2).xy.color==top.color
        if C3:
            cube.action("Li R U Ri Ui L Ri F R Fi");
        else:
            #not two opposite side unsolved pieces
            while not(cube.boxAt(0,1,2).xy.color==top.color and cube.boxAt(1,0,2).xy.color==top.color):
                cube.action("U");
            cube.action("Mi Ui M U2 Mi Ui M");
        return None
    
    #check for a line, a horizontal one at the 2nd row
    if(cube.boxAt(0,1,2).xy.color==top.color and cube.boxAt(2,1,2).xy.color==top.color):
        cube.action("U");
    
    #check for a vertical line
    if(cube.boxAt(1,0,2).xy.color==top.color and cube.boxAt(1,2,2).xy.color==top.color):
        if (cube.boxAt(0,1,2).xy.color==top.color and cube.boxAt(2,1,2).xy.color==top.color):#a cross
            #find how many pieces of corner pieces of OLL are already in place
            num=0;
            boxes=cube.getSide(TOP_SIDE);
            for box in boxes:
                if box.getType()=="corner_box":
                    if box.xy.color==top.color:
                        num += 1;
            
            if num==0:
                #no piece is correct.
                while not(cube.boxAt(2,0,2).yz.color==top.color):
                    cube.action("U");
                
                if (cube.boxAt(0,0,2).yz.color==top.color and cube.boxAt(2,2,2).yz.color==top.color):
                    #type(7)
                    cube.action("R U R' U R U' R' U R U2 R'")
                else:
                    #type(6)
                    if cube.boxAt(0,0,2).yz.color==top.color:
                        cube.action("U");
                    
                    cube.action("L U' R' U L' U R U R' U R");
            elif num==1:
                #a sigle piece solved.
                while not(cube.boxAt(2,0,2).xy.color==top.color):
                    cube.action("U");
                if cube.boxAt(0,0,2).yz.color==top.color:
                    #type(8)
                    cube.action("R' U2 R U R' U R")
                    
                else:
                    #type is #(9)
                    cube.action("L' U R U' L U R'")
            elif num==2:
                #2 pieces solved
                while not (cube.boxAt(0,0,2).xy.color==top.color and cube.boxAt(2,0,2).xy.color!=top.color):
                    cube.action("U");
                if cube.boxAt(0,2,2).xy.color!=top.color:
                    while not(cube.boxAt(2,2,2).xz.color==top.color):
                        cube.action("U");
                    #type is now #(10)
                    cube.action("R' F' L' F R F' L F")
                elif cube.boxAt(2,0,2).yz.color==top.color:
                    cube.action("U");
                    #type(11)
                    cube.action("R2 D R' U2 R D' R' U2 R'")
                else:
                    #type(12)
                    cube.action("R' F' L F R F' L' F");
            else:
                print num
                raise SystemError("invalid cube");
            return;
        else:
            # "no cross";
            
            number=0;
            for box in cube.getSide(TOP_SIDE):
                if box.getType()=="corner_box":
                    if box.xy.color==top.color:
                        number += 1;
            if number==0:
                #just a vertical line
                
                left_yz_solved_count=0;
                right_yz_solved_count=0;
                for box in cube.getSide(TOP_SIDE):
                    if box.getPos()[0]==0:
                        if box.yz.color==top.color:
                            left_yz_solved_count +=1;
                    elif box.getPos()[0]==2:
                        if box.yz.color==top.color:
                            right_yz_solved_count += 1;
                array=(left_yz_solved_count,right_yz_solved_count);
                
                if array==(2,2):
                    while not(cube.boxAt(0,0,2).xz.color==top.color and cube.boxAt(1,0,2).xz.color==top.color):
                        cube.action("U");
                    #"type 15";
                    cube.action("F U R U' R' U R U' R' F'")
                elif array==(3,1) or array==(1,3):
                    if(array==(3,1)):
                        cube.action("U2");
                    #"type(14)";
                    cube.action("R' U' y L' U L' y' L F L' F R");
                elif array==(3,3):
                    #"type(13)";
                    cube.action("R U2 R2 U' R U' R' U2 F R F'");
                elif array==(1,1):
                    #"type(16)";
                    cube.action("U L' B' L U' R' U R U' R' U R L' B L");
                else:
                    raise SystemError("invalid_line");                
            elif number==1:
                for box in [cube.boxAt(0,0,2),cube.boxAt(0,2,2)]:
                    if box.xy.color==top.color:
                        cube.action("U2");
                        break;
                if cube.boxAt(2,2,2).xy.color==top.color:
                    if cube.boxAt(2,0,2).yz.color==top.color:
                        cube.action("U");
                        cube.action("R' F R U R' F' R y L U' L'");
                    elif cube.boxAt(2,0,2).xz.color==top.color:
                        cube.action("U");
                        cube.action("L' B' L R' U' R U L' B L");
                    else:
                        raise SystemError("unknown Big L");
                elif cube.boxAt(2,0,2).xy.color==top.color:
                    if cube.boxAt(0,0,2).yz.color==top.color:
                        cube.action("U");
                        cube.action("L F' L' U' L F L' y' R' U R");
                    elif cube.boxAt(0,0,2).xz.color==top.color:
                        cube.action("U");
                        cube.action("R B R' L U L' U' R B' R'");
                else:
                    raise SystemError("unknown BigL");
            elif number==2:
                box1=None
                box2=None
                for box in [cube.boxAt(0,2,2),cube.boxAt(2,2,2),cube.boxAt(2,0,2),cube.boxAt(0,0,2)]:
                    if box.xy.color==top.color:
                        if box1:
                            box2=box
                            break
                        else:
                            box1=box
                assert(box1 and box2);
                
                if box1.pos[0]==box2.pos[0]:
                    if box1.pos[0]==2:
                        cube.action("U2");
                    if cube.boxAt(2,2,2).yz.color==top.color:
                        cube.action("R U x' R U' R' U x U' R'");
                    else:
                        cube.action("Ui");
                        cube.action("R U R2 U' R' F R U R U' F'");
                elif box1.pos[1]==box2.pos[1]:
                    if box1.pos[1]==2:
                        cube.action("U2");
                    if cube.boxAt(0,2,2).xz.color==top.color:
                        cube.action("Ui");
                        cube.action("F R U R' U' F'");
                    else:
                        cube.action("Ui");
                        cube.action("R U R' U' R' F R F'");
                else:
                    if cube.boxAt(2,0,2).xy.color==top.color:
                        #type like(26)
                        if not(cube.boxAt(2,2,2).yz.color==top.color and cube.boxAt(2,1,2).yz.color==top.color):
                            cube.action("U2");
                        cube.action("Ui");
                        #type is #26
                        cube.action("L F' L' U' L U F U' L'");
                    else:
                        
                        if not(cube.boxAt(2,0,2).yz.color==top.color and cube.boxAt(2,1,2).yz.color==top.color):
                            cube.action("U2");
                        cube.action("Ui");
                        #type(25)
                        cube.action("R' F R U R' U' F' U R");
            else:
                raise SystemError("OLL ERROR ");
        return;
    
    number=0
    for box in cube.getSide(TOP_SIDE):
        if box.getType()==SIDE_BOX:
            if box.xy.color==top.color:
                number += 1
    if number==3 or number==4:
        raise SystemError("invalid cross shape on oll")
    elif number==2:
        print "little L";
        from algorithms import smallL_oll
        try:
            answer=smallL_oll.getAnswerFor(cube);
            cube.action(answer);
        except:
            raise SystemError("invalid oll in cube");
        return;
    else:
        print "dot";
        from algorithms import dot_oll
        answer=dot_oll.getAnswerFor(cube);
        cube.action(answer);
        
    return;
def solvePLL(cube):
    import algorithms.pll
    answer=algorithms.pll.solve(cube)
    cube.action(answer);
    
    
    
    
    
def getCrossCellsCount(cube,side):
    '''Returns the number of same boxes in the given side, respective to the middle color.'''
    boxes=cube.getSide(side)
    
    #get the color of the centre box
    for box in boxes:
        if box.pos[0]==1 and box.pos[1]==1:
            color=box.xy
            
    count=0    #count of the number of boxes in cross including the middle piece
    
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
        for    box in self.boxes:
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

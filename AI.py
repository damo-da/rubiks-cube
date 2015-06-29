'''Supplies the artificial intelligence for the cube solver.'''

from headers import *
from referenceToAlgorithm import Algorithm
import time
from box import *

#our Algorithm handler
Algo=Algorithm()



def solveTheCube(cube):
    '''Returns the algorithm for solving the cube.'''

    #cube...hmm...we need to stop recording what we are doing to it
    cube.stopRecording()

    #clone it, so that we can not do anything stupid :-)
    cube.original=copyCube(cube.boxes)

    #now, we are gonna set the move log in the cube to be empty
    cube.resetMoves()


    initial_time= time.time()


    #make the cube like a cube with sides.  
    #IE, if yellow is on the bottom side of the cube, we can actually get yellow from Bottom side. Yay!
    cube.updateFaceColors();

    #choose the best possible side for solving
    chooseBestSide(cube);

    #solve the base cross
    solveCross(cube)

    solveF2L(cube)

    solveOLL(cube)
    solvePLL(cube)
    #by now, the cube should be solved

    #calculate and print the total time elapsed
    timeTaken=time.time()-initial_time
    print ("Cube solved in %0.2f seconds"%(timeTaken))

    #log into the time.txt file, the current time elapsed
    with open("time.txt","a") as f:
        f.write("%s\n"%timeTaken)
    
    
    #now read whatever the cube has moved
    moves=cube.getMoves()    

    #stash the moves
    cube.resetMoves()

    #reset the cube boxes
    cube.boxes=cube.original

    #again start recording whatever the user has entered
    cube.startRecording()
    
    #and finally, return the moves that we have made
    return moves
    
def chooseBestSide(cube):
    '''Orients the cube to the side we think is the best for solving.'''

    print ("getting best solved side")
    bestSide=chooseBestSolvedSide(cube)

    print ("orienting the cube to %s as base"%str(bestSide))
    orientCube(cube,bestSide)

    #since we MIGHT have rotated the cube, we need to update the faceColors. 
    #for references like bottom to give Yellow, etc
    cube.updateFaceColors();
    
def solveCross(cube):
    '''Solves the base cross.'''
    #we assume that the bottom is the best side to create a cross on

    #bring the bottom-side pieces to wherever bottom-sides, irrespective of where they belong
    print ("getting base cross")
    bringCrossPiecesInPositon(cube)
    
    print ("matching them with their respective sides")
    solveBaseCross(cube)

def solveF2L(cube):
    '''Solves the first two layers.'''
    #we assume that the base cross is solved

    #solve the first layer
    print ("getting the base corner pieces in position")
    bringBaseCornersInPosition(cube)
    
    #and then the second layer
    print ("Solving second level")
    solveSecondLevel(cube)

def solveOLL(cube):
    '''Optimize the last layer-Solve the top side of the cube.'''
    
    #get the structure of the oll cross.
    
    #coded from solve-the-cube.com, advanced.html
    #all possible structures:
        #point 
            #all_corners -img(61)
            #lineimg(62)
                #T - img(63)
                #Z 
                #C 
                #bigL
            #littleL
                #cross
                #W
                #P
    
    if cube.OLLsolved(): return

    #for easier assessment
    top=FaceColor.top    
    
    #check if all corners are solved or not
    C1=cube.boxAt(0,0,2).xy.color==top.color;
    C1=C1 and cube.boxAt(2,0,2).xy.color==top.color;
    C1=C1 and cube.boxAt(0,2,2).xy.color==top.color;
    C1=C1 and cube.boxAt(2,2,2).xy.color==top.color;
    
    if C1:
        #all corners solved

        #count how many of the side pieces in the top row are solved.
        solved_side_pieces=0
        for box in cube.getSide(TOP_SIDE):
            if box.getType()=="side_box":
                if not(box.xy.color==top.color):
                    solved_side_pieces += 1;

        if solved_side_pieces==4:
            #img(27)
            cube.action("M' U2 M U2 M' U M U2 M' U2 M");
            return;

        #check if there is a vertical line from (1,0) to (1,2) at the top face.
        #if exists, give the cube a "U" turn
        C2=cube.boxAt(1,0,2).xy.color==top.color
        C2=C2 and cube.boxAt(1,2,2).xy.color==top.color

        if C2:
            cube.action("U");
        
        #now check if there is a horizontal line from (0,1) to (2,1)  at the top face

        C3=cube.boxAt(0,1,2).xy.color==top.color
        C3= C3 and cube.boxAt(2,1,2).xy.color==top.color
        if C3:
            # we have a H-bridge at the top, oriented like "H", not like "I"

            cube.action("Li R U Ri Ui L Ri F R Fi");
            return;
        else:
            #not two opposite side unsolved pieces
            #ie, there is no line in the side-row(the middle row)

            #now bring solved pieces to front-top-side piece and to left-top-side piece.
            #notice that we are assuming that since there is not a line,
                #there must be two "adjacent" side pieces that have solved top.color
                #which happens if the cube is actually a working cube
            while not(cube.boxAt(0,1,2).xy.color==top.color and cube.boxAt(1,0,2).xy.color==top.color):
                cube.action("U");

            # we must be looking like img(64)
            cube.action("Mi Ui M U2 Mi Ui M");
            return;
    
    # we are not all_corners now

    # lets check for the existence of a line
    
    # if there is a horizontal line, make it vertical
    if(cube.boxAt(0,1,2).xy.color==top.color and cube.boxAt(2,1,2).xy.color==top.color):
        cube.action("U");
    
    #check for a vertical line
    if(cube.boxAt(1,0,2).xy.color==top.color and cube.boxAt(1,2,2).xy.color==top.color):
        # yeah, a vertical line

        #check if there is a cross
        if (cube.boxAt(0,1,2).xy.color==top.color and cube.boxAt(2,1,2).xy.color==top.color):
            # yes, a cross

            #find how many pieces of corner boxes of OLL are already in place
            num=0;
            boxes=cube.getSide(TOP_SIDE);
            for box in boxes:
                if box.getType()=="corner_box":
                    if box.xy.color==top.color:
                        num += 1;

            if num==0:
                #no corner piece==top.color in top face
                
                # bring a corner piece to front-right-top corner, so that its right side is top.color ANYHOW
                while not(cube.boxAt(2,0,2).yz.color==top.color):
                    cube.action("U");
                

                if (cube.boxAt(0,0,2).yz.color==top.color and cube.boxAt(2,2,2).yz.color==top.color):
                    #type(7)
                    cube.action("R U R' U R U' R' U R U2 R'")
                else:
                    if cube.boxAt(0,0,2).yz.color==top.color:
                        cube.action("U");
                    #type(6)
                    cube.action("L U' R' U L' U R U R' U R");

            elif num==1:
                #one of the corner box==top.color is in top face
                

                #now, bring the solved box at front-right-top
                while not(cube.boxAt(2,0,2).xy.color==top.color):
                    cube.action("U");

                #if the box at front-left-top has top.color on its left side, 
                if cube.boxAt(0,0,2).yz.color==top.color:
                    #type(8)
                    cube.action("R' U2 R U R' U R")
                else:
                    #type is #(9)
                    cube.action("L' U R U' L U R'")
                return;
            elif num==2:
                #two of the corner box==top.color are in top face

                # make front-left-top.top=top.color and front-right-top.top != top.color.
                while not (cube.boxAt(0,0,2).xy.color==top.color and cube.boxAt(2,0,2).xy.color!=top.color):
                    cube.action("U");

                #so that means, that either back-left-top or back-right-top must have top.color in correct place
                if cube.boxAt(0,2,2).xy.color!=top.color:
                    #it means, that back-right-top must be managed. 

                    #not to position xz side to apply the algorithm, use the following
                    while not(cube.boxAt(2,2,2).xz.color==top.color):
                        cube.action("U");

                    #type is now img(10)
                    cube.action("R' F' L' F R F' L F")

                #else, elif, whatever but now it's assured that back-left-top must be correctly oriented
                elif cube.boxAt(2,0,2).yz.color==top.color:                    
                    cube.action("U");
                    #type(11)
                    cube.action("R2 D R' U2 R D' R' U2 R'")

                else:
                    #type(12)
                    cube.action("R' F' L F R F' L' F");
                return;
            else:
                #oops, we have an invalid exception
                raise SystemError("can not solve OLL: invalid cube");

            return;
        else:
            #no cross, no all_corners
            
            #count the number of corner boxes solved correctly oriented
            number=0;
            for box in cube.getSide(TOP_SIDE):
                if box.getType()=="corner_box":
                    if box.xy.color==top.color:
                        number += 1;

            if number==0:
                #no corner boxes properly oriented, no cross, so that leaves just a line

                #note: we made the line vertical already! See above.

                # now check the left and right side of the left and right side rows respectively
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

                    #img(15);
                    cube.action("F U R U' R' U R U' R' F'")

                elif array==(3,1) or array==(1,3):

                    if(array==(3,1)):
                        cube.action("U2");
                    #img(14);
                    cube.action("R' U' y L' U L' y' L F L' F R");

                elif array==(3,3):
                    #img(13);
                    cube.action("R U2 R2 U' R U' R' U2 F R F'");

                elif array==(1,1):
                    #img(16);
                    cube.action("U L' B' L U' R' U R U' R' U R L' B L");

                else:
                    #oops, we reached at an invalid line!
                    raise SystemError("invalid_line");                
                return;

            elif number==1:
                #it is a vertical line and one of the corner box is properly oriented
                #It's a bigL

                #bring the solved piece to right side, but make sure that the vertical line is not destroyed
                for box in [cube.boxAt(0,0,2),cube.boxAt(0,2,2)]:
                    if box.xy.color==top.color:
                        cube.action("U2");
                        break;

                #if back-right-top was correctly oriented,
                if cube.boxAt(2,2,2).xy.color==top.color:
                    if cube.boxAt(2,0,2).yz.color==top.color:
                        cube.action("U");
                        
                        #img(17)
                        cube.action("R' F R U R' F' R y L U' L'");
                    elif cube.boxAt(2,0,2).xz.color==top.color:

                        #img(18)
                        cube.action("U");
                        cube.action("L' B' L R' U' R U L' B L");
                    else:
                        raise SystemError("unknown BigL 1");

                #or now, front-right-top is correctly oriented
                elif cube.boxAt(2,0,2).xy.color==top.color:
                    if cube.boxAt(0,0,2).yz.color==top.color:
                        cube.action("U");

                        #img(19)
                        cube.action("L F' L' U' L F L' y' R' U R");
                    elif cube.boxAt(0,0,2).xz.color==top.color:
                        cube.action("U");

                        #img(20);
                        cube.action("R B R' L U L' U' R B' R'");
                    else:
                        raise SystemError("unknown BigL 2");
                else:
                    raise SystemError("unknown BigL 3");

            elif number==2:
                # there is a vertical line and there are two corner boxes properly oriented

                #get the properly oriented corner boxes
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

                #now we have the boxes
                if box1.pos[0]==box2.pos[0]:
                    #the "C" 
                    # either both are in left or right side.

                    if box1.pos[0]==2:
                        #if both of them are on right side,
                        #Bring both of them to the left
                        cube.action("U2");
                    else:
                        #both of them must not be on the right side.
                        #ie, they are on the left side
                        pass

                    if cube.boxAt(2,2,2).yz.color==top.color:
                        #img(23)
                        cube.action("R U x' R U' R' U x U' R'");
                    else:
                        cube.action("Ui");
                        
                        #img(24)
                        cube.action("R U R2 U' R' F R U R U' F'");

                elif box1.pos[1]==box2.pos[1]:
                    #the "T"

                    #they are not both on the same (left or right) side
                    #but they are both either on front, or no back


                    if box1.pos[1]==2:
                        #if both on back, bring both to front
                        cube.action("U2");


                    if cube.boxAt(0,2,2).xz.color==top.color:
                        cube.action("Ui");
                        #img(21)

                        cube.action("F R U R' U' F'");
                    else:
                        cube.action("Ui");

                        #img(22)
                        cube.action("R U R' U' R' F R F'");
                else:
                    #the "Z"

                    if cube.boxAt(2,0,2).xy.color==top.color:

                        #type like(26)
                        if not(cube.boxAt(2,2,2).yz.color==top.color and cube.boxAt(2,1,2).yz.color==top.color):
                            cube.action("U2");
                        cube.action("Ui");

                        #img(26)
                        cube.action("L F' L' U' L U F U' L'");
                    else:
                        #type like img(25)
                        if not(cube.boxAt(2,0,2).yz.color==top.color and cube.boxAt(2,1,2).yz.color==top.color):
                            cube.action("U2");

                        cube.action("Ui");

                        # img(25)
                        cube.action("R' F R U R' U' F' U R");
            else:
                #oops, unhandled exception
                raise SystemError("OLL line error ERROR. Neither C or T or Z ");
        return;
    
    #no, there is no vertical line. No horizontal either.
    
    #count the number of SIDE_BOX that are correctly oriented
    number=0
    for box in cube.getSide(TOP_SIDE):
        if box.getType()==SIDE_BOX:
            if box.xy.color==top.color:
                number += 1

    if number==3 or number==4 or number==1:
        #how could it be? we already declared that there ain't no cross!
        #Similarly, how could there be 1 or 3 correctly oriented side pieces on OLL? o.O
        raise SystemError("invalid cross shape on oll")

    elif number==2:
        #little L;

        #this code has been modularized. 
        from algorithms import smallL_oll
        try:
            answer=smallL_oll.getAnswerFor(cube);
            cube.action(answer);
        except:
            #some errors?
            raise SystemError("invalid oll in cube 1");

        return;
    else:
        #"dot" only
        from algorithms import dot_oll
        #this code has been modularized. 

        try:
            answer=dot_oll.getAnswerFor(cube);
            cube.action(answer);
        except:
            #some errors?
            raise SystemError("invalid oll in cube 2");

        return;

def solvePLL(cube):
    '''Solves the Last layer [except the top layer] of the cube.'''

    import algorithms.pll
    answer=algorithms.pll.solve(cube)

    cube.action(answer);
     
def getBaseCrossBoxesCount(cube):
    '''Returns the number of boxes correctly placed in the base cross, with respect to the center box.'''
    #including the center box.

    #get the boxes
    boxes=cube.getSide(BOTTOM_SIDE);

    #get the color of the centre box
    for box in boxes:
        if box.pos[0]==1 and box.pos[1]==1:
            color=box.xy
            
    count=0 #count of the number of boxes in cross including the middle piece

    #now count the boxes of the cross that match to their boss(centre)
    for box in boxes:
        if box.pos[0]==1 or box.pos[1]==1:
            if box.xy.color==color.color:
                count += 1

    return count
    
def chooseBestSolvedSide(cube):
    '''Chooses the best side fit to be the base.'''

    array=[]

    #these actions bring the cube to ALL of the sides. 
    actions=["","Xi","Xi","Xi","Z","Z2"]

    #check which side has the highest number of base-cross items organized.
    for action in actions:
        cube.action(action)
        array.append({
                        "color":str(cube.boxAt(1,1,0).xy),
                        "count":getBaseCrossBoxesCount(cube)
                    })


    highest={"color":"green","count":0}
    for item in array:
        if item['count']>highest['count']:
            highest=item;

    # return the side with highest number of cross pieces properly oriented
    return highest['color'];
    
def orientCube(cube,side):
    '''Orients the cube with 'side' as base.'''

    #rotate in the axis 'Z' four times, or until the base is oriented
    count=0
    while not (str(cube.boxAt(1,1,0).xy)==side) and count<4:
        count += 1
        cube.action("Z")

    # and now in the "X" axis
    while not str(cube.boxAt(1,1,0).xy)==side:
        cube.action("Xi")    

    # by now, the cube should be theoretically oriented to have cube.base.center.color==side.color
    

def solveSecondLevel(cube):
    '''Solves the second layer. [part of F2l].
    Given that the base corner pieces are already in their correct position.'''

    #positions that can hold side-boxes of the second layer
    #the side positions of second and third row
    piecesThatCanHold=[(0,0,1),(0,2,1),(2,0,1),(2,2,1),(1,0,2),(1,2,2),(0,1,2),(2,1,2)]

    #the sides that the boxes need to be placed on.
    sides=[(0,0,1),(0,2,1),(2,0,1),(2,2,1)]

    #So, basically, what we are doing are bring cubes located in piecesThatCanHold to sides


    #rule here:
    
    #solve the boxes of middle layer that are in the top layer
    #if f2l-second phase complete:break
    #else:
        #bring the boxes of middle layer, from middle layer, which are incorrectly oriented.

    while True:
        #get boxes that do not have a FaceColor.top side. 
        #it means, that these boxes are of the middle layer
        boxes=cube.findAllWithout(piecesThatCanHold,FaceColor.top)
        assert(len(boxes)==4);

        #for each piece, 
        i=0
        while i < 4:
            box=boxes[i]
            pos=box.pos

            #check if it lies in top layer

            if pos[2]==1:
                #this box lies on the middle layer. skip this box for now
                i=i+1
                continue
            
            #get the transformation algorithm
            answer=Algo.getAnswerForf2lSecondLineTransformation("f2l-secondLineSolve",box)
            
            #apply the algorithm.
            cube.action(answer)
            
            #since the cube is rotated, the boxes we found initially, are messed up.
            #we need to find them again.
            boxes=cube.findAllWithout(piecesThatCanHold,FaceColor.top)
            
            #and then, we need to restart the process from scratch :-\
            i=0

        if cube.f2lSecondPhaseComplete():
            break
        else:
            for side in sides:
                if not cube.isSolvedAt(side):
                    cube= Algo.getAnswerForF2lSecondLineBringBoxToTopTransformation(side)
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

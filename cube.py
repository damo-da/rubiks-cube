'''The class for the cube.'''

from box import *
from headers import *
from loader import loadCubeFromFile,saveCubeToFile
from rotation import *
from AI import *
import random
from math import pi

class Cube(object):
    '''The Cube Class.'''
    def __init__(self,file_name="cube.txt"):
        self.reset()
        self.boxes=self.boxes=loadCubeFromFile(file_name)
        
        self.gui=None
        self.recording=False
        self.initialFunction=None
        self.calledForPause=False;
    def getFaceColor(self):
        return FaceColor
    def startRecording(self):
        self.recording=True
    def stopRecording(self):
        self.recording=False
    def setFunction(self,fun):
        self.initialFunction=fun
    def reset(self):
        '''Reset the cube.'''
        self.boxes=loadCubeFromFile("cube.txt")
        self.resetMoves()
    def save(self,fileName):
        saveCubeToFile(self,fileName);
        print "done";
    def getMoves(self):
        return optimizeMoves(self.move)
    
    def initialMovement(self):
        if self.initialFunction:
            self.initialFunction()
    def isSolvedAt(self,pos):
        '''Check if a pos has its native colors, flipped properly.'''
        #get the centre piece of box adjacent sides
        if pos[0]==0:
            if not self.boxAt(*pos).yz.color==self.boxAt(0,1,1).yz.color: return False
        elif pos[0]==2:
            if not self.boxAt(*pos).yz.color==self.boxAt(2,1,1).yz.color: return False
        if pos[1]==0:
            if not self.boxAt(*pos).xz.color==self.boxAt(1,0,1).xz.color: return False
        elif pos[1]==2:
            if not self.boxAt(*pos).xz.color==self.boxAt(1,2,1).xz.color: return False
        if pos[2]==0:
            if not self.boxAt(*pos).xy.color==self.boxAt(1,1,0).xy.color: return False
        elif pos[2]==2:
            if not self.boxAt(*pos).xy.color==self.boxAt(1,1,2).xy.color: return False
        return True
    def isSolved(self):
        '''Check if the cube is solved.'''
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
    
    def updateFaceColors(self):
        FaceColor.update({"front":self.boxAt(1,0,1).xz,"left":self.boxAt(0,1,1).yz,"top":self.boxAt(1,1,2).xy});
    def registerGraphicsHandler(self,g):
        self.gui=g;
    def pauseAction(self):
        self.calledForPause=True;
    def unpauseAction(self):
        self.calledForPause=False;
    def isActionPaused(self):
        return self.calledForPause;
    def action(self,word):
        '''Apply algorithm to the cube.'''
        keys=split_word(word);
        
        for key in keys:
            if len(key)>1:
                key=key[0].upper()+key[1:]
            else:
                key=key.upper()
            if key=="": continue
            
            if key=='F':
                rotateFrontSide(self);
                self.gui.rotateBoxes(self.getSide(FRONT_SIDE),(0,0,1))
            elif key=='B':
                rotateBackSide(self);
                self.gui.rotateBoxes(self.getSide(BACK_SIDE),(0,0,1),reverse=True)
            elif key=='L':
                rotateLeftSide(self);
                self.gui.rotateBoxes(self.getSide(LEFT_SIDE),(1,0,0),reverse=True)
            elif key=='R':
                rotateRightSide(self);
                self.gui.rotateBoxes(self.getSide(RIGHT_SIDE),(1,0,0))
            elif key=='U':
                rotateTopSide(self);
                self.gui.rotateBoxes(self.getSide(TOP_SIDE),(0,1,0))
            elif key=='D':
                rotateBottomSide(self);
                self.gui.rotateBoxes(self.getSide(BOTTOM_SIDE),(0,1,0),reverse=True)
            elif key=='Fi':
                rotateFrontSide(self);
                rotateFrontSide(self);
                rotateFrontSide(self);
                self.gui.rotateBoxes(self.getSide(FRONT_SIDE),(0,0,1),reverse=True)
            elif key=='Bi':
                rotateBackSide(self);
                rotateBackSide(self);
                rotateBackSide(self);
                self.gui.rotateBoxes(self.getSide(BACK_SIDE),(0,0,1))
            elif key=='Li':
                rotateLeftSide(self);
                rotateLeftSide(self);
                rotateLeftSide(self);
                self.gui.rotateBoxes(self.getSide(LEFT_SIDE),(1,0,0))
            elif key=='Ri':
                rotateRightSide(self);
                rotateRightSide(self);
                rotateRightSide(self);
                self.gui.rotateBoxes(self.getSide(RIGHT_SIDE),(1,0,0),reverse=True)
            elif key=='Ui':
                rotateTopSide(self);
                rotateTopSide(self);
                rotateTopSide(self);
                self.gui.rotateBoxes(self.getSide(TOP_SIDE),(0,1,0),reverse=True)
            elif key=='Di':
                rotateBottomSide(self);
                rotateBottomSide(self);
                rotateBottomSide(self);
                self.gui.rotateBoxes(self.getSide(BOTTOM_SIDE),(0,1,0))
            elif key=='F2':
                rotateFrontSide(self);
                rotateFrontSide(self);
                self.gui.rotateBoxes(self.getSide(FRONT_SIDE),(0,0,1), angle=pi)
            elif key=='B2':
                rotateBackSide(self);
                rotateBackSide(self);
                self.gui.rotateBoxes(self.getSide(BACK_SIDE),(0,0,1),reverse=True,angle=pi)
            elif key=='L2':
                rotateLeftSide(self);
                rotateLeftSide(self);
                self.gui.rotateBoxes(self.getSide(LEFT_SIDE),(1,0,0),reverse=True,angle=pi)
            elif key=='R2':
                rotateRightSide(self);
                rotateRightSide(self);
                self.gui.rotateBoxes(self.getSide(RIGHT_SIDE),(1,0,0),angle=pi)
            elif key=='U2':
                rotateTopSide(self);
                rotateTopSide(self);
                self.gui.rotateBoxes(self.getSide(TOP_SIDE),(0,1,0),angle=pi)
            elif key=='D2':
                rotateBottomSide(self);
                rotateBottomSide(self);
                self.gui.rotateBoxes(self.getSide(BOTTOM_SIDE),(0,1,0),reverse=True,angle=pi)
            elif key=="M":
                rotateM(self);
                boxes=[]
                for box in self.boxes:
                    if box.pos[0]==1:
                        boxes.append(box)
                self.gui.rotateBoxes(boxes,(1,0,0),reverse=True)
            elif key=="E":
                rotateE(self)
                boxes=[]
                for box in self.boxes:
                    if box.pos[2]==1:
                        boxes.append(box)
                self.gui.rotateBoxes(boxes,(0,1,0),reverse=True)
            elif key=="S":
                rotateS(self)
                boxes=[]
                for box in self.boxes:
                    if box.pos[1]==1:
                        boxes.append(box)
                self.gui.rotateBoxes(boxes,(0,0,1))
            elif key=="M2":
                rotateM(self);
                rotateM(self);
                boxes=[]
                for box in self.boxes:
                    if box.pos[0]==1:
                        boxes.append(box)
                self.gui.rotateBoxes(boxes,(1,0,0),reverse=True,angle=pi)
            elif key=="E2":
                rotateE(self)
                rotateE(self)
                boxes=[]
                for box in self.boxes:
                    if box.pos[2]==1:
                        boxes.append(box)
                self.gui.rotateBoxes(boxes,(0,1,0),reverse=True,angle=pi)
            elif key=="S2":
                rotateS(self)
                rotateS(self)
                boxes=[]
                for box in self.boxes:
                    if box.pos[1]==1:
                        boxes.append(box)
                self.gui.rotateBoxes(boxes,(0,0,1),angle=pi)
            elif key=="Mi":
                rotateM(self);
                rotateM(self);
                rotateM(self);
                boxes=[]
                for box in self.boxes:
                    if box.pos[0]==1:
                        boxes.append(box)
                self.gui.rotateBoxes(boxes,(1,0,0))
            elif key=="Ei":
                rotateE(self)
                rotateE(self)
                rotateE(self)
                boxes=[]
                for box in self.boxes:
                    if box.pos[2]==1:
                        boxes.append(box)
                self.gui.rotateBoxes(boxes,(0,1,0))
            elif key=="Si":
                rotateS(self)
                rotateS(self)
                rotateS(self)
                boxes=[]
                for box in self.boxes:
                    if box.pos[1]==1:
                        boxes.append(box)
                self.gui.rotateBoxes(boxes,(0,0,1),reverse=True)
            elif key=="X":
                rotateRightSide(self)
                rotateLeftSide(self)
                rotateLeftSide(self)
                rotateLeftSide(self)
                rotateM(self)
                rotateM(self)
                rotateM(self)
                self.gui.rotateBoxes(self.boxes,(1,0,0))
            elif key=="Xi":
                rotateRightSide(self)
                rotateRightSide(self)
                rotateRightSide(self)
                rotateLeftSide(self)
                rotateM(self)
                self.gui.rotateBoxes(self.boxes,(1,0,0),reverse=True)
            elif key=="X2":
                rotateM(self)
                rotateM(self)
                rotateRightSide(self)
                rotateRightSide(self)
                rotateLeftSide(self)
                rotateLeftSide(self)
                self.gui.rotateBoxes(self.boxes,(1,0,0),angle=pi)
            elif key=="Y":
                rotateTopSide(self)
                rotateBottomSide(self)
                rotateBottomSide(self)
                rotateBottomSide(self)
                rotateE(self)
                rotateE(self)
                rotateE(self)
                self.gui.rotateBoxes(self.boxes,(0,1,0))
            elif key=="Yi":
                rotateTopSide(self)
                rotateTopSide(self)
                rotateTopSide(self)
                rotateBottomSide(self)
                rotateE(self)
                self.gui.rotateBoxes(self.boxes,(0,1,0),reverse=True)
            elif key=="Y2":
                rotateTopSide(self)
                rotateTopSide(self)
                rotateBottomSide(self)
                rotateBottomSide(self)
                rotateE(self)
                rotateE(self)
                self.gui.rotateBoxes(self.boxes,(0,1,0),angle=pi)
            elif key=="Z":
                rotateFrontSide(self)
                rotateFrontSide(self)
                rotateFrontSide(self)
                rotateBackSide(self)
                rotateS(self)
                rotateS(self)
                rotateS(self)
                self.gui.rotateBoxes(self.boxes,(0,0,1),reverse=True)
            elif key=="Zi":
                rotateFrontSide(self)
                rotateBackSide(self)
                rotateBackSide(self)
                rotateBackSide(self)
                rotateS(self)
                self.gui.rotateBoxes(self.boxes,(0,0,1))
            elif key=="Z2":
                rotateFrontSide(self)
                rotateFrontSide(self)
                rotateBackSide(self)
                rotateBackSide(self)
                rotateS(self)
                rotateS(self)
                self.gui.rotateBoxes(self.boxes,(0,0,1),reverse=True,angle=pi)
            else:
                print "unknown character : "+key
                raise SystemError
            self.move += " "+key+" "
    def OLLsolved(self):
        self.updateFaceColors();
        boxes=self.getSide(TOP_SIDE);
        for box in boxes:
            if box.xy.color is not FaceColor.top.color:
                return False
        return True;
    def findAll(self,array,color):
        '''Returns all box with color from the array.'''
        ret=[]
        for box in self.boxes:
            if box.pos in array:
                if box.hasColor(color):
                    ret.append(box)
        return ret
    def actionRealTime(self,word):
        '''Solves real time for the user. For each next move, the user presses the space key.'''
        #if self.isActionPaused():
        #self.gui.waitForUnpause();
        keys=word.split(" ");
        for key in keys:
            try:
                self.action(key);
                self.gui.waitForUnpause();
            except:
                continue;        
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

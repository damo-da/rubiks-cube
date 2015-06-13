'''Rotates the cube by algorithm. Such as F->front, R->right,L->left,B->back,D->down,U->UP'''

from headers import *
from copy import deepcopy

def rotateFrontSide(self):
    pieces=self.boxes
    
    index=0
    for index in range(0,len(pieces)):
        piece=pieces[index]
        if not piece.pos[1]:
            pos=deepcopy(piece.pos)
            x=pos[0]
            z=pos[1]
            translation=None
            if pos==(1,1,1):
                pass
            elif pos==(0,0,0):
                translation=(0,0,2)
            elif pos==(0,0,2):
                translation=(2,0,2)
            elif pos==(2,0,2):
                translation=(2,0,0)
            elif pos==(2,0,0):
                translation=(0,0,0)
            elif pos==(1,0,0):
                translation=(0,0,1)
            elif pos==(0,0,1):
                translation=(1,0,2)
            elif pos==(1,0,2):
                translation=(2,0,1)
            elif pos==(2,0,1):
                translation=(1,0,0)
            if translation:
                pieces[index].setPos(translation[0],translation[1],translation[2])
                a=deepcopy(piece.yz)
                piece.yz=deepcopy(piece.xy)
                piece.xy=deepcopy(a)
        index += 1
        
def rotateBackSide(self):
    pieces=self.boxes
    index=0
    for index in range(0,len(pieces)):
        piece=pieces[index]
        if piece.pos[1] ==2:
            pos=deepcopy(piece.pos)
            x=pos[0]
            z=pos[1]
            translation=None
            if pos==(1,1,1):
                pass
            elif pos==(0,2,0):
                translation=(2,2,0)
            elif pos==(0,2,1):
                translation=(1,2,0)
            elif pos==(0,2,2):
                translation=(0,2,0)
            elif pos==(1,2,0):
                translation=(2,2,1)
            elif pos==(1,2,2):
                translation=(0,2,1)
            elif pos==(2,2,0):
                translation=(2,2,2)
            elif pos==(2,2,1):
                translation=(1,2,2)
            elif pos==(2,2,2):
                translation=(0,2,2)
            if translation:
                pieces[index].setPos(translation[0],translation[1],translation[2])
                a=deepcopy(piece.yz)
                piece.yz=deepcopy(piece.xy)
                piece.xy=deepcopy(a)
            #else:
                #print "oopsie toopsie error at rotation :("
        index += 1


def rotateLeftSide(self):
    pieces=self.boxes
    index=0
    for index in range(0,len(pieces)):
        piece=pieces[index]
        if piece.pos[0]==0:
            pos=deepcopy(piece.pos)
            x=pos[0]
            z=pos[1]
            translation=None
            if pos==(1,1,1):
                pass
            elif pos==(0,0,0):
                translation=(0,2,0)
            elif pos==(0,0,1):
                translation=(0,1,0)
            elif pos==(0,0,2):
                translation=(0,0,0)
            elif pos==(0,1,0):
                translation=(0,2,1)
            elif pos==(0,1,2):
                translation=(0,0,1)
            elif pos==(0,2,0):
                translation=(0,2,2)
            elif pos==(0,2,1):
                translation=(0,1,2)
            elif pos==(0,2,2):
                translation=(0,0,2)
            if translation:
                pieces[index].setPos(translation[0],translation[1],translation[2])
                a=deepcopy(piece.xy)
                piece.xy=deepcopy(piece.xz)
                piece.xz=deepcopy(a)
        index += 1


def rotateRightSide(self):
    pieces=self.boxes
    index=0
    for index in range(0,len(pieces)):
        piece=pieces[index]
        if piece.pos[0]==2:
            pos=deepcopy(piece.pos)
            x=pos[0]
            z=pos[1]
            translation=None
            if pos==(1,1,1):
                pass
            elif pos==(2,0,0):
                translation=(2,0,2)
            elif pos==(2,0,1):
                translation=(2,1,2)
            elif pos==(2,0,2):
                translation=(2,2,2)
            elif pos==(2,1,0):
                translation=(2,0,1)
            elif pos==(2,1,2):
                translation=(2,2,1)
            elif pos==(2,2,0):
                translation=(2,0,0)
            elif pos==(2,2,1):
                translation=(2,1,0)
            elif pos==(2,2,2):
                translation=(2,2,0)
            if translation:
                pieces[index].setPos(translation[0],translation[1],translation[2])
                a=deepcopy(piece.xy)
                piece.xy=deepcopy(piece.xz)
                piece.xz=deepcopy(a)
        index += 1

def rotateTopSide(self):
    pieces=self.boxes
    index=0
    for index in range(0,len(pieces)):
        piece=pieces[index]
        if piece.pos[2]==2:
            pos=deepcopy(piece.pos)
            x=pos[0]
            z=pos[1]
            translation=None
            if pos==(1,1,1):
                pass
            elif pos==(0,0,2):
                translation=(0,2,2)
            elif pos==(0,1,2):
                translation=(1,2,2)
            elif pos==(0,2,2):
                translation=(2,2,2)
            elif pos==(1,0,2):
                translation=(0,1,2)
            elif pos==(1,2,2):
                translation=(2,1,2)
            elif pos==(2,0,2):
                translation=(0,0,2)
            elif pos==(2,1,2):
                translation=(1,0,2)
            elif pos==(2,2,2):
                translation=(2,0,2)
            if translation:
                pieces[index].setPos(translation[0],translation[1],translation[2])
                a=deepcopy(piece.xz)
                piece.xz=deepcopy(piece.yz)
                piece.yz=deepcopy(a)
        index += 1
    
def rotateM(self):    
    pieces=self.boxes
    index=0
    for index in range(0,len(pieces)):
        
        piece=pieces[index]
        if piece.pos[0]==1:
            pos=piece.pos
            y=pos[1]
            z=pos[2]
            translation=None
            if pos==(1,1,1):
                pass
            elif pos==(1,1,0):
                translation=(1,2,1)
            elif pos==(1,2,0):
                translation=(1,2,2)
            elif pos==(1,2,1):
                translation=(1,1,2)
            elif pos==(1,2,2):
                translation=(1,0,2)
            elif pos==(1,1,2):
                translation=(1,0,1)
            elif pos==(1,0,2):
                translation=(1,0,0)
            elif pos==(1,0,1):
                translation=(1,1,0)
            elif pos==(1,0,0):
                translation=(1,2,0)
            if translation:
                pieces[index].setPos(translation[0],translation[1],translation[2])
                a=deepcopy(piece.xz)
                piece.xz=deepcopy(piece.xy)
                piece.xy=deepcopy(a)
    self.updateFaceColors()
                
def rotateE(self):
    pieces=self.boxes
    index=0
    for index in range(0,len(pieces)):
        
        piece=pieces[index]
        if piece.pos[2]==1:
            pos=piece.pos
            y=pos[1]
            x=pos[0]
            translation=None
            if pos==(1,1,1):
                pass
            elif pos==(0,0,1):
                translation=(2,0,1)
            elif pos==(1,0,1):
                translation=(2,1,1)
            elif pos==(2,0,1):
                translation=(2,2,1)
            elif pos==(2,1,1):
                translation=(1,2,1)
            elif pos==(2,2,1):
                translation=(0,2,1)
            elif pos==(1,2,1):
                translation=(0,1,1)
            elif pos==(0,2,1):
                translation=(0,0,1)
            elif pos==(0,1,1):
                translation=(1,0,1)
            if translation:
                pieces[index].setPos(translation[0],translation[1],translation[2])
                a=deepcopy(piece.xz)
                piece.xz=deepcopy(piece.yz)
                piece.yz=deepcopy(a)
    self.updateFaceColors()
def rotateS(self):
    pieces=self.boxes
    index=0
    for index in range(0,len(pieces)):
        piece=pieces[index]
        if piece.pos[1]==1:
            pos=piece.pos
            z=pos[1]
            x=pos[0]
            translation=None
            if pos==(1,1,1):
                pass
            elif pos==(0,1,1):
                translation=(1,1,2)
            elif pos==(0,1,2):
                translation=(2,1,2)
            elif pos==(1,1,2):
                translation=(2,1,1)
            elif pos==(2,1,2):
                translation=(2,1,0)
            elif pos==(2,1,1):
                translation=(1,1,0)
            elif pos==(2,1,0):
                translation=(0,1,0)
            elif pos==(1,1,0):
                translation=(0,1,1)
            elif pos==(0,1,0):
                translation=(0,1,2)
            if translation:
                pieces[index].setPos(translation[0],translation[1],translation[2])
                a=deepcopy(piece.xy)
                piece.xy=deepcopy(piece.yz)
                piece.yz=deepcopy(a)
    self.updateFaceColors()
        
def rotateBottomSide(self):
    pieces=self.boxes
    index=0
    for index in range(0,len(pieces)):
        piece=pieces[index]
        if piece.pos[2]==0:
            pos=deepcopy(piece.pos)
            x=pos[0]
            z=pos[1]
            translation=None
            if pos==(1,1,1):
                pass
            elif pos==(0,0,0):
                translation=(2,0,0)
            elif pos==(0,1,0):
                translation=(1,0,0)
            elif pos==(0,2,0):
                translation=(0,0,0)
            elif pos==(1,0,0):
                translation=(2,1,0)
            elif pos==(1,2,0):
                translation=(0,1,0)
            elif pos==(2,0,0):
                translation=(2,2,0)
            elif pos==(2,1,0):
                translation=(1,2,0)
            elif pos==(2,2,0):
                translation=(0,2,0)
            if translation:
                pieces[index].setPos(translation[0],translation[1],translation[2])
                a=deepcopy(piece.xz)
                piece.xz=deepcopy(piece.yz)
                piece.yz=deepcopy(a)
        index += 1
if __name__=="__main__":
    import main

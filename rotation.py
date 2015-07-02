'''Rotates the cube by algorithm. Such as F->front, R->right,L->left,B->back,D->down,U->UP'''

from headers import *
from copy import deepcopy

def rotateFrontSide(self):
    boxes=self.boxes
    
    index=0
    for index in range(0,len(boxes)):
        box=boxes[index]
        if not box.pos[1]:
            pos=deepcopy(box.pos)
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
                boxes[index].setPos(translation[0],translation[1],translation[2])
                a=deepcopy(box.yz)
                box.yz=deepcopy(box.xy)
                box.xy=deepcopy(a)
        index += 1
        
def rotateBackSide(self):
    boxes=self.boxes
    index=0
    for index in range(0,len(boxes)):
        box=boxes[index]
        if box.pos[1] ==2:
            pos=deepcopy(box.pos)
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
                boxes[index].setPos(translation[0],translation[1],translation[2])
                a=deepcopy(box.yz)
                box.yz=deepcopy(box.xy)
                box.xy=deepcopy(a)
            #else:
                #print "oopsite topsie error at rotation :("
        index += 1


def rotateLeftSide(self):
    boxes=self.boxes
    index=0
    for index in range(0,len(boxes)):
        box=boxes[index]
        if box.pos[0]==0:
            pos=deepcopy(box.pos)
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
                boxes[index].setPos(translation[0],translation[1],translation[2])
                a=deepcopy(box.xy)
                box.xy=deepcopy(box.xz)
                box.xz=deepcopy(a)
        index += 1


def rotateRightSide(self):
    boxes=self.boxes
    index=0
    for index in range(0,len(boxes)):
        box=boxes[index]
        if box.pos[0]==2:
            pos=deepcopy(box.pos)
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
                boxes[index].setPos(translation[0],translation[1],translation[2])
                a=deepcopy(box.xy)
                box.xy=deepcopy(box.xz)
                box.xz=deepcopy(a)
        index += 1

def rotateTopSide(self):
    boxes=self.boxes
    index=0
    for index in range(0,len(boxes)):
        box=boxes[index]
        if box.pos[2]==2:
            pos=deepcopy(box.pos)
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
                boxes[index].setPos(translation[0],translation[1],translation[2])
                a=deepcopy(box.xz)
                box.xz=deepcopy(box.yz)
                box.yz=deepcopy(a)
        index += 1
    
def rotateM(self):    
    boxes=self.boxes
    index=0
    for index in range(0,len(boxes)):
        
        box=boxes[index]
        if box.pos[0]==1:
            pos=box.pos
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
                boxes[index].setPos(translation[0],translation[1],translation[2])
                a=deepcopy(box.xz)
                box.xz=deepcopy(box.xy)
                box.xy=deepcopy(a)
    self.updateFaceColors()
                
def rotateE(self):
    boxes=self.boxes
    index=0
    for index in range(0,len(boxes)):
        
        box=boxes[index]
        if box.pos[2]==1:
            pos=box.pos
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
                boxes[index].setPos(translation[0],translation[1],translation[2])
                a=deepcopy(box.xz)
                box.xz=deepcopy(box.yz)
                box.yz=deepcopy(a)
    self.updateFaceColors()
def rotateS(self):
    boxes=self.boxes
    index=0
    for index in range(0,len(boxes)):
        box=boxes[index]
        if box.pos[1]==1:
            pos=box.pos
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
                boxes[index].setPos(translation[0],translation[1],translation[2])
                a=deepcopy(box.xy)
                box.xy=deepcopy(box.yz)
                box.yz=deepcopy(a)
    self.updateFaceColors()
        
def rotateBottomSide(self):
    boxes=self.boxes
    index=0
    for index in range(0,len(boxes)):
        box=boxes[index]
        if box.pos[2]==0:
            pos=deepcopy(box.pos)
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
                boxes[index].setPos(translation[0],translation[1],translation[2])
                a=deepcopy(box.xz)
                box.xz=deepcopy(box.yz)
                box.yz=deepcopy(a)
        index += 1
if __name__=="__main__":
    import main

'''Rendering Graphics.'''
from copypy import GUI
import math
from headers import *
import numpy as np
from math import pi,tan,atan,sin,cos
import sys
from visual import color
import visual
from cube import *
from time import sleep


_GRAPHICS=None;
_PAUSED=visual.text(text='-',pos=(0,2,0),align="center", depth=-0.3, color=color.red)
_PAUSED.visible=False;
_FPS=70

class GUI(object):
    def stopAction(self,event):
	#if space  pressed, 
		#stop  action in cube
		#wait for a keyup of space key
		#resume the action in cube
	#if reset pressed, 
		#delay some time
		#reset the cube
		#empty actions to be performed
	#baam
        try:
            global _GRAPHICS;
            cube=_GRAPHICS.cube;
            if(event.key==" "):
                global _PAUSED;
                cube.pauseAction();
                
                
        except:
            raise SystemError("GRAPHICS not initialised");
        return None;
    def waitForUnpause(self):
        _PAUSED.visible=True;
        while True:
            event=visual.scene.waitfor('keyup');
            if event.key==" ":
                _PAUSED.visible=False;
                break;
        return None;
        
    def __init__(self,c):
        self.cube=c
        self.rendering=False
        global _GRAPHICS;
        _GRAPHICS=self;

    def init(self):
        '''Assigns boxes with their respective colorBoxes.'''
        #self.black=visual.box(pos=(0,0,0), size=(2,2,2),color=color.black)
        for box in self.cube.boxes:
            if  box.xy:
                pos=box.pos
                pos=[pos[0]-1,-1.5*(abs(pos[2]-1)/(1-pos[2])),1-pos[1]]
                size=[0.97,0.05,0.97]
                box.xyBox=self.drawBox(pos,size,box.xy.color)
            if box.xz:
                pos=box.pos
                pos=[pos[0]-1,pos[2]-1,-1.5*(abs(pos[1]-1)/(pos[1]-1))]
                size=[0.97,0.97,0.05]
                box.xzBox=self.drawBox(pos,size,box.xz.color)
            if box.yz:
                pos=box.pos
                pos=[-1.5*(abs(pos[0]-1)/(1-pos[0])),pos[2]-1,1-pos[1]]
                size=[0.05,0.97,0.97]
                box.yzBox=self.drawBox(pos,size,box.yz.color)
            
    def drawBox(self,pos,size,color):
        '''Draws a box on the screen and returns its address.'''
        return visual.box(pos=pos,size=size,color=color)
    def rotateBoxes(self,boxes,direction,reverse=False,angle=None):
        if not self.rendering: return None
        if not self.cube.recording:
            return None

        if not angle: angle=pi/2
        slicedAngle=0.07
        counts=float(angle)/slicedAngle
        if counts>int(counts): counts=int(counts)+1
        if not reverse:
            slicedAngle=-slicedAngle
        
        for i in range(0,counts+1):
            global _FPS;
            rate(_FPS)
            if (i==counts):
                slicedAngle=angle-abs(slicedAngle)*counts
                if not reverse:
                    slicedAngle=-slicedAngle
            for box in boxes:
                if box.xzBox:
                    box.xzBox.rotate(angle=slicedAngle,axis=direction,origin=(0,0,0))
                if box.xyBox:
                    box.xyBox.rotate(angle=slicedAngle,axis=direction,origin=(0,0,0))
                if box.yzBox:
                    box.yzBox.rotate(angle=slicedAngle,axis=direction,origin=(0,0,0))

    def begin(self):
        self.rendering=True
        self.init();
        visual.scene.bind('keyup',self.stopAction);
        self.cube.initialMovement()
        
        while True:
            key=visual.scene.waitfor("keyup")
            key=key.key
            if key=="f":
                self.cube.action("F")
            elif key=="F":
                self.cube.action("Fi")
            elif key=="b":
                self.cube.action("B")
            elif key=="B":
                self.cube.action("Bi")
            elif key=="r":
                self.cube.action("R")
            elif key=="R":
                self.cube.action("Ri")
            elif key=="l":
                self.cube.action("L")
            elif key=="L":
                self.cube.action("Li")
            elif key=="u":
                self.cube.action("U")
            elif key=="U":
                self.cube.action("Ui")
            elif key=="d":
                self.cube.action("D")
            elif key=="D":
                self.cube.action("Di")
            elif key=="x":
                self.cube.action("x")
            elif key=="y":
                self.cube.action("y")
            elif key=="z":
                self.cube.action("z")
            elif key=="X":
                self.cube.action("xi")
            elif key=="Y":
                self.cube.action("yi")
            elif key=="Z":
                self.cube.action("zi")
            elif key=="m":
                self.cube.action("M")
            elif key=="M":
                self.cube.action("Mi")
            elif key=="e":
                self.cube.action("E")
            elif key=="E":
                self.cube.action("Ei")
            elif key=="s":
                self.cube.action("S")
            elif key=="S":
                self.cube.action("Si")

if __name__=="__main__":
    import main

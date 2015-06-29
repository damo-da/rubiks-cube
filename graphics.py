'''The graphics handler'''

import math
from headers import *
import sys
from visual import color
import visual
from cube import *
from math import floor


_GRAPHICS=None;
_PAUSED=visual.text(text='-',pos=(0,2,0),align="center", depth=-0.3, color=color.red)
_PAUSED.visible=False;
_FPS=70

class GUI(object):
    def ESCexitHandler(self,event):
	'''Handles the exit event callback due to ESCAPE press.'''
        global _GRAPHICS;
        cube=_GRAPHICS.cube;

        global _PAUSED;
        if(event.key=="esc"):
            visual.exit();


    def waitForUnpause(self):
        '''Qaits till the user presses the "space" key.'''
        #this is used during interactive mode

        #show that we are paused.
        _PAUSED.visible=True;

        while True:
            event=visual.scene.waitfor('keyup');
            if event.key==" ":
                #hide that we are paused, because we are unpausing now
                _PAUSED.visible=False;
                break;
        
    def __init__(self,c):
        self.cube=c

        #assign myself as a graphics handler in the cube
        c.registerGraphicsHandler(self)

        # by default, graphics is not shown
        self.rendering=False

        # make myself global
        global _GRAPHICS;
        _GRAPHICS=self;

    def init(self):
        '''Initialize graphics.'''

        #should show black in centre of the cube? Uncomment the followig line.
        #self.black=visual.box(pos=(0,0,0), size=(2,2,2),color=color.black)


        #Assign visual to each box in cube
        #Things to note here
        # the visual coordinating and our coordinating do not match. 
        # Our y-axis is its z-axis and vice versa.
        #and also our origin lies on front-left-bottom corner, 
            # while visual's lies in center of the cube
        
        #some visual adjustments
        
        #width of the box
        boxLength=0.97
        #height of the box
        boxHeight=0.05;

        for box in self.cube.boxes:
            if  box.xy:
                pos=box.pos
                pos=[pos[0]-1,-1.5*(abs(pos[2]-1)/(1-pos[2])),1-pos[1]]
                size=[boxLength,boxHeight,boxLength];
                box.xyBox=self.drawBox(pos,size,box.xy.color)
            if box.xz:
                pos=box.pos
                pos=[pos[0]-1,pos[2]-1,-1.5*(abs(pos[1]-1)/(pos[1]-1))]
                size=[boxLength,boxLength,boxHeight]
                box.xzBox=self.drawBox(pos,size,box.xz.color)
            if box.yz:
                pos=box.pos
                pos=[-1.5*(abs(pos[0]-1)/(1-pos[0])),pos[2]-1,1-pos[1]]
                size=[boxHeight,boxLength,boxLength]
                box.yzBox=self.drawBox(pos,size,box.yz.color)
            
    def drawBox(self,pos,size,color):
        '''Draws a box on the screen and returns its reference.'''
        return visual.box(pos=pos,size=size,color=color)

    def rotateBoxes(self,boxes,direction,reverse=False,angle=None):
        '''The function for showing the rotation of Cube graphically'''
        if not self.rendering: return None
        if not self.cube.recording:
            return None

        if not angle: angle=pi/2

        # by how much to rotate at one time
        slicedAngle=0.07

        # the total number of rotations to be made
        counts=int(ceil( float(angle)/slicedAngle ))

        # should rotate +angle or -angle?
        if not reverse:
            slicedAngle=-slicedAngle
        
        # read the FPS
        global _FPS;

        # begin the rotation process
        for i in range(0,counts+1):
            # delay the rotation
            rate(_FPS)

            # if last rotation, bring the boxes EXACTLY at the requested angle
            if (i==counts):
                #fix the little uncertainty obtained while rotating
                slicedAngle=angle-abs(slicedAngle)*counts

                if not reverse:
                    slicedAngle=-slicedAngle

            # the time to rotate the boxes
            for box in boxes:
                if box.xzBox:
                    box.xzBox.rotate(angle=slicedAngle,axis=direction,origin=(0,0,0))

                if box.xyBox:
                    box.xyBox.rotate(angle=slicedAngle,axis=direction,origin=(0,0,0))

                if box.yzBox:
                    box.yzBox.rotate(angle=slicedAngle,axis=direction,origin=(0,0,0))

    def begin(self):
        '''Show the AI, and call the initialMovement() functin if exists'''

        #broadcast that I am rendering
        self.rendering=True

        self.init();

        #stop myself if the user does a keyup of "escape"
        visual.scene.bind('keyup',self.ESCexitHandler);

        #perform the initial movement on the cube, or whatever is requested.
        #This happens before the keys are binded to the UI.
        # The only choice user has is to close the program right now
        self.cube.initialMovement()
        
        # the initial function has complete its journey. Yay
        # now the "GameLoop"
        while True:
            # wait for a key press. By key press, I mean, keyup
            key=visual.scene.waitfor("keyup")
            key=key.key

            # yeah, stuffs
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
    #if started from this file, 
    #assume that we are running the main file.
    import main

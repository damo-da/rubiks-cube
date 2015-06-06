'''Rendering Graphics.'''
from copypy import GUI
import math
from headers import *
import numpy as np
from math import pi,tan,atan,sin,cos

from visual import *
from cube import *

array=np.zeros((3,3,3))
c=Cube()
c.action("F R U F F D")

class GUI(object):
    def __init__(self,c):
        self.cube=c
        
    def render(self):
        self.fronts=c.getSide(FRONT_SIDE)
        self.backs=c.getSide(BACK_SIDE)
        self.lefts=c.getSide(LEFT_SIDE)
        self.rights=c.getSide(RIGHT_SIDE)
        self.tops=c.getSide(TOP_SIDE)
        self.bottoms=c.getSide(BOTTOM_SIDE)
        
        box(pos=(0,0,0),size=(3,3,3),color=color.black)
        for item in self.fronts:
            pos=item.pos
            pos=(pos[0]-1,pos[2]-1,1.5)
            box(pos=pos,size=(0.9,0.9,0.1),color=item.xz.color)
        for item in self.backs:
            pos=item.pos
            pos=(pos[0]-1,pos[2]-1,-1.5)
            box(pos=pos,size=(0.9,0.9,0.1),color=item.xz.color)
        for item in self.lefts:
            pos=item.pos
            pos=(-1.5,pos[2]-1,1-pos[1])
            box(pos=pos,size=(0.1,0.9,0.9),color=item.yz.color)
        for item in self.rights:
            pos=item.pos
            pos=(1.5,pos[2]-1,1-pos[1])
            box(pos=pos,size=(0.1,0.9,.9),color=item.yz.color)
        for item in self.tops:
            pos=item.pos
            pos=(pos[0]-1,1.5,1-pos[1])
            box(pos=pos,size=(.9,0.1,.9),color=item.xy.color)
        for item in self.bottoms:
            pos=item.pos
            pos=(pos[0]-1,-1.5,1-pos[1])
            box(pos=pos,size=(.9,0.1,.9),color=item.xy.color)
    def begin(self):
        self.render()
        while True:
            sleep(1)
            
        

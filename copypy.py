'''Rendering Graphics.'''

from cube import *
from headers import *

import math
from math import pi,tan,atan,sin,cos
from pygame import *
import pygame

class GUI(object):
    '''The class for the rendering purpose.'''
    def __init__(self,cube):
        self.cube=cube
        self.readsExit=False
        self.clock=pygame.time.Clock()
        self.screen=None
        
        self.xrotation=0
        self.yrotation=0
        
        self.gestureMode=False
        self.gestureStartPos=(0,0)
        self.gestures=[]
        
    def eventHandler(self):
        '''Handles events,such as mouse clicks.'''
        Changed=False
        firstTime=True
        while not Changed:
            self.clock.tick(50);
            i=pygame.event.wait()
            if i.type==QUIT:
                self.readsExit=True
                return
            else:
                if i.type==MOUSEBUTTONDOWN and i.button==1:
                    self.gestureMode=True
                    self.gestureStartPos=i.pos
                    Changed=True
                elif i.type==MOUSEBUTTONUP and i.button==1:
                    self.gestureMode=False
                    gesture=(self.gestureStartPos,i.pos)
                    self.gestures.append(gesture)
                    Changed=True
                if i.type==MOUSEMOTION and self.gestureMode:
                    if abs(i.rel[0])<=1: return
                    if abs(i.rel[1])<=1: return
                    self.xrotation += i.rel[0]
                    self.yrotation += i.rel[1]
                    Changed=True
                
            
                
    def getFrontRect(self):
        '''Returns surface for front side.'''
        front=Surface((221,221))
        front.fill(Color("gray"))
        fronties=self.cube.getSide(FRONT_SIDE)
        for item in fronties:
            surface=Surface((70,70))
            surface.fill(item.xz.getColor())
            y=(2-item.pos[2])*75
            x=item.pos[0] * 75
            rect=pygame.Rect(x,y,70,70)
            front.blit(surface,rect)
        return front
        
    def getRightRect(self):
        '''Returns surface for right side.'''
        side=Surface((221,221))
        side.fill(Color("gray"))
        sidies=self.cube.getSide(RIGHT_SIDE)
        for item in sidies:
            surface=Surface((70,70))
            surface.fill(item.yz.getColor())
            y=(2-item.pos[2])*75
            x=item.pos[1] * 75
            rect=pygame.Rect(x,y,70,70)
            side.blit(surface,rect)
        
        theta=30*pi/180
        width=110
        side=pygame.transform.scale(side,(width,side.get_rect().height))
        oldRect=side.get_rect()
        width=oldRect.width
        newSurface=Surface((width,oldRect.height+oldRect.width*tan(theta)))
        newSurface.fill((0,0,0,0))
        newSurface.set_colorkey((0,0,0,0))
        for x in range(0,oldRect.width,2):
            a=oldRect.width-x
            h=a*tan(theta)
            for y in range(0,oldRect.height):
                color=side.get_at((x,y))
                pos=(x,int(y+h))
                pos1=(x+1,int(y+h))
                pos2=(x+3,int(y+h))
                newSurface.set_at(pos,color)
                newSurface.set_at(pos1,color)
                newSurface.set_at(pos2,color)
        return newSurface
        
    def getTopRect(self):
        '''Returns surface for top side.'''
        side=Surface((221,221))
        side.fill(Color("gray"))
        sidies=self.cube.getSide(TOP_SIDE)
        for item in sidies:
            surface=Surface((70,70))
            surface.fill(item.xy.getColor())
            y=(2-item.pos[1])*75
            x=item.pos[0] * 75
            rect=pygame.Rect(x,y,70,70)
            side.blit(surface,rect)
        
        theta=60*pi/180
        height=62
        side=pygame.transform.scale(side,(side.get_rect().width,height))
        oldRect=side.get_rect()
        height=oldRect.height
        newSurface=Surface((oldRect.width+oldRect.height*tan(theta),height))
        newSurface.fill((0,0,0,0))
        newSurface.set_colorkey((0,0,0,0))
        for y in range(0,oldRect.height,2):
            a=oldRect.height-y
            w=a*tan(theta)
            for x in range(0,oldRect.width):
                color=side.get_at((x,y))
                pos=(int(x+w),y)
                pos1=(int(x+w),y+1)
                pos2=(int(x+w),y+2)
                newSurface.set_at(pos,color)
                newSurface.set_at(pos1,color)
                newSurface.set_at(pos2,color)
        return newSurface
        #return side
        
    def getLeftRect(self):
        '''Returns surface for left side.'''
        side=Surface((221,221))
        side.fill(Color("gray"))
        sidies=self.cube.getSide(LEFT_SIDE)
        for item in sidies:
            surface=Surface((70,70))
            surface.fill(item.yz.getColor())
            y=(2-item.pos[2])*75
            x=(2-item.pos[1]) * 75
            rect=pygame.Rect(x,y,70,70)
            side.blit(surface,rect)
        return side
        
    def getBottomRect(self):
        '''Returns surface for bottom side.'''
        side=Surface((221,221))
        side.fill(Color("gray"))
        sidies=self.cube.getSide(BOTTOM_SIDE)
        for item in sidies:
            surface=Surface((70,70))
            surface.fill(item.xy.getColor())
            y=(item.pos[1])*75
            x=(item.pos[0]) * 75
            rect=pygame.Rect(x,y,70,70)
            side.blit(surface,rect)
        return side
        
    def getBackRect(self):
        '''Returns surface for back side.'''
        side=Surface((221,221))
        side.fill(Color("gray"))
        sidies=self.cube.getSide(BACK_SIDE)
        for item in sidies:
            surface=Surface((70,70))
            surface.fill(item.xz.getColor())
            y=(2-item.pos[2])*75
            x=(item.pos[0]) * 75
            rect=pygame.Rect(x,y,70,70)
            side.blit(surface,rect)
        return side
        
    def updateDisplay(self):
        '''reRenders the screen.'''
        #print self.xrotation,self.yrotation
        #return
        front=self.getFrontRect()
        frontRect=front.get_rect()
        frontRect.centerx=self.screen.get_rect().centerx
        frontRect.centery=self.screen.get_rect().centery-30
        
        rightSide=self.getRightRect()
        rightRect=rightSide.get_rect()
        rightRect.x += 461
        rightRect.centery=self.screen.get_rect().centery-62
        
        topSide=self.getTopRect()
        topRect=topSide.get_rect()
        topRect.y=173
        topRect.centerx=frontRect.centerx+52
        
        leftSide=self.getLeftRect()
        leftRect=leftSide.get_rect()
        leftRect.y=rightRect.y
        
        bottomSide=self.getBottomRect()
        bottomRect=bottomSide.get_rect()
        bottomRect.y=480
        bottomRect.x=topRect.x
        
        backSide=self.getBackRect()
        backSide=pygame.transform.scale(backSide,(150,150))
        backRect=backSide.get_rect()
        backRect.x=550
        backRect.y=560
        
        self.screen.blit(front,frontRect)
        
        self.screen.blit(rightSide,rightRect);
        self.screen.blit(topSide,topRect)
        self.screen.blit(leftSide,leftRect)
        self.screen.blit(bottomSide,bottomRect)
        self.screen.blit(backSide,backRect)
        pygame.display.update()
        
        
    def begin(self):
        '''Gameloop.'''
        self.screen=pygame.display.set_mode((700,750))
        while not self.readsExit:
            self.eventHandler()
            self.updateDisplay()
            #self.clock.tick(1)
        pygame.quit()
        
if __name__=="__main__":
    #import main
    print "done"

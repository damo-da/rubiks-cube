'''THE LAUNCHER.'''
from __future__ import print_function,division

from headers import *
from cube import *
from graphics import GUI
from time import sleep
import sys

print("Welcome to the Rubik's Cube!");

def fun():
    """This function is launched after the graphics has been initialized."""

    print('Generating random algorithm')
    algo=randomAlgorithm(20);
    print(algo)
    
    print('Applying random algorithm to the cube')
    c.action(algo);

    print('Getting the solution algorithm')
    answer=c.solve()
    print (answer)

    print('Applying the solution to the cube')
    c.action(answer);

    print('Is rubiks cube solved? {}'.format(c.isSolved()))

    print ("End of Program")

c=Cube()
#c.updateFaceColors();
graphics=GUI(c)
c.registerGraphicsHandler(graphics)
c.startRecording()
c.setFunction(fun)


graphics.begin()

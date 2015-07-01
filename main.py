'''THE LAUNCHER.'''
from __future__ import print_function,division

from headers import *
from cube import *
from graphics import GUI
from time import sleep
import sys
from utilities import *


algo=randomAlgorithm(20);

def fun():
    answer=c.solve()
    #answer="y";
    print ("Solved by: "+answer)
    
    # c.action(answer);
    #c.actionRealTime(answer);
    
    # print (c.isSolved())

    print ("End of initialFunction()")

c=Cube()
graphics=GUI(c)

c.action(algo);

c.setFunction(fun)
c.startRecording()
graphics.begin()

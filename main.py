'''THE LAUNCHER.'''
from __future__ import print_function,division

from headers import *
from cube import Cube
from graphics import GUI
from utilities import *


algo=randomAlgorithm(20);

def fun():
    # c.action(answer);
    # c.actionRealTime(answer);
    
    # print (c.isSolved())

    print ("End of initialFunction()")

c=Cube()
graphics=GUI(c)

algo="F Ri Ui"
c.action(algo);
answer=c.solve()
print ("Solved by: "+answer)
c.action(answer);

c.setFunction(fun)
c.startRecording()
graphics.begin()

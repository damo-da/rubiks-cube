
'''THE LAUNCHER.'''

from headers import *
from cube import *
from graphics import GUI
from time import sleep
'''Cube().action("R U Ri") would move the cube in R U Ri '''
'''Cube().solve() would return answer for solving the cube:'''
'''So by rules, Cube().action(Cube.solve()) would be Cube().reset().'''


def fun():
    algo="F U Fi Ui R U Ri Di B D Bi"
    #algo=c.randomAlgorithm(20);
    print algo;
    c.action(algo);
    answer=c.solve()
    print "Solved by: "+answer
    
    c.action(answer);
    
    
c=Cube()
graphics=GUI(c)

c.registerGraphicsHandler(graphics)
c.startRecording()

c.setFunction(fun)
graphics.begin()

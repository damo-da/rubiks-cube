

'''THE LAUNCHER.'''

from headers import *
from cube import *
from graphics import GUI

'''Cube().action("R U Ri") would move the cube in R U Ri '''
'''Cube().solve() would return answer for solving the cube:'''
'''So by rules, Cube().action(Cube.solve()) would be Cube().reset().'''

def fun():
    print "random algorithm: "
    algo=c.randomAlgorithm(50)
    algo=optimizeMoves(algo)
    c.action(algo);

    print "solving"
    answer=c.solve()
    print "Solved by: "+answer
    c.action(answer)

print optimizeMoves("D L Li B Bi L L Di D L ")

c=Cube()
graphics=GUI(c)
c.registerGraphicsHandler(graphics)
c.startRecording()
c.setFunction(fun)
graphics.begin()

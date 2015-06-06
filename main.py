'''THE LAUNCHER.'''

from headers import *
from cube import *
from graphics import GUI

'''Cube().action("R U Ri") would move the cube in R U Ri '''
'''Cube().solve() would return answer for solving the cube:'''
'''So by rules, Cube().action(Cube.solve()) would be Cube().reset().'''

c=Cube()
graphics=GUI(c)
print "random algorithm: "
algo=c.randomAlgorithm(25)
print algo

print "applying scramble algorithm"
c.action(algo)

print "solving"
answer=c.solve()
print answer

print "applying answer"
c.action(answer)

graphics.begin()

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
i=0
while True:
    algo=c.randomAlgorithm(50)
    algo="L L L Li B D Ri Fi Fi R Li D F Bi D B D Bi D Bi Fi Ri R Bi Fi L F Fi B D Ri Di R R Li Bi Di F Ri Li Ri D R Li B F Fi Li F L "
    print algo

    #print "applying scramble algorithm"
    c.action(algo)

    #print "solving"
    answer=c.solve()
    c.action(answer)
    
    i += 1
    print i
    
    #break

#print "applying answer"
#c.action(answer)

graphics.begin()

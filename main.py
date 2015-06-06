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
    algo="Ri Di D B F Bi L B Fi Fi Di Fi D Bi Bi Li F L R Di Bi D D F Bi F Ri Ri B Fi L Bi Bi Di B L Li Di Di L Bi L B Li D B D Li B L"
    print algo

    #print "applying scramble algorithm"
    c.action(algo)
    break

#print "applying answer"
#c.action(answer)

graphics.begin()

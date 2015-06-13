'''THE LAUNCHER.'''

from headers import *
from cube import *
from graphics import GUI
from time import sleep
import sys
'''Cube().action("R U Ri") would move the cube in R U Ri '''
'''Cube().solve() would return answer for solving the cube:'''
'''So by rules, Cube().action(Cube.solve()) would be Cube().reset().'''

def fun():

    #algo=randomAlgorithm(20);
    #print algo;
    
    #c.action(algo);
    answer=c.solve()
    print "Solved by: "+answer
    
    c.action(answer);
    #c.actionRealTime(answer);
    print c.isSolved();
    print "End of Program";
c=Cube()

#algo=opposite_of("R' F R F' U2 R' F R y' R2 U2 R U2");
#algo="U D Li Fi x Mi E S D U F"

graphics=GUI(c)
c.registerGraphicsHandler(graphics)
c.startRecording()
c.setFunction(fun)

#c.action(opposite_of(algo));
algo="Ri xi Ei Si Bi zi M x Ei Si zi Ri Ei Fi z E yi M z Li E M yi M F yi M L Ei xi y zi Fi L x zi F B yi Mi Ei B Mi xi yi D";

if True:
    c.action(algo)
    answer=c.solve()
    c.action(answer)
    print c.isSolved();
    sys.exit()
    i=0
    while True:
        i+=1
        print "round "+str(i)
        algo=randomAlgorithm(50)
        print algo
        c.action(algo);
        try:
            answer=c.solve();
        except:
            print "error in program";
            raise SystemError
        c.action(answer)
        if(not c.isSolved()):
            print "cube is not solved";
            raise SystemError;
        print "\n"
else:
    c.action(algo);
    
graphics.begin()

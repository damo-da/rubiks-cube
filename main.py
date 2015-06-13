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
    #answer=c.solve()
    #print "Solved by: "+answer
    
    #c.action(answer);
    #c.actionRealTime(answer);
    print c.isSolved();
    print "End of Program";
c=Cube()

#algo=opposite_of("R' U' R y' x' R U' R' F R U R' zi x");

graphics=GUI(c)
c.registerGraphicsHandler(graphics)
c.startRecording()
c.setFunction(fun)

#c.action(opposite_of(algo));
algo="z x E S xi Fi Ei xi Li M E S Di x E Fi Ri Li zi zi z Si Mi S Fi Bi Li x Ei Si B S R Ei xi R B E y L D Si D E z Fi y M";
#algo=opposite_of("y L' R2 B R' B L U2 L' B Mi xi");
if True:
    i=0
    while True:
        if(not c.isSolved()):
            print "broken at first";
            break;
        i+=1
        print "see problems.txt";
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
            break;
            print FaceColor.top
            print c.getSide(TOP_SIDE);
            print "";
            
            print FaceColor.bottom
            print c.getSide(BOTTOM_SIDE);
            print ""
            
            print FaceColor.left;
            print c.getSide(LEFT_SIDE);
            print "";
            
            print FaceColor.right;
            print c.getSide(RIGHT_SIDE);
            print "";
            print "cube is not solved";
            raise SystemError;
        print "\n"
else:
    c.action(algo);
    c.action(c.solve());
    pass
    
graphics.begin()

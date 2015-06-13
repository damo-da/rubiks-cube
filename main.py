'''THE LAUNCHER.'''

from headers import *
from cube import *
from graphics import GUI
from time import sleep
import sys


def fun():

    #algo=randomAlgorithm(20);
    #print algo;
    
    #c.action(algo);
    answer=c.solve()
    #answer="y";
    print "Solved by: "+answer
    
    c.action(answer);
    #c.actionRealTime(answer);
    print c.isSolved();
    print "End of Program";
c=Cube()
c.updateFaceColors();
graphics=GUI(c)
c.registerGraphicsHandler(graphics)
c.startRecording()
c.setFunction(fun)

#algo=opposite_of("y2 R U R' y' R2 Ui E R U' R' U R' U Ei R2");
algo="B M Ei Ri S B y y Mi S Fi z xi D y y R y B Ei B Fi E M x Bi Di Li S B Fi y zi Ei F Di Fi D z D R Di Ei Bi zi L"
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
    sys.exit();
else:
    c.action(algo);
    #c.action(c.solve());
    pass
 
graphics.begin()

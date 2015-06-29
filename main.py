'''THE LAUNCHER.'''
from __future__ import print_function,division

from headers import *
from cube import *
from graphics import GUI
from time import sleep
import sys

print("HI");
def fun():
    algo=randomAlgorithm(20);
    print(algo)
    
    c.action(algo);
    answer=c.solve()
    #answer="y";
    print ("Solved by: "+answer)
    
    c.action(answer);
    #c.actionRealTime(answer);
    print (c.isSolved())
    print ("HI")
    print ("End of Program")
c=Cube()
#c.updateFaceColors();
graphics=GUI(c)
c.registerGraphicsHandler(graphics)
c.startRecording()
c.setFunction(fun)


#algo=opposite_of("y2 R U R' y' R2 Ui E R U' R' U R' U Ei R2");
algo="S M z Si D xi Di L Fi R B2 M Ri M x Bi Li zi B yi Si y Ei yi L S Bi yi xi Ei R2 D xi Bi R xi xi zi M D2 zi yi Si F S Bi Di"
if False:
    i=0
    while True:
        if(not c.isSolved()):
            print("broken at first");
            break;
        i+=1
        print ("see problems.txt");
        print ("round "+str(i))
        algo=randomAlgorithm(50)
        print (algo)
        c.action(algo);
        try:
            answer=c.solve();
        except:
            print ("error in program");
            raise SystemError
        c.action(answer)
        if(not c.isSolved()):
            print (FaceColor.top)
            print (c.getSide(TOP_SIDE));
            print ("");
            
            print (FaceColor.bottom)
            print ( c.getSide(BOTTOM_SIDE) );
            print ("")
            
            print (FaceColor.left);
            print (c.getSide(LEFT_SIDE));
            print ("");
            
            print (FaceColor.right);
            print (c.getSide(RIGHT_SIDE));
            print ("");
            print ("cube is not solved");
            raise SystemError;
        print ("\n")
    sys.exit();
else:
    #c.action(randomAlgorithm(50));
    #c.actionRealTime(c.solve());
    #c.save('saves/1');
    #sys.exit();
    pass
 

graphics.begin()

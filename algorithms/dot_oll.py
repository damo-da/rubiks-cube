from headers import *
__all__=['algos']
__ALL__=['algos']

algos=[]

def getAnswerFor(cube):
    top=cube.getFaceColor().top
    
    num=0
    for box in cube.getSide(TOP_SIDE):
        if box.getType()==CORNER_BOX and box.xy.color==top.color:
            num += 1
    if num==2:
        while not(cube.boxAt(2,2,2).xy.color==top.color):
            cube.action("U")
        if cube.boxAt(2,0,2).xy.color==top.color:
            cube.action("Ui");
        if not (cube.boxAt(0,2,2).xy.color==top.color):
            cube.action("U")
            if not(cube.boxAt(0,0,2).yz.color==top.color and cube.boxAt(0,1,2).yz.color==top.color):
                cube.action("U2")
            #print "type is 34"
            cube.action("R U R' U R' F R F' U2 R' F R F'");
        else:
            if (cube.boxAt(0,0,2).xz.color==top.color and cube.boxAt(2,0,2).xz.color==top.color):
                cube.action("U2");
                #print "type is 33"
                cube.action("F R U R' U y' R' U2 R' F R F'")
            else:
                #print "type is 32"
                cube.action("R' U2 F R U R' U' y' R2 U2 x' R U x");
    elif num==1:
        while not(cube.boxAt(2,2,2).xy.color==top.color):
            cube.action("U");
        if cube.boxAt(2,0,2).yz.color==top.color:
            print "type 31"
            cube.action("R' U2 x R' U R U' y R' U' R' U R' F yi xi")
        else:
            cube.action("U");
            print "type 30";
            cube.action("y L' R2 B R' B L U2 L' B Mi xi")
    elif num==0:
        while not(cube.boxAt(0,0,2).xz.color==top.color and cube.boxAt(2,0,2).xz.color==top.color):
            cube.action("U");
        if cube.boxAt(2,2,2).xz.color==top.color and cube.boxAt(0,2,2).xz.color==top.color:
            cube.action("U");
            print "type is 28";
            cube.action("R U B' M L U L2 M2 x' U' R' F R F'");
        else:
            print "type is 29";
            cube.action("R' F R F' U2 R' F R y' R2 U2 R")
    else:
        #raise SystemError("invalid oll dot");
        print "different"
    return ""
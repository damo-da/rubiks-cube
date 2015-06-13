from headers import *
algos=[{"answer":"x R2 D2 R U R' D2 R U' R",
        "type":"1",
        "transitions":[
            {"from":(2,0),"to":(2,2)},
            {"from":(2,2),"to":(0,2)},
            {"from":(0,2),"to":(2,0)}
        ]},
        {"answer":"x Ri U Ri D2 R  Ui Ri D2 R2",
        "type":"2",
        "transitions":[
            {"from":(2,0),"to":(0,2)},
            {"from":(0,2),"to":(2,2)},
            {"from":(2,2),"to":(2,0)},
        ]},
        {"answer":"M2 U M2 U2 M2 U M2",
        "type":"3",
        "transitions":[
            {"from":(1,0),"to":(1,2)},
            {"from":(1,2),"to":(1,0)},
            {"from":(0,1),"to":(2,1)},
            {"from":(2,1),"to":(0,1)},
        ]},
        {"answer":"R' U' R2 U R U R' U' R U R U' R U' R' U2",
        "type":"4",
        "transitions":[
            {"from":(1,0),"to":(2,1)},
            {"from":(2,1),"to":(1,0)},
            {"from":(0,1),"to":(1,2)},
            {"from":(1,2),"to":(0,1)},
        ]},
        {"answer":"R' U R' U' R' U' R' U R U R2",
        "type":"5",
        "transitions":[
            {"from":(0,1),"to":(1,2)},
            {"from":(1,2),"to":(2,1)},
            {"from":(2,1),"to":(0,1)},
        ]},
        {"answer":"R2 U' R' U' R U R U R U' R",
        "type":"6",
        "transitions":[
            {"from":(0,1),"to":(2,1)},
            {"from":(2,1),"to":(1,2)},
            {"from":(1,2),"to":(0,1)},
        ]},
        {"answer":"R' F' L' F R F' L F R' F' L F R F' L' F",
        "type":"7",
        "transitions":[
            {"from":(0,0),"to":(2,0)},
            {"from":(2,0),"to":(0,0)},
            {"from":(0,2),"to":(2,2)},
            {"from":(2,2),"to":(0,2)},
        ]},
        {"answer":"U' R' U R U' R2 F' U' F U R F R' F' R2",
        "type":"8",
        "transitions":[
            {"from":(1,0),"to":(1,2)},
            {"from":(2,0),"to":(2,2)},
            {"from":(1,2),"to":(1,0)},
            {"from":(2,2),"to":(2,0)},
        ]},
        {"answer":"R U R' U' R' F R2 U' R' U' R U R' F'",
        "type":"9",
        "transitions":[
            {"from":(0,1),"to":(2,1)},
            {"from":(2,1),"to":(0,1)},
            {"from":(2,0),"to":(2,2)},
            {"from":(2,2),"to":(2,0)},
        ]},
        {"answer":"R U R' F' R U R' U' R' F R2 U' R' U'",
        "type":"10",
        "transitions":[
            {"from":(1,0),"to":(2,1)},
            {"from":(2,1),"to":(1,0)},
            {"from":(2,0),"to":(2,2)},
            {"from":(2,2),"to":(2,0)},
        ]},
        {"answer":"L' U' L F L' U' L U L F' L2 U L U",
        "type":"11",
        "transitions":[
            {"from":(0,0),"to":(0,2)},
            {"from":(0,2),"to":(0,0)},
            {"from":(1,0),"to":(0,1)},
            {"from":(0,1),"to":(1,0)},
        ]},
        {"answer":"R' U2 R U2 R' F R U R' U' R' F' R2 U'",
        "type":"12",
        "transitions":[
            {"from":(1,0),"to":(2,1)},
            {"from":(2,1),"to":(1,0)},
            {"from":(0,2),"to":(2,2)},
            {"from":(2,2),"to":(0,2)},
        ]},
        {"answer":"L U2 L' U2 L F' L' U' L U L F L2 U",
        "type":"13",
        "transitions":[
            {"from":(1,0),"to":(0,1)},
            {"from":(0,1),"to":(1,0)},
            {"from":(0,2),"to":(2,2)},
            {"from":(2,2),"to":(0,2)},
        ]},
        {"answer":"R' U R' U' B' D B' D' B2 R' B' R B R",
        "type":"14",
        "transitions":[
            {"from":(2,0),"to":(0,2)},
            {"from":(0,2),"to":(2,0)},
            {"from":(2,1),"to":(1,2)},
            {"from":(1,2),"to":(2,1)},
        ]},
        {"answer":"F R U' R' U' R U R' F' R U R' U' R' F R F'",
        "type":"15",
        "transitions":[
            {"from":(2,0),"to":(0,2)},
            {"from":(0,2),"to":(2,0)},
            {"from":(0,1),"to":(1,2)},
            {"from":(1,2),"to":(0,1)},
        ]},
        {"answer":"R' U R U' R' F' U' F R U R' F R' F' R U' R",
        "type":"16",
        "transitions":[
            {"from":(2,0),"to":(0,2)},
            {"from":(0,2),"to":(2,0)},
            {"from":(0,1),"to":(2,1)},
            {"from":(2,1),"to":(0,1)},
        ]},
        {"answer":"R U' R' U L M U F U' R' F' R U' R U Li Mi U R'",
        "type":"17",
        "transitions":[
            {"from":(0,0),"to":(2,2)},
            {"from":(2,2),"to":(0,0)},
            {"from":(0,1),"to":(2,1)},
            {"from":(2,1),"to":(0,1)},
        ]},
        {"answer":"y R2 U Ei R' U R' U' R Ui E R2 y' R' U R",
        "type":"18",
        "transitions":[
            {"from":(0,0),"to":(0,2)},
            {"from":(0,2),"to":(2,0)},
            {"from":(2,0),"to":(0,0)},
            {"from":(1,0),"to":(1,2)},
            {"from":(1,2),"to":(0,1)},
            {"from":(0,1),"to":(1,0)},
        ]},
        {"answer":"R' U' R y R2 U Ei R' U R U' R Ui E R2",
        "type":"19",
        "transitions":[
            {"from":(0,0),"to":(2,0)},
            {"from":(2,0),"to":(0,2)},
            {"from":(0,2),"to":(0,0)},
            {"from":(1,0),"to":(0,1)},
            {"from":(0,1),"to":(1,2)},
            {"from":(1,2),"to":(1,0)},
        ]},
        {"answer":"y R2 Ui E R U' R U R' U Ei R2 y R U' R'",
        "type":"20",
        "transitions":[
            {"from":(0,0),"to":(2,0)},
            {"from":(2,0),"to":(2,2)},
            {"from":(2,2),"to":(0,0)},
            {"from":(1,0),"to":(1,2)},
            {"from":(1,2),"to":(2,1)},
            {"from":(2,1),"to":(1,0)},
        ]},
        {"answer":"y2 R U R' y' R2 Ui E R U' R' U R' U Ei R2",
        "type":"21",
        "transitions":[
            {"from":(0,0),"to":(2,2)},
            {"from":(2,2),"to":(2,0)},
            {"from":(2,0),"to":(0,0)},
            {"from":(1,0),"to":(2,1)},
            {"from":(2,1),"to":(1,2)},
            {"from":(1,2),"to":(1,0)},
            ]
        }
];

def findTransitionsToMake(cube):
    #returns an array of required transitions, like
#list[{"from":(0,0),"to":(2,2)},{"from":(0,2),"to":(2,0)}]
    ret=[]
    for box in cube.getSide(TOP_SIDE):
        if cube.isSolvedAt(box.pos):
            continue
        
        transition=[0,0]
        
        if box.getType()==CORNER_BOX:
            colors=[]
            if box.xz:
                colors.append(box.xz.color)
            if box.yz:
                colors.append(box.yz.color)
                
            if FaceColor.front.color in colors:
                transition[1]=0;            
            elif FaceColor.back.color in colors:
                transition[1]=2;
            if FaceColor.left.color in colors:
                transition[0]=0;
            elif FaceColor.right.color in colors:
                transition[0]=2;            
        elif box.getType()==SIDE_BOX:
            color=box.xz
            if not color:
                color=box.yz
            assert(not color == None)
            
            if color.color==FaceColor.left.color:
                #print "YES";
                #print box.pos
                #print box.xz
                #print FaceColor.left.color
                transition=[0,1]
            elif color.color==FaceColor.right.color:
                transition=[2,1]
            elif color.color==FaceColor.back.color:
                transition=[1,2]
            elif color.color==FaceColor.front.color:
                transition=[1,0]
            else:
                raise SystemError("while making transition, unknown error 1 happened");
            #print transition
        else:
            raise SystemError("while making transition, unknown error 2 happened");
        
        statement={"from":(box.pos[0],box.pos[1]),"to":(transition[0],transition[1])}
        #assert(not(statement['from'] == statement['to']))
        ret.append(statement);
    return ret

def getAlgoForTransition(t):
    
    for algo in algos:
        if len(t)==len(algo['transitions']):
            match=True
            for transition in t:
                if transition not in algo['transitions']:
                    match=False;
                    break;
            if match:
                return algo
    return False;
def solve(cube):
    for i in range(0,4):
        cube.action("U");
        if cube.isSolved():
            return "";
    for i in range(0,4):
        count=0;
        while(count<4):
            count += 1;
            transitions=findTransitionsToMake(cube);
            #print len(transitions);
            #print transitions
            trans=getAlgoForTransition(transitions);
            if trans:
                print trans['type']
                return trans['answer']
            cube.action("U");
            #break;
        cube.action("y");
        #break;
    raise SystemError("unsolvavle PLL cube");
    
    return "";
'''Various utilities for Rubik's cube.'''

import random
from copy import deepcopy
from box import Box

def randomAlgorithm(count=20):
    '''Generates a random algorithm of required length.'''

    chars=["F","Fi","R","Ri","B","Bi","L","Li", "D", "Di","x","xi","M","Mi","y","yi","z","zi","E","Ei","S","Si"] 

    string=""
    index=len(chars)-1
    for i in range(count):
        string += chars[random.randint(0,index)] + " "

    return optimizeMoves(string)

def optimizeMoves(moves):
    '''Removes redundancy in algorithms.'''

    #a collection of all possible clockwise and anticlockwise moves
    chars=["F","B","L","R","U","D","X","Y","Z","M","E","S"]
    opps=["Fi",'Bi','Li','Ri','Ui','Di',"Xi","Yi","Zi","Mi","Ei","Si"]
    
    #forst convert all F and similar to Fi and similar
    moves=moves.replace("'","i")

    #add space in front and last, so the spaces are not ommited
    moves=" "+moves+" " 
    
    while "  " in  moves:
        moves=moves.replace("  "," ")
        
    #remove 2s from the text. eg: convert F2 to F F
    if "2" in moves:
        for i in range(len(chars)):
            moves=moves.replace(" {0}2 ".format(chars[i])," {0} {0} ".format(chars[i]))

    initial=moves    

    for i in range(len(chars)):
        cor=chars[i]
        opp=opps[i]
        
        #remove DDDD
        moves=moves.replace(" {0} {0} {0} {0} ".format(cor) ," ")
        moves=moves.replace(" {0} {0} {0} {0} ".format(opp) ," ")
        
        #remove FFi and FiF
        moves=moves.replace(" {0} {1} ".format(cor,opp), " ")
        moves=moves.replace(" {1} {0} ".format(cor,opp), " ")
        
        #change DDD to Di
        moves=moves.replace(" {0} {0} {0} ".format(opp)," {0} ".format(cor))
        moves=moves.replace(" {0} {0} {0} ".format(cor)," {0} ".format(opp))
    
    if moves != initial:#change has been made, recursion goes now
        moves=optimizeMoves(moves)
    
    #if no change, now go for adding 2s for FF,etc
    for i in range(len(chars)):
        cor=chars[i]
        opp=opps[i]
        
        #change FiFi and FF to F2 
        moves=moves.replace(" {0} {0} ".format(opp), " {0}2 ".format(cor))
        moves=moves.replace(" {0} {0} ".format(cor), " {0}2 ".format(cor))
    
    #trim moves
    moves=moves.lstrip().rstrip()
    
    return moves

def copyCube(boxes):
    '''Creates a clone of the boxes of rubik's cube.'''

    ret=[]

    for i in range(len(boxes)):
        box=Box(boxes[i].boxType)
        box.xz=deepcopy(boxes[i].xz)
        box.yz=deepcopy(boxes[i].yz)
        box.xy=deepcopy(boxes[i].xy)
        box.pos=deepcopy(boxes[i].pos)
        
        box.xzBox=boxes[i].xzBox
        box.yzBox=boxes[i].yzBox
        box.xyBox=boxes[i].xyBox
        ret.append(box)
    return ret

def split_algorithm(word):
    '''Split an algorithm into an array of single moves.'''
    

    word=word.replace("'","i")

    keys=word.split(" ")
    return keys

def opposite_of(algorithm):
    '''Returns the EXACT opposite of an algorithm.'''
    #suppose I sent it F D R, it would send me Ri Di Fi

    ret=""

    keys=split_algorithm(algorithm)
    keys.reverse()
    for key in keys:
        if "i" ==key[-1]:
            key=key[:-1]
        elif '2' ==key[-1]:
            pass
        else:
            key=key+"i"
        ret += " "+key+" ";

    return ret
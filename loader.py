'''This file helps to load a cube from a file'''

from box import *
from colors import decodeColorFromText
from box import *

def decode(line):
    '''Decodes line from the file.'''
    actions=line.split(',')
    if len(actions)<8: return None
    
    pos=(int(actions[0]),int(actions[1]),int(actions[2]))
    obj=None
    if actions[3].startswith('s'):#side box
        obj=SideBox()
    elif actions[3].startswith("cent"):#center box
        obj=CenterBox()
    elif actions[3].startswith("corn"):#corner box
        obj=CornerBox()
    obj.pos=pos
    
    obj.xz=decodeColorFromText(actions[4])
    obj.yz=decodeColorFromText(actions[5])
    obj.xy=decodeColorFromText(actions[6])
    #print obj.pos
    #print obj.yz
    #print
    return obj    

def loadCubeFromFile(fileName):
    '''Loads the cube structure from a file.
    Returns the cube itself.'''
    boxes=[]
    with open(fileName,'r') as f:
        lines=f.read().split("\n")
        for line in lines:
            if line.startswith("#"):
                continue
            elif len(line)<12:
                continue
            else:
                obj=decode(line)
                if obj:
                    boxes.append(obj)
    return boxes
if __name__=="__main__":
    array=loadCubeFromFile()

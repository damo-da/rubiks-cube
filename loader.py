'''This file helps to load a cube from a file'''
from headers import *
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
    
    return obj    
def encode(box):
    '''Encodes a box and returns the line for file storage.'''
    encode="{x},{y},{z},{box_type},{xz},{yz},{xy},"
    if box.getType()==SIDE_BOX:
        box_type="side";
    elif box.getType()==CORNER_BOX:
        box_type="corner";
    elif box.getType()==CENTER_BOX:
        box_type="center";
    else:
        raise SystemError("invalid box type to encode(box)");
    encode=encode.format(x=box.pos[0],y=box.pos[1],z=box.pos[2],box_type=box_type,xy=box.xy,xz=box.xz,yz=box.yz);
    
    return encode
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
def saveCubeToFile(cube,fileName):
    print "saving to %s"%fileName
    with open(fileName,'w') as f:
        for box in cube.boxes:
            line=encode(box)+"\n";
            f.write(line);
        
    return True
if __name__=="__main__":
    array=loadCubeFromFile()

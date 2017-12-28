import os
import json


def ReadMetaFile(name):
    metadata = open('metas/' + name, 'r')
    i = 0
    frame = metadata.readline()[:-1].replace("'", '"').replace("False", "false").replace("True", "true")
    while frame:
        if not os.path.exists('frames/' + name[:-5]):
            os.makedirs('frames/' + name[:-5])
        file = open('frames/' + name[:-5] + '/f' + str(i) + '.json', 'w')
        frame = metadata.readline()[:-1].replace("'", '"').replace("False", "false").replace("True", "true")
        file.write(frame)
        file.close()
        i += 1


def ReadMllMetas():
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir("metas") if isfile(join("metas", f))]
    for i in range(0, len(onlyfiles)):
        ReadMetaFile(onlyfiles[i])


def extractValidDataFromFrames():
    return ""

def getLane(x,y):
    if y>270:
        if x>500:
            return 550
        elif x>400:
            return 500
        else: return 450
    elif y>200:
        if x>500:
            return 550
        elif x>440:
            return 500
        else: return 450
    elif y>180:
        if x>500:
            return 550
        elif x>490:
            return 500
        else: return 450
    else:
        if x>510:
            return 550
        elif x>500:
            return 500
        else: return 450


def fixFrame(frame):

    for i in range (0,len(frame['objects'])):
        object = frame['objects'][i]
        x = object['bounding_box'][0]
        y = object['bounding_box'][1]
        object['bounding_box'][0] = getLane(x,y)
        if getLane(x,y) == 450:
            y -=150
        elif getLane(x,y) == 500:
            y -=175
        else: y -=200
        if(y<0):
            y=0
        y *=2.666666
        object['bounding_box'][0]=y
    return frame





def fixJson(jsonObject):
    for i  in range (0,len(jsonObject)):
        jsonObject[i] = fixFrame(0,jsonObject[i])


def MakeCarsFromFrame():
    from os import listdir
    from os.path import isfile, join
    paths = [f for f in listdir("frames") if isfile(join("frames", f))]
    for i in range(0, len(paths)):
       frames = extractValidDataFromFrames()
       fixJson("")

openMe("tetxt.txt")
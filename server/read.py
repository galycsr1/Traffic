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

def MakeVehiclesFromeFrames(path):





def MakeCarsFromFrame():
    from os import listdir
    from os.path import isfile, join
    paths = [f for f in listdir("frames") if isfile(join("frames", f))]
    for i in range(0, len(paths)):
        vehicles = MakeVehiclesFromeFrames(paths[i])


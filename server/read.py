import os
import json


def ReadMetaFile(name):
    metadata = open('metas/' + name, 'r+')
    i = 0
    frame = metadata.readline()[:-1].replace("'", '"').replace("False", "false").replace("True", "true")
    while frame:
        if not os.path.exists('frames/' + name[:-5]):
            os.makedirs('frames/' + name[:-5])
        file = open('frames/' + name[:-5] + '/f' + str(i) + '.json', 'w')
        #edit the line (json) before writing it
        #for objc in frame['objects']:
        #    print(objc['type'])

        file.write(frame)
        frame = metadata.readline()[:-1].replace("'", '"').replace("False", "false").replace("True", "true")
        file.close()
        i += 1


def ReadMllMetas():
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir("metas") if isfile(join("metas", f))]
    for i in range(0, len(onlyfiles)):
        print(onlyfiles[i])
        ReadMetaFile(onlyfiles[i])


def MakeCarsFromFrame():
    from os import listdir
    from os.path import isfile, join
    paths = [f for f in listdir("frames") if isfile(join("frames", f))]
    for i in range(0, len(paths)):
        vehicles = MakeVehiclesFromeFrames(paths[i])


def changeJson(jsFile):
    data = []
    for objc in jsFile['objects']:
        updatedObj = {"type": objc['type'], "created_at": objc['created_at'], "tracking_id": objc['tracking_id'], "bounding_box": objc['bounding_box']}
        data.append(updatedObj)
    jsFile['objects'] = data
    #print(jsFile)

#ReadMllMetas()
#ReadMetaFile('text.txt')
changeJson({"objects": [{"confidence": 0.92, "type": "bus", "static": True, "created_at": "2017-12-28 04:55:02.750086", "times_lost_by_convnet": 1, "speed": 13.65099956558118, "lost": False, "alert_tags": [], "tracking_id": 24488, "bounding_box": [386, 212, 105, 130], "new": False, "counted": False}, {"confidence": 0.58, "type": "car", "static": False, "created_at": "2017-12-28 04:55:41.927352", "times_lost_by_convnet": 1, "speed": 3.138550189376427, "lost": False, "alert_tags": [], "tracking_id": 24491, "bounding_box": [535, 304, 61, 57], "new": False, "counted": False}], "frame_index": 5443497})

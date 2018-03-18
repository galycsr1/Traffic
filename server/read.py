import os
import json


'''def ReadMetaFile(name):
    metadata = open('metas/' + name, 'r')
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
'''

def ReadMetaFile():
    file = open("big_28.12.2017-04_55_56.meta",'r')
    data = fixFile(file.read())
    print(data)
    #file.write(data)


def fixFile(data):
    jsons = data.replace("'", '"').replace("False", "false").replace("True", "true").split("\n")
    ans=[]
    for json in jsons:
        if json:
           json=changeJson(json)
           json = fixFrame(json)
           ans.append(json)
    return ans


'''def ReadAllMetas():
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir("metas") if isfile(join("metas", f))]
    for i in range(0, len(onlyfiles)):
        #print(onlyfiles[i])
        ReadMetaFile(onlyfiles[i])
'''

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
    ans=[]
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
        object['bounding_box'][1]=y
        ans.append(object)
    return ans


def fixJson(jsonObject):
    for i  in range (0,len(jsonObject)):
        jsonObject[i] = fixFrame(0,jsonObject[i])

'''def changeJsons(path):
    slash = len(path)
    for i in range (0, len(path)):
        if path[i]=='/':
            slash=1
            break
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(path[slash:]) if isfile(path[slash:], f)]
    for i in range(0, len(onlyfiles)):
'''



'''def fixFrames():
    from os import listdir
    from os.path import isfile, join
    paths = [f for f in listdir("frames") if isfile(join("frames", f))]
    for i in range(0, len(paths)):
        changeJsons(paths[i])

'''
import json


def changeJson(jsonFile):
    data = []
    jsFile = json.loads(jsonFile)
    for objc in jsFile['objects']:
        updatedObj = {"type": objc['type'], "created_at": objc['created_at'], "tracking_id": objc['tracking_id'], "bounding_box": objc['bounding_box']}
        data.append(updatedObj)
    jsFile['objects'] = data
    return jsFile

#ReadMetaFile()

#changeJson({"objects": [{"confidence": 0.92, "type": "bus", "static": True, "created_at": "2017-12-28 04:55:02.750086", "times_lost_by_convnet": 1, "speed": 13.65099956558118, "lost": False, "alert_tags": [], "tracking_id": 24488, "bounding_box": [386, 212, 105, 130], "new": False, "counted": False}, {"confidence": 0.58, "type": "car", "static": False, "created_at": "2017-12-28 04:55:41.927352", "times_lost_by_convnet": 1, "speed": 3.138550189376427, "lost": False, "alert_tags": [], "tracking_id": 24491, "bounding_box": [535, 304, 61, 57], "new": False, "counted": False}], "frame_index": 5443497})


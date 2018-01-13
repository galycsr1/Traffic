import os
import json

'''def read_meta_file(name):
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


def read_meta_file():
    file = open("big_28.12.2017-04_55_56.meta", 'r')
    data = fix_file(file.read())


def get_array(param):
    ans = [[], []]
    for i in range(0, len(param[1])):
        coordinates = param[1][i]
        ans[0].append(coordinates[0])
        ans[1].append(coordinates[1])
    return ans


def clean_routs(hash_vehicles):
#      array = get_array(hash_vehicles.popitem())
#      x = array[0]
#      y = array[1]
#      for i in range (0,len(x)):
#          print(len(x))
     return hash_vehicles


def clean_routs_jesons(hash_vehicles, jsons):
    list_index_hash_vehicles = []
    for json in jsons:
        objects = json['objects']
        for i in range(0, len(objects)):
            vehicle = objects[i]
            #print(vehicle)
            vehicle_id = vehicle['tracking_id']
            if not list_index_hash_vehicles.__contains__(vehicle_id):

                list_index_hash_vehicles[vehicle_id] = 0
            vehicle_list = hash_vehicles[vehicle_id]
            vehicle_index_count = list_index_hash_vehicles[vehicle_id]
            vehicle['bounding_box'][0] = vehicle_list[vehicle_index_count]['y']
            vehicle['bounding_box'][1] = vehicle_list[vehicle_index_count]['x']
            list_index_hash_vehicles[vehicle_id] += 1
    return jsons


def clean_data(data):
    jsons = data.replace("'", '"').replace("False", "false").replace("True", "true").split("\n")
    ans=[]
    hash_vehicles = {}
    for frame in jsons:
        try:
            json_frame = json.loads(frame)
        except ValueError:  # includes simplejson.decoder.JSONDecodeError
            pass
        objects = json_frame['objects']
        for i in range(0, len(objects)):
            vehicle = objects[i]
            vehicle_id = int(vehicle['tracking_id'])
            coordinates = [[], []]
            if not hash_vehicles.__contains__(vehicle_id):
                hash_vehicles[vehicle_id] = list()
            coordinates[0] = vehicle['bounding_box'][0]
            coordinates[1] = vehicle['bounding_box'][1]
            hash_vehicles[vehicle_id].append(coordinates)
            # if (vehicle_id ==24488):
            #     print (hash_vehicles[vehicle_id])
    hash_vehicles = clean_routs(hash_vehicles)
    return jsons


def fix_file(data):
    jsons = clean_data(data)
    ans = []
    for json in jsons:
        if json:
            json = change_json(json)
            json = fix_frame(json)
            ans.append(json)
    return ans


'''def ReadAllMetas():
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir("metas") if isfile(join("metas", f))]
    for i in range(0, len(onlyfiles)):
        #print(onlyfiles[i])
        read_meta_file(onlyfiles[i])
'''


def get_lane(x, y):
    if y > 270:
        if x > 500:
            return 550
        elif x > 400:
            return 500
        else:
            return 450
    elif y > 200:
        if x > 500:
            return 550
        elif x > 440:
            return 500
        else:
            return 450
    elif y > 180:
        if x > 500:
            return 550
        elif x > 490:
            return 500
        else:
            return 450
    else:
        if x > 510:
            return 550
        elif x > 500:
            return 500
        else:
            return 450


def fix_frame(frame):
    ans = []
    for i in range(0, len(frame['objects'])):
        object = frame['objects'][i]
        x = object['bounding_box'][0]
        y = object['bounding_box'][1]
        object['bounding_box'][0] = get_lane(x, y)
        if get_lane(x, y) == 450:
            y -= 150
        elif get_lane(x, y) == 500:
            y -= 175
        else:
            y -= 200
        if (y < 0):
            y = 0
        y *= 2.666666
        object['bounding_box'][1] = y
        ans.append(object)
    return ans


def fix_json(json_object):
    for i in range(0, len(json_object)):
        json_object[i] = fix_frame(0, json_object[i])


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


def change_json(json_file):
    data = []
    jsFile = json.loads(json_file)
    for objc in jsFile['objects']:
        updatedObj = {"type": objc['type'], "created_at": objc['created_at'], "tracking_id": objc['tracking_id'],
                      "bounding_box": objc['bounding_box']}
        data.append(updatedObj)
    jsFile['objects'] = data
    return jsFile


#read_meta_file()

# change_json({"objects": [{"confidence": 0.92, "type": "bus", "static": True, "created_at": "2017-12-28 04:55:02.750086", "times_lost_by_convnet": 1, "speed": 13.65099956558118, "lost": False, "alert_tags": [], "tracking_id": 24488, "bounding_box": [386, 212, 105, 130], "new": False, "counted": False}, {"confidence": 0.58, "type": "car", "static": False, "created_at": "2017-12-28 04:55:41.927352", "times_lost_by_convnet": 1, "speed": 3.138550189376427, "lost": False, "alert_tags": [], "tracking_id": 24491, "bounding_box": [535, 304, 61, 57], "new": False, "counted": False}], "frame_index": 5443497})

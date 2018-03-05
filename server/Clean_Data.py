import json


def get_array(param):
    ans = [[], []]
    for i in range(0, len(param[1])):
        coordinates = param[1][i]
        ans[0].append(coordinates[0])
        ans[1].append(coordinates[1])
    return ans


def clean_routs(hash_vehicles):
    while hash_vehicles.__len__() > 0:
        array = get_array(hash_vehicles.popitem())
        x = array[0]
        y = array[1]

    return hash_vehicles


def clean_routs_jsons(hash_vehicles, jsons):
    list_index_hash_vehicles = []
    for json in jsons:
        objects = json['objects']
        for i in range(0, len(objects)):
            vehicle = objects[i]
            vehicle_id = int(vehicle['tracking_id'])
            if not list_index_hash_vehicles.__contains__(vehicle_id):
                list_index_hash_vehicles[vehicle_id] = 0
            vehicle_list = hash_vehicles[vehicle_id]
            vehicle_index_count = list_index_hash_vehicles[vehicle_id]
            vehicle['bounding_box'][0] = vehicle_list[vehicle_index_count]['y']
            vehicle['bounding_box'][1] = vehicle_list[vehicle_index_count]['x']
            list_index_hash_vehicles[vehicle_id] += 1
    return jsons


def clean(data):
    jsons = data.replace("'", '"').replace("False", "false").replace("True", "true").split("\n")
    ans = []
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
    #hash_vehicles = clean_routs(hash_vehicles)
    normalizeData(hash_vehicles)
    return jsons, hash_vehicles

def normalizeData(vehiclesPath):
    for path in vehiclesPath:
        start_location = vehiclesPath[path][0]
        end_location = vehiclesPath[path][len(vehiclesPath[path])-1]
        # We'll check that every location is in the range in x axis and in y axis
        # between the start and end location and delete location that doesn't satisfies that
        vehiclesPath[path] = [location for location in vehiclesPath[path] if checkInRange(start_location[0], end_location[0], location[0])]
        vehiclesPath[path] = [location for location in vehiclesPath[path] if checkInRange(start_location[1], end_location[1], location[1])]

        #for location in path:
            #x_loc = location[0]
            #y_loc = location[1]
            #if not (start_location[0] <= x_loc <= end_location[0] or end_location[0] <= x_loc <= start_location[0])
            #somelist = [x for x in somelist if not determine(x)]

def checkInRange(start, end, currenLocation):
    # check x/y axis
    ans = True
    if not (start <= currenLocation <= end or end <= currenLocation <= start):
        # anaomality detected
        ans = False
    return ans
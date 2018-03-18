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
    vehiclesSpeed = {}
    # Extract path for each vehicle by collecting location per frame from the current JSON file
    for frame in jsons:
        try:
            json_frame = json.loads(frame)
        except ValueError:  # includes simplejson.decoder.JSONDecodeError
            pass
        objects = json_frame['objects']
        # Extract location of each vehicle in the current frame
        for i in range(0, len(objects)):
            vehicle = objects[i]
            vehicle_id = int(vehicle['tracking_id'])
            coordinates = [[], []]
            if not hash_vehicles.__contains__(vehicle_id):
                hash_vehicles[vehicle_id] = list()
            if not vehiclesSpeed.__contains__(vehicle_id):
                vehiclesSpeed[vehicle_id] = list()
            coordinates[0] = vehicle['bounding_box'][0]
            coordinates[1] = vehicle['bounding_box'][1]
            hash_vehicles[vehicle_id].append(coordinates)
            vehiclesSpeed[vehicle_id].append(vehicle['speed'])

    #hash_vehicles = clean_routs(hash_vehicles)
    normalizeData(hash_vehicles, vehiclesSpeed)
    updateJson(jsons, hash_vehicles)
    return jsons

def updateJson(jsonFile, vehiclesPath):
    # Pass through all the frames in order to update them
    for frame in jsonFile:
        try:
            jsonFrame = json.loads(frame)
        except ValueError:  # includes simplejson.decoder.JSONDecodeError
            pass
        objects = jsonFrame['objects']
        # Update location of each vehicle in the current frame
        for i in range(0, len(objects)):
            vehicle = objects[i]
            vehicle_id = int(vehicle['tracking_id'])
            currentVehiclePath = vehiclesPath[vehicle_id]
            modifiedLocation = currentVehiclePath.pop(0)
            vehicle['bounding_box'][0] = modifiedLocation[0]
            vehicle['bounding_box'][1] = modifiedLocation[1]

def normalizeData(vehiclesPath, vehiclesSpeed):
    # Fix and handle locations of vehicles from given data
    for path in vehiclesPath:
        start_location = vehiclesPath[path][0]
        end_location = vehiclesPath[path][len(vehiclesPath[path])-1]

        # First Stage:
        #   We'll check that every location is in the range in x axis and in y axis
        #   between the start and end location and then change locations that doesn't satisfies that
        #   We'll change these locations to the boundaries. Which means: to max value if bigger or to
        #   min value if smaller. Do it whether in x/y axis or in both axes
        for location in vehiclesPath[path]:
            location[0] = checkInRangeAndFit(start_location[0], end_location[0], location[0])
            location[1] = checkInRangeAndFit(start_location[1], end_location[1], location[1])

        # Second Stage:
        #   We'll check(and fix if needed) that the vehicle movement is linear. Which means that if in x/y axis we start
        #   in high number and end in lower number, the numbers should be going down all the way or vice versa.
        linearMovement(start_location, vehiclesPath[path])

    # Third Stage:
    #   We'll fix logically impossible sampled speeds. For example speeds that are too high.


def checkInRangeAndFit(start, end, currentLocation):
    # check x/y axis
    newLocation = currentLocation
    if not (start <= currentLocation <= end or end <= currentLocation <= start):
        # anomaly detected
        if currentLocation > start:
            if end > start:
                newLocation = end
            else:
                newLocation = start
        else:
            if end > start:
                newLocation = start
            else:
                newLocation = end
    return newLocation

def linearMovement(start, path):
    index = 1
    # check if the movement is from higher to lower numbers or vice versa
    directionX = checkForDirection(start, path[index], 0)
    directionY = checkForDirection(start, path[index], 1)
    while index < len(path):
        # if not the last location in path (maybe redundant)
        if index != len(path) - 1:
            if directionX == "unknown":
                directionX = checkForDirection(path[index], path[index+1], 0)
            if directionY == "unknown":
                directionY = checkForDirection(path[index], path[index + 1], 1)
            # if isOK = True, move to the next index else 'fix' the location in index+1
            isOkX = checkIfLinear(path[index], path[index+1], directionX, 0)
            if not isOkX:
                path[index + 1][0] =  path[index][0]
            isOkY = checkIfLinear(path[index], path[index+1], directionY, 1)
            if not isOkY:
                path[index + 1][1] =  path[index][1]
            else:
                index += 1
        else:
            index += 1

def checkForDirection(locFrom, locTo, xORy):
    direction = "unknown"
    if locFrom[xORy] > locTo[xORy]:
        direction = "down"
    elif locFrom[xORy] < locTo[xORy]:
        direction = "up"
    # else there is no difference between the locations
    return direction

def checkIfLinear(locFrom, locTo, direction, xORy):
    ans = True
    if direction != "unknown":
        if direction == "up":
            if locFrom[xORy] > locTo[xORy]:
                ans = False
        else: # direction = down
            if locTo[xORy] > locFrom[xORy]:
                ans = False
    return ans

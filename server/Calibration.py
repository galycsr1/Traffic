def get_incline(p1, p2):
    if p1[0] == p2[0] and p1[1] > p2[1]:
        return -9999999
    if p1[0] == p2[0] and p1[1] < p2[1]:
        return 9999999
    return (p1[1] - p2[1]) / (p1[0] - p2[0])


def is_lane(lane, x, y):
    min_x = lane[0]
    min_y = lane[0]
    max_x = lane[0]
    max_y = lane[0]
    for i in range(0, 4):
        if min_x[0] > lane[i][0]:
            min_x = lane[i]
        if max_x[0] < lane[i][0]:
            max_x = lane[i]
    for i in range(0, 4):
        if min_y[1] > lane[i][1] != min_x[1] and lane[i][0] != min_x[0]:
            min_y = lane[i]
        if max_y[1] < lane[i][1] != max_x[1] and lane[i][0] != max_x[0]:
            max_y = lane[i]
    # print("min y:", min_y)
    # print("min x:", min_x)
    # print("max y:", max_y)
    # print("max x:", max_x) debug
    if min_x[0] > x or max_x[0] < x:
        return False
    if min_y[1] > y or max_y[1] < y:
        return False
    if get_incline(min_x, min_y) > get_incline(min_x, [x, y]):
        # print(min_x) debug
        # print(min_y)
        # print(get_incline(min_x, min_y))
        # print(get_incline(min_x, [x, y]))
        return False
    if max_y[0] < x and get_incline(max_y, max_x) < get_incline(max_y, [x, y]):
        return False
    if max_y[0] > x and get_incline(min_x, max_y) < get_incline(min_x, [x, y]):
        return False
    if min_y[0] < x and get_incline(min_y, max_x) > get_incline(min_y, [x, y]):

        return False
    return True


def get_lane(x, y, info):
    lane1 = info[0]
    lane2 = info[1]
    lane3 = info[2]
    if is_lane(lane1['points'], x, y):
        return 550
    elif is_lane(lane2['points'], x, y):
        return 500
    elif is_lane(lane3['points'], x, y):
        return 450
    # print("x:",x ,"y:",y)
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


def fix_frame(frame, info):
    ans = []
    for i in range(0, len(frame['objects'])):
        object = frame['objects'][i]
        x = object['bounding_box'][0]
        y = object['bounding_box'][1]
        lane = get_lane(x, y, info)
        object['bounding_box'][0] = lane
        if lane == 450:
            y -= 150
        elif lane == 500:
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
import json
import server.Calibration
import server.Clean_Data
import server.Knowledge_Base


def fix_file(data,info_name):
    jsons, vehiclesPath = server.Clean_Data.clean(data)
    #lst = json.loads(jsons[0])
    #id = lst['objects'][0]['tracking_id']
    #print(id)
    #print(vehiclesPath[24547])
    info = json.load(open(info_name, 'r'))
    ans = []
    for frame in jsons:
        if frame:
            frame = strip_json(frame)
            frame = server.Calibration.fix_frame(frame, info['tracking_params']['lanes'])
            ans.append(frame)
        server.Knowledge_Base.store(ans)
    return ans

def strip_json(json_file):
    data = []
    jsFile = json.loads(json_file)
    for objc in jsFile['objects']:
        updatedObj = {"type": objc['type'], "created_at": objc['created_at'], "tracking_id": objc['tracking_id'],
                      "bounding_box": objc['bounding_box']}
        data.append(updatedObj)
    jsFile['objects'] = data
    return jsFile
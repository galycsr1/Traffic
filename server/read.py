import os
import json

metadata = open('big_22.12.2017-10_28_44.meta','r')
i = 0
frame = metadata.readline()[:-1].replace("'", '"').replace("False", "false").replace("True", "true")
while (frame) :
    name = 'frames/f' + str(i) +'.json'
    file = open(name, 'w')
    frame = metadata.readline()[:-1].replace("'", '"').replace("False", "false").replace("True", "true")
    file.write(frame)
    file.close()
    i+=1

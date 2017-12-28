#!/usr/bin/env python


import sys
from http.client import HTTPConnection
#get http server ip
http_server = sys.argv[1]
#create a connection
conn = HTTPConnection(http_server,8080)

while 1:
    cmd = input('input command (ex. GET dummy.html): ')
    print (cmd)
    cmd = cmd.split()
    print(cmd[0])
    print(cmd[1])
    print(cmd[2])

    if cmd[0] == 'exit': #tipe exit to end it
        break
    
    #request command to server
    conn.request(cmd[0],cmd[1],cmd[2])

    #get response from server
    rsp = conn.getresponse()
    
    #print server response and data
    print(rsp.status, rsp.reason)
    data_received = rsp.read()
    print(data_received)
    print(data_received)
    
conn.close()

#!/usr/bin/python3
import socket
import sys
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.18', 8899))
content = bytes.fromhex('010300000002C40B')

while True:
    s.send(content)
    res = s.recv(100).hex()
    print(res)
    dt = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    wetness = int(res[6:10],16)/10
    tempture = int(res[10:14],16)/10
    print(str(dt) +",温度:" + str(tempture) + ",湿度:" + str(wetness) + "%")
    time.sleep(1)

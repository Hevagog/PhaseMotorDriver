# version    0.004 with 7bytes
import serial, string, struct, binascii
from serial import Serial
import matplotlib.pyplot as plt
import numpy as np
from queue import Queue
import timeit
# 768
import time

queue0 = Queue()
t1 = timeit.default_timer()
result = []

xP = []
xp = []
y1p = []
y2p = []
y3p = []
y4p = []
y5p = []
y6p = []

ya1 = []
ya2 = []
ya3 = []
yd1 = []
yd2 = []
yd3 = []
# from threading import Thread
serM = serial.Serial("COM9", 1000000)
serU = serial.Serial("COM4", 1000000)
while 1:


    m = 0
    line = serU.read(size=1729)
    print("DONE U")
    offset = 0

    for i in range(0, 1729, 7):
        # print("m",line[i])
        # print(line[i:i+6])
        if (i >= 1710 - offset):
            break
        f = bytes(line[i + offset:i + 8 + offset])

        # print(f)
        y = struct.unpack('BBBBHB', bytes(line[i + offset:i + 7 + offset]))
        if y[0] == 0:
            if (y[4] > m and y[1] < 16) or (y[4] > 60000 and y[1] < 16):
                xp.append(y[4])
                y1p.append(y[2])
                y2p.append(y[3])
                y3p.append(y[5])
                m = y[4]
                if y[1] > 8:
                    y4p.append(10)
                else:
                    y4p.append(0)
                if y[1] == 3 or y[1] == 11 or y[1] == 15:
                    y6p.append(10)
                else:
                    y6p.append(0)
                if y[1] == 5 or y[1] == 13 or y[1] == 15:
                    y5p.append(10)
                else:
                    y5p.append(0)

        else:
            for n in range(1, 5):
                offset += 1
                if (y[n] == 0):
                    break
            if (i >= 1710 - offset):
                break
            y = struct.unpack('BBBBHB', bytes(line[i + offset:i + 7 + offset]))

            if (y[0] == 0):
                if (y[4] > m and y[1] < 16) or (y[4] > 60000 and y[1] < 16):
                    m = y[4]
                    xp.append(y[4])
                    y1p.append(y[2])
                    y2p.append(y[3])
                    y3p.append(y[5])
                    if y[1] > 8:
                        y4p.append(10)
                    else:
                        y4p.append(0)
                    if y[1] == 3 or y[1] == 11 or y[1] == 15:
                        y6p.append(10)
                    else:
                        y6p.append(0)
                    if y[1] == 5 or y[1] == 13 or y[1] == 15:
                        y5p.append(10)
                    else:
                        y5p.append(0)


    m = 0
    line = serM.read(size=1729)
    print("DONE M")
    offset = 0

    for i in range(0, 1729, 7):
        # print("m",line[i])
        # print(line[i:i+6])
        if (i >= 1710 - offset):
            break
        f = bytes(line[i + offset:i + 8 + offset])

        # print(f)
        y = struct.unpack('BBBBHB', bytes(line[i + offset:i + 7 + offset]))

        if y[0] == 0:
            if (y[4] > m and y[1] < 16) or (y[4] > 60000 and y[1] < 16):
                xp.append(y[4])
                y1p.append(y[2])
                y2p.append(y[3])
                y3p.append(y[5])
                m = y[4]
                if y[1] > 8:
                    y4p.append(10)
                else:
                    y4p.append(0)
                if y[1] == 3 or y[1] == 11 or y[1] == 15:
                    y6p.append(10)
                else:
                    y6p.append(0)
                if y[1] == 5 or y[1] == 13 or y[1] == 15:
                    y5p.append(10)
                else:
                    y5p.append(0)

        else:
            for n in range(1, 5):
                offset += 1
                if (y[n] == 0):
                    break
            if (i >= 1710 - offset):
                break
            y = struct.unpack('BBBBHB', bytes(line[i + offset:i + 7 + offset]))

            if (y[0] == 0):
                if (y[4] > m and y[1] < 16) or (y[4] > 60000 and y[1] < 16):
                    m = y[4]
                    xp.append(y[4])
                    y1p.append(y[2])
                    y2p.append(y[3])
                    y3p.append(y[5])
                    if y[1] > 8:
                        y4p.append(10)
                    else:
                        y4p.append(0)
                    if y[1] == 3 or y[1] == 11 or y[1] == 15:
                        y6p.append(10)
                    else:
                        y6p.append(0)
                    if y[1] == 5 or y[1] == 13 or y[1] == 15:
                        y5p.append(10)
                    else:
                        y5p.append(0)




    print(xp)
    # print(yp)
    plt.plot(xp, y6p, color="red")
    plt.plot(xp, y5p, color="orange")
    plt.plot(xp, y4p, color="purple")
    plt.plot(xp, y3p, color="green")
    plt.plot(xp, y2p, color="blue")
    plt.plot(xp, y1p, color="yellow")
    plt.show()


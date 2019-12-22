# version    0.003 with 7bytes
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
gl =[]
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
from multiprocessing import Process


def func1():
    global gl
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

                    gl.put(y)


                    # print(gl)
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

                        # queue1.put(y[1])
                        # queue2.put(y[2])
                        # queue3.put(y[3])
                        # queue4.put(y[4])
                        # queue5.put(y[5])

                        gl.append(y)

                        # print(gl)
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


def func2():
    global gl
    serM = serial.Serial("COM9", 1000000)
    while 1:
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
                    # queue1.put(y[1])
                    # queue2.put(y[2])
                    # queue3.put(y[3])
                    # queue4.put(y[4])
                    # queue5.put(y[5])

                    gl.append(y)

                    # print(gl)
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
                        # queue1.put(y[1])
                        # queue2.put(y[2])
                        # queue3.put(y[3])
                        # queue4.put(y[4])
                        # queue5.put(y[5])

                        gl.append(y)

                        # print(gl)
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


def func3():
    global gl
    while (1):
        time.sleep(1)
        print("         ", gl)
        # if not queue5.empty():
        # print("WELL")
        #
        # q = queue1.get()
        #
        # if q > 8:
        #     yd3.append(10)
        # else:
        #     yd3.append(0)
        # if q == 3 or q == 11 or q == 15:
        #     yd1.append(10)
        # else:
        #     yd1.append(0)
        # if q == 5 or q == 13 or q == 15:
        #     yd2.append(10)
        # else:
        #     yd2.append(0)

        # #print(xP)
        # # print(yp)
        # plt.plot(xP, yd3, color="red")
        # plt.plot(xP, yd2, color="orange")
        # plt.plot(xP, yd1, color="purple")
        # plt.plot(xP, ya3, color="green")
        # plt.plot(xP, ya2, color="blue")
        # plt.plot(xP, ya1, color="yellow")
        # plt.show()
        #
        # print(xp)
        # # print(yp)
        # plt.plot(xp, y6p, color="red")
        # plt.plot(xp, y5p, color="orange")
        # plt.plot(xp, y4p, color="purple")
        # plt.plot(xp, y3p, color="green")
        # plt.plot(xp, y2p, color="blue")
        # plt.plot(xp, y1p, color="yellow")
        # plt.show()

    # else:
    #     print(end="")#"dupa")
    # bin()
    # print (y)
    # if y[4] > m or (y[4] > 60000 and y[1] < 16) and y[2] < 257 and y[1] < 16:


if __name__ == '__main__':

    print("im alive")
    p = Process(target=func1)
    p2 = Process(target=func2)
    p3 = Process(target=func3)

    # p.setDaemon(True)
    # p2.setDaemon(True)
    # p3.setDaemon(True)

    p.start()
    p2.start()
    p3.start()

    while True:
        pass

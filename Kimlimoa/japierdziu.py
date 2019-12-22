#version    0.002 with 7bytes
import serial, string ,struct,binascii
from serial import Serial
import matplotlib.pyplot as plt
import numpy as np
ser = serial.Serial("COM9", 1000000)
#768
m =0
while 1:
    line = ser.read(size=1729)
    offset = 0

    xp = []
    y1p = []
    y2p = []
    y3p = []
    for i in range(0 , 1729,7):
        #print("m",line[i])
        #print(line[i:i+6])
        if (i >= 1710 - offset):
            break
        f = bytes(line[i + offset:i+8 + offset])
        #print(f)
        y = struct.unpack('BBBBHB', bytes(line[i + offset:i+7 + offset]))
        if(y[0] == 0):
            if(y[4] > m or y[4]>60000 and y[2]<257):
                print(y)
                xp.append(y[4])
                y1p.append(y[2])
                y2p.append(y[3])
                y3p.append(y[5])
                m = y[4]


        else:
            for n in range(1 , 5):
                offset += 1
                if(y[n] == 0):
                    break
            if (i >= 1710 - offset):
                break
            y = struct.unpack('BBBBHB', bytes(line[i + offset:i+7 + offset]))
            if (y[0] == 0):
                if(y[4]>m or y[4]>60000 and y[2]<257):
                    print(y)
                    m = y[4]
                    xp.append(y[4])
                    y1p.append(y[2])
                    y2p.append(y[3])
                    y3p.append(y[5])



    print(xp)
    #print(yp)
    plt.plot(xp, y1p , color =  "green")
    plt.plot(xp, y2p ,color =  "blue")
    plt.plot(xp, y3p ,color =  "red")
    plt.show()


           # else:
           #     print(end="")#"dupa")
        #bin()
        #print (y)
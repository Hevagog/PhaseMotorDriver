import serial, string
from serial import Serial
ser = serial.Serial("COM4", 115200)
while 1:
    line = ser.read(size=1536)
    for i in line:

       bit = bin(i)
       print(bit)
       for n in bit:
           print(n)

    #print (line)



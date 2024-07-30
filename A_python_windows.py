import serial.tools.list_ports , serial , time, keyboard,sys
import numpy as np

def detect():
    mdict = {} 
    port = serial.tools.list_ports.comports()

    for i in range(len(port)):
        print((str(port[i])))

    print("which one?")
    if(str(port[0]).startswith("COM")):
        while(True):
            vin = input("COM")
            if(vin.isdigit()):
                mdict['selport'] = "COM"+str(vin)
                break
    elif(str(port[0]).startswith("/dev/ttyUSB")):
        selectport = int(input("/dev/ttyUSB"))
        mdict['selport'] = "/dev/ttyUSB"+ str(selectport)
    else:
        print("WTF")

    mdict['baudrate'] = int(input("baudrate "))

    mdict['check'] = int(input("OK ,  "+ str(mdict['selport']) +" WITH BAUD RATE "+str(mdict['baudrate']) +" HAS BEEN SELECTED . PLZ PRESS 0 TO CANCEL OR 1 TO PROCESS "))
    return mdict

mode = 0

Hdict = detect()
while(Hdict['check'] == 0):
    Hdict = detect()

uart = serial.Serial(port=Hdict['selport'],baudrate=Hdict['baudrate'],timeout=2)
#uart.open()
arr = []
arr2 = []
#print(arr)
while(True):
    if(mode == 0):
        print(uart.read())
    elif(mode == 1):
        arr.append(uart.read())
        #print(arr)
        for i in range (len(arr)):
            if(arr[i] != b'\x00'):
                arr2.append(int(arr[i]))
            else:
                print(','.join(map(str,arr2)))
                arr2.clear()

    if(keyboard.is_pressed('q')):
        uart.close()
        exit()

    if(keyboard.is_pressed('e')):
        uart.close()
        Hdict = detect()
        uart = serial.Serial(port=Hdict['selport'],baudrate=Hdict['baudrate'],timeout=2)

    if(keyboard.is_pressed('n')):
        print("YOU WANT TO REPLACE NULL WITH NEW LINE .PLZ PRESS 0 TO CANCEL OR 1 TO PROCESS ,PRESS 3 == DEFULT ")
        while(True):
            vin = input()
            if(vin.isdigit()):
                #print(type(vin))
                if(vin == str(3)):
                    mode = 0
                if(vin == str(1)):
                    mode = 1

                break   

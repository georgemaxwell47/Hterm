import serial.tools.list_ports , serial , time, keyboard
# in linux version first you must root and active env !

# for root su and sudo -s 
# for active env source env/bin/activate 
port = serial.tools.list_ports.comports()

for i in range(len(port)):
    print((str(port[i])))

print("which one?")
if(str(port[0]).startswith("COM")):
    selectport = int(input("COM"))
    selectport = "COM"+str(selectport)
elif(str(port[0]).startswith("/dev/ttyUSB")):
    selectport = int(input("/dev/ttyUSB"))
    selectport = "/dev/ttyUSB"+ str(selectport)
else:
    print("WTF")

buadrate = int(input("baudrate "))

check = int(input("OK ,  "+ str(selectport) +" WITH BAUD RATE "+str(buadrate) +" HAS BEEN SELECTED . PLZ PRESS 0 TO CANCEL OR 1 TO PROCESS "))
while(check == 0):
    port = serial.tools.list_ports.comports()

    for i in range(len(port)):
        print((str(port[i])))

    print("which one?")
    if(str(port[0]).startswith("COM")):
        selectport = int(input("COM"))
        selectport = "COM"+str(selectport)
    elif(str(port[0]).startswith("/dev/ttyUSB")):
        selectport = int(input("/dev/ttyUSB"))
        selectport = "/dev/ttyUSB"+ str(selectport)
    else:
        print("WTF")

    buadrate = int(input("baudrate "))

    check = int(input("OK ,"+ str(selectport) +" WITH BAUD RATE "+str(buadrate) +" HAS BEEN SELECTED . PLZ PRESS 0 TO CANCEL OR 1 TO PROCESS "))

uart = serial.Serial(port=selectport,baudrate=buadrate,timeout=2)
#uart.open()
while(True):
    print(uart.read())
    if(keyboard.is_pressed('q')):
        exit()
    


'''
if(uart.is_open):
    while(True):
        uart.in_waiting()

        if (size != 0):
            data = uart.read(size)
            print(data)

        else:
            print("NO DATA")
            time.sleep(1)

else:
    print("UART NOT OPEN")
'''

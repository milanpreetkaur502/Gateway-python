import serial
from time import sleep

print('-------------BEGIN-----')
wifi=serial.Serial('/dev/ttyACM0',115200,timeout=5)

wifi.write(b'AT+WlanScan=0,5\r')
sleep(2)
bytes=wifi.in_waiting
print(bytes)
recv=wifi.read(bytes)
print(recv)
print('----------DONE-------')
wifi.close()

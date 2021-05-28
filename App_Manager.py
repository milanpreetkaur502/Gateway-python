##Python Socket Client over Wifi(CC3220s AT) and Ethernet(imX6ull)
#Devp=ARV


import time
import socket
import serial
from datetime import datetime as clock

print("-"*50)
print(" "*20+"APPLICATION")
PHY=int(input('Choose connection Type 1-Wifi, 2-Ethernet=>'))
SERVER_IP=input('Enter server IP address as x.x.x.x=>')
PORT=input('Enter server PORT=>')
sd=''
DEL=0.3
def Sock_create():
    print(" "*10+"CREATE")
    global sd
    global eth
    if PHY==1:
        wifi.write(b'AT+Socket=INET,STREAM,TCP\r')
        time.sleep(DEL)
        n_bytes=wifi.in_waiting
        r_bytes=str(wifi.read(n_bytes))
        sd=r_bytes[r_bytes.find(':')+1]
        print(r_bytes)
        print("sd->%s",sd)
    elif PHY==2:
        eth=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("-"*20)

def Sock_connect(ip,port):
    print(" "*10+"CONNECT")
    if PHY==1:
        cmd=bytes('AT+Connect='+sd+',INET,'+port+',['+ip+']\r','utf-8')
        print(cmd)
        wifi.write(cmd)
        time.sleep(DEL)
        n_bytes=wifi.in_waiting
        r_bytes=str(wifi.read(n_bytes))
        print(r_bytes)
    elif PHY==2:
        eth.connect((ip, int(port)))
    print("-"*20)
    
def Sock_send(data):
    print(" "*10+"SEND")
    if PHY==1:
        n_bytes=str(len(data))
        cmd=bytes('AT+Send='+sd+',0,'+n_bytes+','+data+'\r','utf-8')
        print(cmd)
        wifi.write(cmd)
        time.sleep(DEL)
        n_bytes=wifi.in_waiting
        r_bytes=str(wifi.read(n_bytes))
        print(r_bytes)
    elif PHY==2:
        eth.sendall(bytes(data,'utf-8'))
    print("-"*20)
    
def Sock_close():
    print(" "*10+"CLOSE")
    if PHY==1:
        cmd=bytes('AT+Close='+sd+'\r','utf-8')
        print(cmd)
        wifi.write(cmd)
        time.sleep(2)
        n_bytes=wifi.in_waiting
        r_bytes=str(wifi.read(n_bytes))
        print(r_bytes)
    elif PHY==2:
        eth.close()
    print("-"*20)
    
def WLAN_connect():
    print(" "*10+"WLAN")
    wifi.write(b'AT+WlanConnect=CHENAB,,WPA_WPA2,9810762494,,,\r')
    time.sleep(2)
    n_bytes=wifi.in_waiting
    r_bytes=str(wifi.read(n_bytes))
    print(r_bytes)
    print("-"*20)


if PHY==1:
    wifi=serial.Serial('COM8',115200,timeout=5)
    wifi=serial.Serial('/dev/ttyACM0',115200,timeout=5)
    WLAN_connect()
    time.sleep(1)

Sock_create()
Sock_connect(SERVER_IP,PORT)
d=(clock.now()).strftime("D%d%m%yT%H%M")
Sock_send(d)
Sock_close()

if PHY==1:
    wifi.close()

import time
import socket
import serial

print("-"*50)
print(" "*20+"HTTP TEST SERVER OVER SOCKET")

sd=''
DEL=0.3
r_bytes=''

########FUNCTION DEFINED##############
def wifi_read(d):
    global r_bytes
    time.sleep(d)
    n_bytes=wifi.in_waiting
    r_bytes=str(wifi.read(n_bytes))
    print(r_bytes)

def AP_config():
    print("--AP Config--")
    wifi.write(b'AT+WlanSetMode=AP\r')
    wifi_read(0.5)
    wifi.write(b'AT+WlanSet=AP,SSID,BLEGateway\r')
    wifi_read(0.5)
    wifi.write(b'AT+Stop=0\r')
    wifi_read(0.5)
    wifi.write(b'AT+Start\r')
    wifi_read(5)
    print("-------------")

def sock_create():
    global sd
    print("--Socket Create--")
    wifi.write(b'AT+Socket=INET,STREAM,TCP\r')
    wifi_read(0.5)
    sd=r_bytes[r_bytes.find('t:')+2]
    print("-------------")

def sock_config():
    print("--Socket Config--")
    cmd='AT+SetSockOpt='+sd+',SOCKET,RCVTIMEO,1,0\r'
    wifi.write(bytes(cmd,'utf-8'))
    wifi_read(0.3)
    print("-------------")

def sock_bind():
    print("--Socket Bind--")
    cmd='AT+Bind='+sd+',INET,5555,[0.0.0.0]\r'
    wifi.write(bytes(cmd,'utf-8'))
    wifi_read(0.3)
    print("-------------")

def sock_listen():
    print("--Socket Bind--")
    cmd='AT+Listen='+sd+',LISTEN\r'
    wifi.write(bytes(cmd,'utf-8'))
    wifi_read(0.3)
    print("-------------")

def sock_accept():
    print("--Socket Accept--")
    cmd='AT+Accept='+sd+',INET\r'
    wifi.write(bytes(cmd,'utf-8'))
    wifi_read(0.3)
    print("-------------")

def sock_read():
    print("--Socket Read--")
    cmd='AT+Recv='+sd+',0,4096\r'
    wifi.write(bytes(cmd,'utf-8'))
    wifi_read(0.3)
    print("-------------")

def sock_send():
    print("---Socket Send---")
    cmd='AT+Send='+sd+',0,5,hello\r'
    wifi.write(bytes(cmd,'utf-8'))
    wifi_read(0.3)
    print("-------------")

def sock_close():
    print("---Socket Close---")
    cmd='AT+Close='+sd+'\r'
    wifi.write(bytes(cmd,'utf-8'))
    wifi_read(0.3)
    print("-------------")
    


#############MAIN FUNCTION#######################
wifi=serial.Serial('COM8',115200,timeout=5)
AP_config()
sock_create()
sock_config()
sock_bind()
sock_listen()
sock_accept()

while True:
    wifi_read(0.3)
    if r_bytes.find('accept')>0:
        time.sleep(5)
        sock_send()
        break
    time.sleep(3)
    

sock_close()
wifi.close() 
    
    

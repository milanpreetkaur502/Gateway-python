
ENB=open("/sys/devices/virtual/misc/FreescaleAccelerometer/enable","w")
ENB.write('1')
ENB.close

VAL=open("/sys/devices/virtual/misc/FreescaleAccelerometer/data","r")
r=VAL.readline()
print(r)
VAL.close

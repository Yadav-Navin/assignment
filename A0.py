from datetime import datetime
import sys
dt=datetime.today()
print(dt)
d1=dt.strftime("%H:%M:%S")
print(d1)
print(sys.version)
#we are using keywords as a data in script
print(True)
date='15-5-2023'
time='8:50PM'
print(date,time)
number=22
print(type(number))
print(type(str(number)))
y=65
r='c'
z='A'
print(chr(100))
print(ord('t'))
print(bin(45))
print(oct(55))
print(hex(1789))
ox=0x2F
print(oct(ox))
by=1100101

ot=125
print(bin(ot))

oc=0o25
hx=0x39
na=oct(oc)
ma=hex(hx)
print(na)
print(ma)
add=na+ma
print(add)

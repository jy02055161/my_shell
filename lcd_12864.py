from machine import Pin
import time

rs=Pin(15,Pin.OUT)
rw=Pin(14,Pin.OUT)
e=Pin(13,Pin.OUT)
d0=Pin(12,Pin.IN)
d1=Pin(11,Pin.IN)
d2=Pin(10,Pin.IN)
d3=Pin(9,Pin.IN)
d4=Pin(8,Pin.IN)
d5=Pin(7,Pin.IN)
d6=Pin(6,Pin.IN)
d7=Pin(5,Pin.OUT)
psb=Pin(4,Pin.OUT)
data_list=[d0,d1,d2,d3,d4,d5,d6,d7]

def e_down():
    e.value(1)
    e.value(0)
def cl_data():
    psb.value(1)
    for i in data_list:
        i.value(0)
cl_data()

def check_busy():
    rs.value(0)
    rw.value(1)
    e_down()
    is_busy=d7.value()
    print("is_busy:%s"%is_busy)


def send_cmd(cmd):
    check_busy()
    rs.value(0)
    rw.value(0)
    for i in range(8):
        data_list[i].value(cmd[i])
    e_down()
    
cl_data()
check_busy()
cmd1=[0,0,0,0,0,0,0,1]
time.sleep(0.1)
cmd2=[0,0,0,0,0,0,1,1]
time.sleep(0.1)
cmd3=[0,0,0,0,0,1,1,1]
send_cmd(cmd1)
send_cmd(cmd2)
send_cmd(cmd3)
from machine import Pin
import time
from My_tools.my_tools import bin_to_list as b2l,list_to_bin as l2b

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
data_list=[d7,d6,d5,d4,d3,d2,d1,d0]


def e_down():
    e.value(1)
    time.sleep_ms(5)
    e.value(0)
def check_busy():
    rs.value(0)
    rw.value(1)
    e_down()
    while d7.value():
        print("busy")
        pass
    
def w_cmd(cmd,is_data=0):
    check_busy()
    rs.value(is_data)
    rw.value(0)
    e.value(0)
    cmd=b2l(cmd)
    for i in range(8):
        data_list[i-1].value(cmd[i-1])
    e_down()
    
    
def init():
    psb.value(1)
    w_cmd(0x30)
    time.sleep_ms(5)
    w_cmd(0x0c)
    time.sleep_ms(5)
    w_cmd(0x1)
    time.sleep_ms(5)
    
def start():
    init()
    w_cmd(0x80)
    w_cmd(0xf7,is_data=1)


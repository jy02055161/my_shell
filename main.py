from machine import Pin
import utime as time
rs=Pin(15,Pin.OUT)
rw=Pin(14,Pin.OUT)
en=Pin(13,Pin.OUT)
d0=Pin(12,Pin.IN)
d1=Pin(11,Pin.IN)
d2=Pin(10,Pin.IN)
d3=Pin(9,Pin.IN)
d4=Pin(8,Pin.IN)
d5=Pin(7,Pin.IN)
d6=Pin(6,Pin.IN)
d7=Pin(5,Pin.IN)
psb=Pin(4,Pin.OUT)
data_list=[d0,d1,d2,d3,d4,d5,d6,d7]

def check_busy():
    print(__name__)
    flag =1
    while flag:
        rs.value(0)
        rw.value(1)
        en.value(0)
        time.sleep_us(50)
        en.value(1)
        if d7.value():
            time.sleep_us(100)
            pass
        else:
            return 0

def w_data_cmd(*d0_7,is_dat=0):
    check_busy()
    rs.value(is_dat)
    rw.value(0)
    en.value(0)
    for i in range(8):
        data_list[i].value(d0_7[i])
    en.value(1)
    time.sleep_us(50)
    en.value(0)

def init():
    psb.value(1)
    extend_cmd=[0,0,1,1,0,1,0,0]#0x34 扩充指令操作
    base_cmd=[0,0,1,1,0,1,0,0]#0x30 基本指令操作
    pr_cmd= [0,0,0,0,1,1,0,0]#0x0c 显示开，关光标
    cl_cmd= [0,0,0,0,0,0,0,1]

    res = [extend_cmd,base_cmd,pr_cmd,cl_cmd]
    for i in res:
        w_data_cmd(i)

def draw():
    cmd=[0,0,1,1,0,1,0,0] # 0x34 打开扩展指令集
    pic_0 = [1,0,0,0,0,0,0,0]
    pic_1=[1,0,1,1,1,1,1,1]
    pic_2=[1,0,0,0,1,1,1,1]
    w_data_cmd(cmd)#0x34
    w_data_cmd(pic_0)
    w_data_cmd(pic_2)
    w_data_cmd(pic_1)
    w_data_cmd([1,1,0,0,1,1,1,1],is_dat=1)

    w_data_cmd([0,0,1,1,0,1,1,0])
    w_data_cmd([0,0,1,1,0,0,0,0])

def start():
    init()
    draw()

start()
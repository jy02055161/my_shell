from machine import Pin
import utime as time

di = Pin(0, Pin.IN, Pin.PULL_UP)  # dat/di
do = Pin(1, Pin.OUT)  # cmd/do
cs = Pin(2, Pin.OUT)  # cs
clk = Pin(3, Pin.OUT)  # clk
T = 6
commands = [
    [1, 0, 0, 0, 0, 0, 0, 0],  # 1
    [0, 1, 0, 0, 0, 0, 1, 0],  # 66 0b01000010
]


def do_func(cmd):
    for i in cmd:
        do.value(i)
        clk.off()
        clk.on()


def do_di_func(cmd):
    res_list = []
    for i in cmd:
        do.value(i)
        clk.off()
        res_list.append(di.value())
        clk.on()
    return res_list


def di_func():
    res_list = []
    for i in range(8):
        clk.off()
        res_list.append(di.value())
        clk.on()
    return res_list


def cs_go():
    data = []
    cs.on()
    clk.on()
    do.on()
    cs.off()
    do_func(commands[0])
    data.append(do_di_func(commands[1]))
    for i in range(8):
        data.append(di_func())
    cs.on
    return (data)


def analysis_data(data):
    mode = data[0]
    code = data[1]
    key = data[2] + data[3]
    rx = data[4]
    ry= data[5]
    lx= data[6]
    ly = data[7]
    data_dic = {"code": code, "mode": mode, "key": key,
                "rx": rx, 
                "ry": ry, 
                "lx": lx,
                "ly": ly,
                }
    return data_dic


def list_to_binary(data, is_reversal=None):
    bin_list = [1, 2, 4, 8, 16, 32, 64, 128]
    index = 0
    res = 0
    if is_reversal:
        re_data = []
        for i in data:
            if i:
                re_data.append(0)
            else:
                re_data.append(1)
        data = re_data
    for i in data:
        if i:
            res |= bin_list[index]
        index += 1
    return res


def ps2_start():
    flag = 1
    while flag:
        time.sleep_ms(10)
        data = analysis_data(cs_go())
        key_num = 0
        for i in data['key']:
            key_num += 1
            if i == 0:
                print(key_num)
                if key_num == 1:
                    flag = 0
            if list_to_binary(data['mode'])==0b01110011:# 01110011，01000001green
                analog_list=['rx','ry','lx','ly']
                for i in analog_list:
                    analog=list_to_binary(data[i],True)
                    if (analog !=127) and (analog !=128) :
                        print(i,'Analog quantity:',analog)
                    
ps2_start()

'''
经测试，执行一次时间为3500微妙
t1=utime.ticks_us()
data=analysis_data(cs_go())
t2=utime.ticks_us()
print(utime.ticks_diff(t2,t1))
'''
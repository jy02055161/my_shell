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
    code = data[0]
    mode = data[1]
    key = data[2] + data[3]
    rx_left = data[4][0:4]
    rx_right = data[4][4:8]
    ry_left = data[5][0:4]
    ry_right = data[5][4:8]
    lx_left = data[6][0:4]
    lx_right = data[6][4:8]
    ly_left = data[7][0:4]
    ly_right = data[7][4:8]

    data_dic = {"code": code, "mode": mode, "key": key,
                "rx_left": rx_left, "rx_right": rx_right,
                "ry_left": ry_left, "ry_right": ry_right,
                "lx_left": lx_left, "lx_right": lx_right,
                "ly_left": ry_left, "ly_right": ry_right,
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


list_to_binary([1, 1, 3, 1], 0)


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

        '''        
        rx_left = list_to_binary(data['rx_left'],1)
        rx_right=list_to_binary(data['rx_right'],1)
        ry_left = list_to_binary(data['ry_left'],1)
        ry_right=list_to_binary(data['ry_right'],1)



        lx_left=list_to_binary(data['lx_left'],1)
        lx_right=list_to_binary(data['lx_right'],1)      
        ly_left = list_to_binary(data['ly_left'],1)
        ly_right=list_to_binary(data['ly_right'],1)


        if rx_left:
            print('rx_l',rx_left)
        if rx_right:
            print('rx_r',rx_right)
        if ry_left:
            print('ry_l',ry_left)
        if ry_right:
            print('ry_r',ry_right)

        if lx_left:
            print('rx_l',lx_left)
        if lx_right:
            print('rx_r',lx_right)
        if ly_left:
            print('ry_l',ly_left)
        if ly_right:
            print('ry_r',ly_right)          


        '''


ps2_start()

'''
经测试，执行一次时间为3500微妙
t1=utime.ticks_us()
data=analysis_data(cs_go())
t2=utime.ticks_us()
print(utime.ticks_diff(t2,t1))
'''
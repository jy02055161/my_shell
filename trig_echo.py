from machine import Pin
import time
def led_demo(n,sec,pin):
    led = Pin(pin,Pin.OUT)
    for i in range(n):
        led_on = led.value(True)
        time.sleep(sec)
        led_off = led.value(False)
        time.sleep(sec)
led_demo(3,0.3,25)


trig = Pin(1,Pin.OUT)
echo = Pin(0,Pin.IN)
trig.off()
echo.on()
def trig_on():
    trig.on()
    time.sleep_us(30)
    trig.off()

def trig_echo():
    '''
    开始测距
    1.向trig端发出20us的信号
    2.开始无限循环检测echo值,时间t_ms累加
        2.1 如果echo值为1退出。
        2.2 如果t_ms值超过临界值，退出循环。
    3.拿到t_ms的值，就是声波传输的时间
    '''
    t0 = time.ticks_us()
    trig_on()
    while 1:
        
        pass
        t1 = time.ticks_us()
        if(time.ticks_diff(t1,t0)>1000000):
            return 9999
        if echo.value()==1:       
            pass
            #360米每秒 1毫秒传播距离时0.36米 100微传播 0.036米，3.6厘米
            while echo.value()==0:
                t2=time.ticks_us()
                t3 = time.ticks_diff(t2,t1)
                return t3
                
            
echo_time = trig_echo()
print(echo_time)
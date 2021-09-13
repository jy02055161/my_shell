from machine import Pin
import utime
import machine
def led_demo(n,time,pin):
    led = Pin(pin,Pin.OUT)
    for i in range(n):
        led_on = led.value(True)
        utime.sleep(time)
        led_off = led.value(False)
        utime.sleep(time)
led_demo(3,0.2,4)

def temp_demo(n):
    sensor_temp = machine.ADC(4)
    conversion_factor = 3.3/(65535) 
    for i in range(n):
        reading = sensor_temp.read_u16()*conversion_factor
        res = 27 - (reading - 0.706)/0.001721
        print(res)
        print( sensor_temp.read_u16()*3.3/65535)
        led_demo(1,0.5,4)
temp_demo(6)

        
        

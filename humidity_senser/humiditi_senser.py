from machine import I2C,Pin,ADC
from ssd1306 import SSD1306_I2C
import time
i2c=I2C(0,sda=Pin(0),scl=Pin(1),freq=400000)
oled = SSD1306_I2C(128,64,i2c)
T=0.6

oled.fill(1)
oled.show()
oled.fill(0)
oled.show()
time.sleep(1)

humidity= ADC(28)
is_wet = Pin(27,Pin.IN)

flag = 1
t=3

while flag:
    time.sleep(0.3)
    oled.fill(0)
    res = humidity.read_u16()
    res2=is_wet.value()
    oled.text('humidity: %s'%(0xffff-res),0,0,1)

    oled.text('is_wet: %s' % bool(res2-1), 0, 10, 1)

    oled.text('t:%s' %t, 0, 30,1)
    oled.show()
from machine import I2C,Pin
from ssd1306 import SSD1306_I2C
import utime as time
cs=Pin(22)
i2c=I2C(0,sda=Pin(20),scl=Pin(21),freq=400000)
oled = SSD1306_I2C(128,64,i2c)
cs.off()
T=0.6

oled.fill(1)
oled.show()
oled.fill(0)
oled.show()
time.sleep(1)
oled.text('Hello world!',0,9,1)
oled.show()
time.sleep(1)
oled.pixel(20,20,1) #x20 y20处画点
oled.show()
time.sleep(1)
oled.line(10,10,20,20,1)# 画线
oled.show()
time.sleep(1)
oled.vline(30,30,20,1) # 画竖线
oled.show()
time.sleep(1)
oled.hline(30,30,20,1) #画横线
oled.show()
time.sleep(1)
oled.fill(1)
oled.show()
oled.fill(0)
oled.show()
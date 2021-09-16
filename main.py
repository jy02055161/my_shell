from machine import Pin

rs=Pin(15,Pin.OUT)
r_w=Pin(14,Pin.OUT)
e_sclk=Pin(13,Pin.OUT)
d0=Pin(12,Pin.IN)
d1=Pin(11,Pin.IN)
d2=Pin(10,Pin.IN)
d3=Pin(9,Pin.IN)
d4=Pin(8,Pin.IN)
d5=Pin(7,Pin.IN)
d6=Pin(6,Pin.IN)
d7=Pin(5,Pin.IN)
psb=Pin(4,Pin.OUT)


d7.value(1)



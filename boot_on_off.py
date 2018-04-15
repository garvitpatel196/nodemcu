import time
from machine import Pin
p0 = Pin(0, Pin.OUT)
while True:# create output pin on GPIO0
    p0.on()
    time.sleep(2)           # set pin to "on" (high) level
    p0.off()                # set pin to "off" (low) level
    time.sleep(2)

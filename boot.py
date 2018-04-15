import network
from umqtt.robust import MQTTClient
import machine
import time
from machine import Pin

p0 = Pin(0, Pin.OUT)
def sub_cb(topic, msg):
   if msg == b"ON":
       print("ON")
       p0.on()
       time.sleep(1)
   else:
       print("OFF")
       p0.off()                # set pin to "off" (low) level
       time.sleep(1)

def conn_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect("Garvit", "12345678")
    while not wlan.isconnected():
        machine.idle()
    print("Connected to Wifi\n")
    print(wlan.ifconfig())

def main(server="localhost"):
    conn_wifi()
    client = MQTTClient("client_2", "18.188.220.135", user="ximpact", password="ximpact.in",port=1883)
    client.set_callback(sub_cb)
    client.connect()
    client.subscribe(b"hello/lights")
    while True:
        if True:
            # Blocking wait for message
            client.wait_msg()
        else:
            # Non-blocking wait for message
            client.check_msg()
            # Then need to sleep to avoid 100% CPU usage (in a real
            # app other useful actions would be performed instead)
            time.sleep(1)

    client.disconnect()

if __name__ == "__main__":
    main()

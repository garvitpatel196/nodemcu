import network
from umqtt.robust import MQTTClient
import machine
import time

def sub_cb(topic, msg):
   print(msg)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("Moto", "idontknow")

while not wlan.isconnected():
    machine.idle()
print("Connected to Wifi\n")
print(wlan.ifconfig())
client = MQTTClient("client_1", "192.168.43.195", user="garvit", password="garvit",port=1883)
client.connect()
while True:
    print("Sending ON")
    client.publish(topic="hello/lights", msg="ON")
    time.sleep(1)
    print("Sending OFF")
    client.publish(topic="hello/lights", msg="OFF")
    time.sleep(1)


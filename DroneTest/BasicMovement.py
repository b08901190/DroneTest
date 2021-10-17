from djitellopy import tello
import time


me = tello.Tello()
me.connect()
print(me.get_battery())
while True:
    print(me.get_yaw())
from djitellopy import tello
import time


me = tello.Tello()
me.connect()
print(me.get_battery())
me.takeoff()
time.sleep(3)


me.land()
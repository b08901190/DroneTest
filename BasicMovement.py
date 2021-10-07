from djitellopy import tello
from time import sleep


me = tello.Tello()
me.connect()
print(me.get_battery())
me.takeoff()
sleep(0.1)
me.send_rc_control(0,0,0,100)
me.land()
import KeyboardControl as kc

kc.init()
# me = tello.Tello()
# me.connect()
# print(me.get_battery())
# initial_yaw = me.get_yaw() #得到初始的方向
while True:
    kc.KeyboardControl()
while True:
    vals = getKeyboardInput()
    startpoint = SetStartPoint()
    if startpoint != False:
        print(startpoint)
    time.sleep(0.05)
import KeyboardControl as kc
import Distance as d
from djitellopy import tello
import uwb_read as uwb
kc.init()
me = tello.Tello()
me.connect()
mode = "initial"
select_mode = True
free_fly = False
back_to_backpoint = False
test = True
initial_yaw = 0 ## the yaw that calculate when drone toward y direction
backpoint = "nan"
print(mode)
anchor_positions = [0,0,0]*4
while test == True :
    print("press j to free fly , press k to fly back , press y to quit this task" )
    while  select_mode :
        if kc.getKey("y"):
            print("end this fly")
            test = False
            select_mode = False
        if kc.getKey("j") :
            mode = "Fly freely"
            print(mode)
            free_fly = True
            select_mode = False
            break
        elif kc.getKey("k") :
            mode = "Start to go back"
            print(mode)
            back_to_backpoint = True
            select_mode = False
            break
    while free_fly :
        [lr,fb,ud,yv] = kc.KeyboardControl()
        me.send_rc_control(lr,fb,ud,yv)
        print("press u to quit free fly")

        if kc.getKey("q"):me.land()
    
        if kc.getKey("e"):me.takeoff()
        
        if kc.getKey("l"):
            anchor_positions = d.set_anchor_positions()
            distances_to_anchors = uwb.dis_to_anchors()
            backpoint = d.real_positions(distances_to_anchors, anchor_positions)
            print("set backpoint at", backpoint)
        if kc.getKey("u"):
            free_fly = False
            select_mode = True
            print("end free fly")
            print("you can select mode now")
    while back_to_backpoint:
            yaw = me.get_yaw() - initial_yaw
            control = d.Back_to_Backpoint(backpoint,yaw)
            # print("press u to quit back to backpoint")
            if control == 'stop' or kc.getKey('u'):
                print("end back to backpoint")
                print("you can select mode now")
                back_to_backpoint = False
                select_mode = True
                break
            me.send_rc_control(control[0],control[1],control[2],control[3])
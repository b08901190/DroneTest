import KeyboardControl as kc
import Distance as d
kc.init()
mode = "initial"
select_mode = True
free_fly = False
back_to_backpoint = False
test = True
backpoint = False
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
        kc.KeyboardControl()
        print("press u to quit free fly")
        if kc.getKey("l"):
            anchor_positions = anchor_positions
            distances_to_anchors = d.cal_dis_to_anchors()
            backpoint = d.real_positions(anchor_positions,distances_to_anchors)
            print("set backpoint at", backpoint)
        if kc.getKey("u"):
            free_fly = False
            select_mode = True
            print("end free fly")
            print("you can select mode now")
    while back_to_backpoint:
            d.Back_to_Backpoint(backpoint)
            print("press u to quit back to backpoint")
            if kc.getKey("u"):
                print("end back to backpoint")
                print("you can select mode now")
                back_to_backpoint = False
                select_mode = True
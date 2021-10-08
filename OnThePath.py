import time

def UnitVector(vector):
    [x,y,z] = vector
    Length = (x**2 + y**2 + z**2)**(0.5)
    unitvector = [x/Length , y/Length , z/Length]

    return  unitvector

def calculate_distance(target_position,real_position):
    distance = [target_position[0] - real_position[0],
                target_position[1] - real_position[1],
                target_position[2]- real_position[2]]
    return distance

def real_positions():
    #in practical , use UWB to calculate
    #for test , it need to return a different position every 0.1 second
    real_position = [0, target_positions()[1]-(target_positions()[1]%(0.1*speed)), 0]
    return real_position


def target_positions():
    # it could be change for different test project
    duration = time.time() - initial_time
    index = duration % 20
    if index >=10 :
        target_position = [0,(20-index)*speed,0]
    else :
        target_position = [0, (index) * speed, 0]
    return target_position
speed = 50
initial_time = time.time()

# FOR practical :
# me = tello.Tello()
# me.connect()
# print(me.get_battery())
# initial_yaw = me.get_yaw() #得到初始的方向
# me.takeoff()

while True :
    target_position =  target_positions()
    real_position = real_positions()
    # yaw = me.get_yaw()-initial_yaw #得到與一開始方向的差別（得到的值是度數）
    distance = calculate_distance(target_position,real_position)
    unit_distance = UnitVector(distance)
    rc_control = [int(speed*unit_distance[0]),int(speed*unit_distance[1]),int(speed*unit_distance[2]),0]
    # rc_control (left_right_velocity,forward_backward_velocity,up_down_velocity,yaw_velocity)
    # 定義forward 的方向是正y方向
    print(rc_control)

## another things need to work is that this code can work when the yaw did not change
## in practical , need to find a way to know its forward direction
## for while loop, rc_control need to change for different forward direction
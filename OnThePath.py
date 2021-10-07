def UnitVector(vector):
    [x,y,z] = vector
    Length = (x**2 + y**2 + z**2)**(0.5)
    unitvector = [x/Length , y/Length , z/Length]

    return  unitvector

def real_positions():
    #in practical , use UWB to calculate
    #for test , it need to return a different position every 0.1 second
    return real_position

def calculate_distance(target_position,real_position):
    distance = [target_position[0] - real_position[0],
                target_position[1] - real_position[1],
                target_position[2] - real_position[2]]
    return distance

while True :
    target_position =  #depend on the test
    real_position = real_positions()
    distance = calculate_distance(target_position,real_position)
    unit_distance = UnitVector(distance)
    rc_control = [int(speed*unit_distance[0]),int(speed*unit_distance[1]),int(speed*unit_distance[2]),0]
    # rc_control (left_right_velocity,forward_backward_velocity,up_down_velocity,yaw_velocity)
    # 定義forward 的方向是正y方向
    print(rc_contrl)

## another things need to work is that this code can work when the yaw did not change
## in practical , need to find a way to know its forward direction
## for while loop, rcc_control need to change for different forward direction

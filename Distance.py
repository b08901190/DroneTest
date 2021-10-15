import KeyboardControl as kc
import distance2location as d2l

def UnitVector(vector):
    [x,y,z] = vector
    Length = (x**2 + y**2 + z**2)**(0.5)
    if Length == 0 :
        unitvector = [0,0,0]
    else:
        unitvector = [x/Length , y/Length , z/Length]
    return  unitvector

def calculate_distance(target_position,real_position):
    distance = [target_position[0] - real_position[0],
                target_position[1] - real_position[1],
                target_position[2]- real_position[2]]
    return distance

def real_positions(anchor_positions,distances_to_anchors):
    # real_position = d2l.costfun_method(distances_to_anchors, anchor_positions)
    real_position = [1,1,1]
    return real_position


def Set_Backpoint():
    backpoint = False
    if kc.getKey("k"):
        backpoint = real_positions()
    return backpoint

def PID_speed(distance,pLength):
    P,I,D =  10,0,10
    [x,y,z] = distance
    Length = (x ** 2 + y ** 2 + z ** 2) ** (0.5)
    speed = Length*P + (Length-pLength)*D
    speed = int(speed)
    if speed > 100 :
        speed = 100
    elif speed < -100 :
        speed = -100
    return speed,Length

def cal_dis_to_anchors():
    return [0,0,0,0]

def Back_to_Backpoint(backpoint):
    pLength = 0
    if type(backpoint) != list :
        print("don't have backpoint yet")
    while True:
        anchor_positions = [0,0,0]*4
        distances_to_anchors = cal_dis_to_anchors()
        real_position = real_positions(anchor_positions,distances_to_anchors)
        distance = calculate_distance(backpoint, real_position)
        unit_distance = UnitVector(distance)
        speed,pLength = PID_speed(distance,pLength)
        lr, fb, ud, yv = [int(speed * unit_distance[0]), int(speed * unit_distance[1]), int(speed * unit_distance[2]),0]
        rc_control = [lr, fb, ud, yv]
        print(rc_control)
        if kc.getKey("u"):
            break


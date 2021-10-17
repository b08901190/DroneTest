import KeyboardControl as kc
import distance2location as d2l
import uwb_read as uwb
import math

def set_anchor_positions():
    anchor_positions = [ [0,0,86] , [4944,0,2101], [0,7208,1960], [4944,7065,0] ] 
    return anchor_positions

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

def real_positions(distances_to_anchors, anchor_positions):
    for i in distances_to_anchors:
        if i == 0:
            return 'error'
    real_position = d2l.costfun_method(distances_to_anchors, anchor_positions)
    return real_position

def changedr(vector, yaw):
    [x, y, z] = vector
    target_yaw = math.atan(x/y)
    target_yaw = target_yaw*180/math.pi
    if y < 0 :
        target_yaw += 180
    Length = (x**2 + y**2)**(0.5)
    arc = target_yaw - yaw
    rad = math.radians(arc)
    vector[0] = math.sin(rad)*Length
    vector[1] = math.cos(rad)*Length
    return vector

def PID_speed(distance,pLength):
    P,I,D =  0.05, 0, 0.02
    [x,y,z] = distance
    Length = (x ** 2 + y ** 2 + z ** 2) ** (0.5)
    print("L",Length)
    speed = Length*P + (Length-pLength)*D
    speed = int(speed)
    if speed > 100 :
        speed = 100
    elif speed < -100 :
        speed = -100
    return speed,Length

def Back_to_Backpoint(backpoint,yaw):
    if kc.getKey("u"):
        return 'stop'
    pLength = 0
    has_backpoint = True
    if backpoint == "nan":
        print("don't have backpoint yet")
        has_backpoint = False
    anchor_positions = set_anchor_positions()
    distances_to_anchors = uwb.dis_to_anchors()
    # print('dis',distances_to_anchors)
    if distances_to_anchors[0] == -1:
        print('[-1,-1,-1,-1]')
        rc_control = [0,0,0,0]
        return rc_control
    real_position = real_positions(distances_to_anchors, anchor_positions)
    if real_position != 'error':
        distance = calculate_distance(backpoint, real_position)
        print("d",distance)
        unit_distance = UnitVector(distance)
        unit_distance = changedr(unit_distance,yaw)
        speed,pLength = PID_speed(distance,pLength)
        lr, fb, ud, yv = [int(speed * unit_distance[0]), int(speed * unit_distance[1]), int(speed * unit_distance[2]),0]
        rc_control = [lr, fb, ud, yv]
    else:
        rc_control = [0,0,0,0]
    return rc_control

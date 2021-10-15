import KeyboardControl as kc

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

def real_positions():
    #in practical , use UWB to calculate
    #for test , it need to return a different position every 0.1 second
    real_position = [0,0,0]
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

def Back_to_Backpoint(backpoint):
    pLength = 0
    has_backpoint = True
    if backpoint == False :
        print("don't have backpoint yet")
        has_backpoint = False
    while has_backpoint == True:
        real_position = real_positions()
        distance = calculate_distance(backpoint, real_position)
        unit_distance = UnitVector(distance)
        speed,pLength = PID_speed(distance,pLength)
        lr, fb, ud, yv = [int(speed * unit_distance[0]), int(speed * unit_distance[1]), int(speed * unit_distance[2]),0]
        rc_control = [lr, fb, ud, yv]
        print(rc_control)
        if kc.getKey("u"):
            break


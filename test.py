import math


def UnitVector(vector):
    [x, y, z] = vector
    Length = (x**2 + y**2 + z**2)**(0.5)
    if Length == 0:
        unitvector = [0, 0, 0]
    else:
        unitvector = [x/Length, y/Length, z/Length]
    return unitvector


def changedr(vector, initial_yaw):
    [x, y, z] = vector
    target_yaw = math.atan(x/y)
    Length = (x**2 + y**2)**(0.5)
    arc = 100 - target_yaw
    rad = math.radians(arc)
    vector[0] = math.sin(rad)/Length
    vector[1] = math.cos(rad)/Length
    newl = (vector[0]**2 + vector[1]**2)**(0.5)
    vector[0] = vector[0]*Length/newl
    vector[1] = vector[1]*Length/newl
    return UnitVector(vector)


print(UnitVector([1, 2, 2]))
print(changedr(UnitVector([1, 2, 2]), 170))


print(UnitVector([1, 2, 2]), 150)
print(UnitVector([12, 2, 3]), 138)
print()

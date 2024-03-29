from djitellopy import tello
import time
import pygame
def init():
    pygame.init()
    win = pygame.display.set_mode((400,400))
def getKey(keyName):
    ans = False
    for eve in pygame.event.get():pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame,'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update
    return ans

def getKeyboardInput():
    global backpoint
    lr,fb,ud,yv = 0,0,0,0
    speed = 50

    if getKey("LEFT"): lr = -speed
    elif getKey("RIGHT"): lr = speed

    if getKey("UP"): fb = speed
    elif getKey("DOWN"): fb = -speed

    if getKey("w"): ud = speed
    elif getKey("s"): ud = -speed

    if getKey("a"): yv = -speed
    elif getKey("d"): yv = speed

    return [lr,fb,ud,yv]

def KeyboardControl():
    vals = getKeyboardInput()
    rc_control = [vals[0] , vals[1] , vals[2] , vals[3]] 
    print(vals)
    time.sleep(0.05)
    return rc_control






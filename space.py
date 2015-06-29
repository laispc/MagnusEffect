import random
from utils import *
from random import randrange

def setLights():
    glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 200, 100, 0.0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)           # most obj files expect to be smooth-shaded

MAX_METEOR_TRANSLATION_X = 100
LAST_METEOR_POSITION_TO_THROW_A_NEW_ONE = -150
METEOR_VANISH_Z = 50
METEOR_MAX_ROT_SPEED = 1
METEOR_SPEED = 0.5
METEOR_MODEL_LIST = ("model/Rock/Rock.obj", "model/Rock_1/Rock_1.obj", "model/Rock_2/Rock_2.obj", "model/Rock_3/Rock_3.obj")

def meteorLoad(meteorList):
    obj = OBJ(METEOR_MODEL_LIST[random.randrange(0,4)], swapyz=True)
    obj.r, obj.t = (0,0), (random.randrange(-MAX_METEOR_TRANSLATION_X, MAX_METEOR_TRANSLATION_X), Y_GAME_PLAN,-Z_FAR * 1.1)
    obj.rot_speed = (random.randrange(-METEOR_MAX_ROT_SPEED, METEOR_MAX_ROT_SPEED), random.randrange(-METEOR_MAX_ROT_SPEED, METEOR_MAX_ROT_SPEED))
    obj.safeX = 20
    obj.safeZ = 7
    obj.passed = False
    meteorList.append(obj)

def meteorDraw(meteorList):
    for meteor in meteorList:
        objDraw(meteor)

def meteorMove(meteor):
    for i in range(len(meteor)):
        meteor[i].t = (meteor[i].t[0], meteor[i].t[1], meteor[i].t[2]+METEOR_SPEED)
        meteor[i].r = (meteor[i].r[0]+meteor[i].rot_speed[0], meteor[i].r[1]+meteor[i].rot_speed[1])

    if meteor[-1].t[2] > LAST_METEOR_POSITION_TO_THROW_A_NEW_ONE:
        meteorLoad(meteor)
    if meteor[0].t[2] > METEOR_VANISH_Z:
        del meteor[0]
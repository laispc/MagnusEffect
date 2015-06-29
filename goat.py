# IMPORT OBJECT LOADER
from utils import *
import math

MAX_TRANS_X = 80
MAX_TRANS_Y = 80
MAX_TRANS_Z = 30
GOAT_X_ANGLE = 90
GOAT_Z_TRANS = -10

X_INITIAL = 0
Y_INITIAL = 0
GRAVITY = -1

X_VEL = 3
ROT_VEL = -4
OBJ_MASS = 1
OBJ_AREA = 1
FLUID_DENSITY = 0.1

def goatLoad():
    obj = OBJ("model/torus/Torus.obj", swapyz=True)
    obj.r, obj.t = (GOAT_X_ANGLE,0, 0), (X_INITIAL,Y_INITIAL,GOAT_Z_TRANS)
    obj.safeX = 20
    obj.safeZ = 2
    obj.velX = 0
    obj.velY = 20
    obj.velZ = X_VEL
    return obj

def goatDraw(obj):
	'''
    if obj.t[0] < -MAX_TRANS_X:
        obj.t = (-MAX_TRANS_X, obj.t[1], obj.t[2])
        return False
    if obj.t[0] > MAX_TRANS_X: 
        obj.t = (MAX_TRANS_X, obj.t[1], obj.t[2])
        return False
    if obj.t[1] < -MAX_TRANS_Y:
        obj.t = (obj.t[0], -MAX_TRANS_Y, obj.t[2])
        return False
    if obj.t[1] > MAX_TRANS_Y:
        obj.t = (obj.t[0], MAX_TRANS_Y, obj.t[2])
        return False
    if obj.t[2] < -MAX_TRANS_Z:
		obj.t = (obj.t[0], obj.t[1], -MAX_TRANS_Z)
		return False
    '''
	objDraw(obj)
    #return True

def objMove(obj):
	##calculate velocity vector
	sx = obj.velX
	sy = obj.velY
	sz = obj.velZ
	##velocity magnitude (raised to the power of 2)
	#s = sx*sx + sy*sy + sz*sz
	#support coefficient
	#coef = 0.1
	##magnus force (dividing by obj mass, we got acceleration)
	#acc_m = (0.5*FLUID_DENSITY*s*OBJ_AREA*coef)/OBJ_MASS
	##magnus force vector
	#acc_m_x = -acc_m*(sx/s)
	#acc_m_z = acc_m*(sx/s)
	##update obj velocity
	#obj.velX = sx + acc_m_x
	obj.velY = sy + GRAVITY
	#obj.velZ = sz + acc_m_z
	#print "velocity = ", obj.velX, " ", obj.velY, " ", obj.velZ
	##move
	obj.t = (obj.t[0] + obj.velX, obj.t[1] + obj.velY, obj.t[2] - obj.velZ)

def objMoveX(obj, tx):
	obj.t = (obj.t[0] + tx, obj.t[1], obj.t[2])

def objMoveY(obj, ty):
	obj.t = (obj.t[0], obj.t[1] + ty, obj.t[2])

def objMoveY(obj, tz):
	obj.t = (obj.t[0], obj.t[1], obj.t[2] + tz)

def objRotate(obj):
    obj.r = (obj.r[0], obj.r[1], obj.r[2] + ROT_VEL)



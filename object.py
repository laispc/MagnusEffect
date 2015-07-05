# IMPORT OBJECT LOADER
from utils import *
import math

#Static params
MAX_TRANS_X = 80
MAX_TRANS_Y = 50
MAX_TRANS_Z = 30

GOAT_Z_TRANS = -5
GOAT_X_ANGLE = 90

X_INITIAL = 0
Y_INITIAL = 30
GRAVITY = -0.2
OBJ_AREA = 0.2
FLUID_DENSITY = 0.1

#Initial params
X_VEL = 0
Y_VEL = 0.1
Z_VEL = 0.1
ROT_VEL = 0
OBJ_MASS = 1
WIND = 0

def objRestart(obj):
	obj.r, obj.t = (GOAT_X_ANGLE,0, 0), (X_INITIAL,Y_INITIAL,GOAT_Z_TRANS)
	obj.velY = obj.velY_initial 
	obj.velZ = obj.velZ_initial
	obj.rotY = obj.rotY_initial
	obj.mass = obj.mass_initial
	obj.wind = obj.wind_initial

def objLoadParams(obj):
    obj.r, obj.t = (GOAT_X_ANGLE,0, 0), (X_INITIAL,Y_INITIAL,GOAT_Z_TRANS)
    
    obj.velX = X_VEL
    
    obj.velY_initial = Y_VEL
    obj.velZ_initial = Z_VEL
    obj.rotY_initial = ROT_VEL
    obj.mass_initial = OBJ_MASS
    obj.wind_initial = WIND

    obj.velY = Y_VEL
    obj.velZ = Z_VEL
    obj.rotY = ROT_VEL
    obj.mass = OBJ_MASS
    obj.wind = WIND

def objLoad():
    obj = OBJ("model/torus/Torus.obj", swapyz=True)
    objLoadParams(obj)
    return obj

def objDrawOnScreen(obj):
	if obj.t[1] < -MAX_TRANS_Y:
		obj.t = (obj.t[0], -MAX_TRANS_Y, obj.t[2])
		obj.velX = 0
		obj.velY = 0
		obj.velZ = 0
	objDraw(obj)
	#return True

def objMove(obj):
	##calculate velocity vector
	sx = obj.velX
	sy = obj.velY
	sz = obj.velZ
	##velocity magnitude (raised to the power of 2)
	s = sx*sx + sy*sy + sz*sz
	if s==0:
		return
	#support coefficient
	rot = obj.rotY;
	coef = 1*rot;
	##magnus force (dividing by obj mass, we got acceleration)
	acc_m = (1.0*FLUID_DENSITY*s*OBJ_AREA*coef)/1.0*OBJ_MASS
	##magnus force vector
	acc_m_x = (0.5*sz/s)*acc_m
	acc_m_z = (-1.0*sx/s)*acc_m
	print "sx,sz = ", sx, " ", sz;
	print "s = ", s;
	print "ACC = ", acc_m;
	print "ACCS = ", acc_m_x, acc_m_z;
	##update obj velocity
	obj.velX = sx + acc_m_x
	obj.velY = sy + GRAVITY
	obj.velZ = sz + acc_m_z + obj.wind
	obj.velX = 1.15 * obj.velX	#Improve visual effect on x
	print "velocity = ", obj.velX, " ", obj.velY, " ", obj.velZ
	##move
	obj.t = (obj.t[0] + obj.velX, obj.t[1] + obj.velY, obj.t[2] - obj.velZ)

def objMoveX(obj, tx):
	obj.t = (obj.t[0] + tx, obj.t[1], obj.t[2])

def objMoveY(obj, ty):
	obj.t = (obj.t[0], obj.t[1] + ty, obj.t[2])

def objMoveY(obj, tz):
	obj.t = (obj.t[0], obj.t[1], obj.t[2] + tz)

def objRotate(obj):
    obj.r = (obj.r[0], obj.r[1], obj.r[2] + obj.rotY)

#Velocity control
def increaseVelocity(obj):
	obj.velZ_initial = obj.velZ_initial + 0.1
	if obj.velZ_initial >= 2:
		obj.velZ_initial = 0.1

def getVelocity(obj):
	return obj.velZ_initial

#Rotation control
def increaseRotation(obj):
	if obj.rotY_initial == -0.1:
		print "entrou"
		obj.rotY_initial = 0.0
	else: 
		obj.rotY_initial = obj.rotY_initial + 0.1
	if obj.rotY_initial > 2.5:
		obj.rotY_initial = -2.5

def getRotation(obj):
	return obj.rotY_initial

#Mass control
def increaseMass(obj):
	obj.mass_initial = obj.mass_initial + 0.1
	if obj.mass_initial > 5:
		obj.mass_initial = 1

def getMass(obj):
	return obj.mass_initial

#Wind control
def increaseWind(obj):
	if obj.wind_initial == -0.1:
		obj.rotY_initial = 0.0
	obj.wind_initial = obj.wind_initial + 0.1
	if obj.wind_initial > 0.5:
		obj.wind_initial = -0.5

def getWind(obj):
	return obj.wind_initial

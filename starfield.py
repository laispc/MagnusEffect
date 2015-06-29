from random import randrange
from math import cos, sin, fabs
from utils import *
 
STAR_SPEED = 2
LAST_STAR_SPEED_TO_THROW_A_NEW_ONE = 15
STAR_VANISH_SPEED = 100

def starDraw(stars):
    for star in stars:
        objDraw(star, 0.05)

def starInit(stars):
    star = OBJ("model/star/star.obj", swapyz=True)
    star.dir = randrange(0, 360)
    star.speed = float(randrange(5, 10)) / 20
    init = randrange(0, 10)
    star.r, star.t = (0,0), (init * star.speed * cos(star.dir),init * star.speed * sin(star.dir),-200)
    stars.append(star)

def starMove(stars):
    for star in stars:
        star.t = (star.t[0] + star.speed * cos(star.dir), star.t[1] + star.speed * sin(star.dir), star.t[2])

    if (fabs(stars[-1].t[0]) > 1) or (fabs(stars[-1].t[1]) > 1):
        starInit(stars)
    if (fabs(stars[0].t[0]) > 55) or (fabs(stars[0].t[1]) > 55):
        del stars[0]
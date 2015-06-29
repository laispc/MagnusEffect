from OpenGL.GLE.exceptional import _lengthOfArgname

__author__ = 'rvferreira e laispc'

import sys

from OpenGL.GLU import *
from pygame.locals import *

from space import setLights, meteorLoad, meteorDraw, meteorMove
from goat import goatLoad, goatDraw
from starfield import *
from goat import goatLoad, goatDraw, objMoveX, objMoveY, objRotate, objMove 
from utils import Z_FAR, Z_NEAR, WINDOW_HEIGHT, WINDOW_WIDTH, load_sound

DEATH_TIMER = 200

def main():

    #pygame.mixer.init()
    #pygame.mixer.music.load('focus.mp3')
    #pygame.mixer.music.play(-1)
    #effect = load_sound('goat_yell.wav')
    #effect.play()

    size = width, height = WINDOW_WIDTH, WINDOW_HEIGHT

    screen = pygame.display.set_mode(size, OPENGL|DOUBLEBUF)
    pygame.display.set_caption("SpaceGoat")
    setLights()

    pygame.init()

    font = pygame.font.Font(None, 20)
    textSurface = font.render("SpaceGoat", True, (255,255,255,255), (0,0,0,255))
    textData = pygame.image.tostring(textSurface, "RGBA", True)
    glRasterPos3d(0,0,5)
    glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, width/float(height), Z_NEAR, Z_FAR)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_MODELVIEW)

    fps = 60
    dt = 1.0/fps
    clock = pygame.time.Clock()

    goat = goatLoad()
    move = False

    x = 100
    y = 500
    keepDrawing = True
    print " ", keepDrawing

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    if event.key == pygame.K_LEFT: pass
                    else: pass
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: pass

        if move:
            goatMove(goat, dir)

        #objMoveX(goat)
        #objMoveY(goat)
        objMove(goat)
        objRotate(goat)
        #goat.t = (goat.t[0], goat.t[1], goat.t[2]-1) 
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
   
        
        keepDrawing = goatDraw(goat)
        print " ", keepDrawing
        pygame.display.flip()

if __name__ == '__main__': main()

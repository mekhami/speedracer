import pygame as pg
import sys

pg.init()

size = width, height = 500, 500
screen = pg.display.set_mode(size)

white = 255, 255, 255
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
        
        screen.fill(white)
        pg.display.flip()

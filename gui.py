import pygame as pg
import sys

from shapes import outside_points, inside_points

pg.init()

size = width, height = 500, 500
screen = pg.display.set_mode(size)

white = 255, 255, 255
black = 0, 0, 0

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
        
        screen.fill(white)
        pg.draw.polygon(screen, black, inside_points, 2)
        pg.draw.polygon(screen, black, outside_points, 2)
        pg.draw.rect(screen, black, pg.Rect(150, 320, 15, 8))
        pg.display.flip()

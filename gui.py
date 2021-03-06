import pygame as pg
import sys

from shapes import outside_points, inside_points

pg.init()

size = width, height = 500, 500
screen = pg.display.set_mode(size)
clock = pg.time.Clock()

white = 255, 255, 255
black = 0, 0, 0

rotational_degree = 0

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()

    screen.fill(white)

    pg.draw.polygon(screen, black, inside_points, 2)
    pg.draw.polygon(screen, black, outside_points, 2)

    car = pg.Surface((15, 8))
    car.fill(black)
    pg.draw.rect(car, black, pg.Rect(0, 0, 15, 8), 1)
    car.set_colorkey(white)
    car = pg.transform.rotate(car, 90)
    screen.blit(car, (150, 320, 15, 8))
    pg.display.flip()

import pygame as pg
import math
import random
pg.init()
screen = pg.display.set_mode((1024,768))
pg.display.set_caption("My First Python Game")
back = pg.image.load(r"background.jpg").convert_alpha()
bomb = pg.image.load(r"bomb.png").convert_alpha()
player = pg.image.load(r"spaceship.png").convert_alpha()
enemy = pg.image.load(r"ufo.png").convert_alpha()
bullet = pg.image.load(r"bullet.png").convert_alpha()
fire = pg.image.load(r"flame.png").convert_alpha()
run=True
bx=0
by=0
px=512
py=700
ex=random.randint(5,968)
ey=68
pi=0
speed = 1
ei=speed
bullet_state = "ready"
def has_collided(x1,x2,y1,y2):
    d= math.sqrt((x2-x1)**2 + (y2-y1)**2)
    if d<=50:
        return True
    else:
        return False
    
while run:
    bomb = pg.transform.scale(bomb,(50,50))
    bullet = pg.transform.scale(bullet,(20,20))
    fire = pg.transform.scale(fire,(50,50))
    player = pg.transform.smoothscale(player,(50,50))
    enemy = pg.transform.scale(enemy,(50,50))
    screen.blit(back,(0,0))
    screen.blit(player,(px,py))
    screen.blit(enemy,(ex,ey))
    events = pg.event.get()
    for e in events:
        if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
            run=False
        if e.type == pg.MOUSEBUTTONDOWN and bullet_state == "ready":
            bullet_state = "fire"
            bx=px
            by=py
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_d:
                pi=speed
            elif e.key == pg.K_a:
                pi=-speed
        if e.type == pg.KEYUP:
            pi=0
    if bullet_state == "fire":
        screen.blit(bullet,(bx,by))
    if by < 0:
        bullet_state = "ready"
    if ex>968:
        ex=968
        ey+=20
        ei=-speed
    if ex<5:
        ex=5
        ey+=20
        ei=speed
    ex+=ei
    if px>968:
        px=968
    if px<5:
        px=5
    px+=pi
    by-=2
    if has_collided(bx,ex,by,ey):
        screen.blit(fire,(ex,ey))
        bullet_state = "ready"
        ex=random.randint(5,968)
        ey=68
    pg.display.update()
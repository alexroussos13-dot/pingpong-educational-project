import pygame as pg
from pingpong_lib import *

def play():
    game_over = False

    pg.font.init()

    background = pg.transform.scale(pg.image.load("background.jpg"), (700, 500))
    window = pg.display.set_mode((700, 500))

    player1 = Player("paddle.png", 5, 10, 200, pg.K_w, pg.K_s)
    player2 = Player("paddle.png", 5, 660, 200, pg.K_UP, pg.K_DOWN)

    game = True
    clock = pg.time.Clock()
    FPS = 60
    while game:
        window.blit(background, (0, 0))

        player1.reset(window)
        player1.events()

        player2.reset(window)
        player2.events()

        events = pg.event.get()
        for e in events:
            if e.type == pg.QUIT:
                return False
        
        pg.display.update()
        clock.tick(FPS)


while play():
    pass

pg.quit()
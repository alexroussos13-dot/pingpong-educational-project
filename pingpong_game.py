import pygame as pg

def play():
    game_over = False

    pg.font.init()

    background = pg.transform.scale(pg.image.load("background.jpg"), (700, 500))
    window = pg.display.set_mode((700, 500))

    game = True
    clock = pg.time.Clock()
    FPS = 60
    while game:
        window.blit(background, (0, 0))


        events = pg.event.get()
        for e in events:
            if e.type == pg.QUIT:
                return False
        
        pg.display.update()
        clock.tick(FPS)


while play():
    pass

pg.quit()
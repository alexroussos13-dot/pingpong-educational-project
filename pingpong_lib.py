import pygame as pg
from random import randint

passed = 0
kills = 0
game_over = False 
rel_time = False
fired = 0
reload_timer = 0 

class GameSprite(pg.sprite.Sprite):
    def __init__(self, img, sp, x, y):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(img), (100, 100))
        self.speed = sp
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.float_x = float(x)  # track real position
        self.float_y = float(y)
    def reset(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, img, sp, x, y, up, down):
        super().__init__(img, sp, x, y)
        self.image = pg.transform.scale(pg.image.load(img), (32, 90))
        self.up_key = up
        self.down_key = down

    def events(self):
        keys_pressed = pg.key.get_pressed()
        """if keys_pressed[pg.K_LEFT] and self.float_x > 5:
                                    self.float_x -= self.speed
                                if keys_pressed[pg.K_RIGHT] and self.float_x < 600:
                                    self.float_x += self.speed
                                self.rect.x = int(self.float_x)  # sync to rect for drawing/collision
                                self.rect.y = int(self.float_y)"""
        if keys_pressed[self.up_key] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[self.down_key] and self.rect.y < 405:
            self.rect.y += self.speed

    
def display_loss():
        font = pg.font.SysFont('Arial', 100)
        red = (255, 0, 0)
        text = font.render('lost', True, red, None)
        textRect = text.get_rect()
        textRect.x = 250
        textRect.y = 350
        window.blit(text, textRect)

def display_win():
        font = pg.font.SysFont('Arial', 100)
        green = (0, 255, 0)
        text = font.render('win', True, green, None)
        textRect = text.get_rect()
        textRect.x = 250
        textRect.y = 350
        window.blit(text, textRect)


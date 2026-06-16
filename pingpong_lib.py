import pygame as pg
from random import randint

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
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
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

class Ball(GameSprite):
    def __init__(self, img, sp, x, y, p1, p2):
        super().__init__(img, sp, x, y)
        self.image = pg.transform.scale(pg.image.load(img), (30, 30))
        self.p1 = p1
        self.p2 = p2
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.y_speed = sp

    def update(self, window):
        self.rect.x += self.speed
        if pg.sprite.collide_rect(self, self.p1):
            self.speed = self.speed * -1
        if pg.sprite.collide_rect(self, self.p2):
            self.speed = self.speed * -1

        self.rect.y += self.y_speed
        if self.rect.y <= 0:
            self.y_speed *= -1
        if self.rect.y >= 480:
            self.y_speed *= -1


        if self.rect.x >= 680:
            display_loss(window, "player1")
            pg.display.update()
            pg.time.wait(2000)
            self.rect.x = 350
            self.rect.y = 250 
            self.y_speed *= -1
            return True

        if self.rect.x <= 0:      
            display_loss(window, "player2")
            pg.display.update()
            pg.time.wait(2000)
            self.rect.x = 350
            self.rect.y = 250
            self.y_speed *= -1
            return True



def display_loss(window, player):
        font = pg.font.SysFont('Arial', 100)
        red = (0, 255, 0)
        t = str(player) + " won"
        text = font.render(t, True, red, None)
        textRect = text.get_rect()
        textRect.x = 250
        textRect.y = 350
        window.blit(text, textRect)

def display_win(window):
        font = pg.font.SysFont('Arial', 100)
        green = (0, 255, 0)
        text = font.render('win', True, green, None)
        textRect = text.get_rect()
        textRect.x = 250
        textRect.y = 350
        window.blit(text, textRect)



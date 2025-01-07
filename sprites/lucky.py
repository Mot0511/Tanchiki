import random

import pygame as pg

from utils.load_image import load_image


class Lucky(pg.sprite.Sprite):
    def __init__(self, all, width, height):
        super().__init__(all)
        self.all = all
        self.image = pg.transform.scale(load_image('lucky.jpg'), (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width - 30)
        self.rect.y = random.randrange(width - height)

        sprites = pg.sprite.spritecollide(self, all, False)
        sprites.remove(self)
        if sprites:
            self.kill()
            self.__init__(all, width, height)

    def update(self):
        sprites = pg.sprite.spritecollide(self, self.all, False)
        sprites.remove(self)
        if sprites:
            tank = sprites[0]
            self.kill()

            high_bonus = random.randrange(1, 10)
            if 1 == high_bonus:
                tank.dead()
                return

            elif 2 == high_bonus:
                tank.enemy.dead()
                return

            else:
                low_bonus = random.randrange(0, 3)
                if 0 == low_bonus:
                    tank.v += 0.2
                    tank.image = pg.transform.scale(tank.image, (tank.rect.width - 3, tank.rect.height - 3))
                    tank.base_image = pg.transform.scale(tank.base_image, (tank.rect.width - 3, tank.rect.height - 3))
                    x = tank.rect.x
                    y = tank.rect.y
                    tank.rect = tank.image.get_rect()
                    tank.rect.x = x
                    tank.rect.y = y
                    return

                elif 1 == low_bonus:
                    tank.bullet_v += 2
                    return
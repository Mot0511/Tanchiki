import pygame as pg

from utils.load_image import load_image


class Wall(pg.sprite.Sprite):
    def __init__(self, all, solids, pos, size):
        super().__init__(all)
        self.add(solids)
        self.image = pg.Surface(size)
        self.image.fill((112, 112, 112))
        self.image = pg.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
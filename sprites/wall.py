import pygame as pg

from utils.load_image import load_image


class Wall(pg.sprite.Sprite):
    def __init__(self, all, solids, pos, size):
        super().__init__(all)
        self.add(solids)
        self.image = load_image('wall.png')
        self.image = pg.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        # self.rect = pg.Rect((pos[0], pos[1], size[0], size[1]))
        # pg.draw.rect(self.image, pg.Color('red'), pg.Rect(pos, size))
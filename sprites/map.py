import pygame as pg

from utils.load_image import load_image


class Map(pg.sprite.Sprite):
    def __init__(self, all, solids):
        super().__init__(all)
        self.image = load_image('map/map1.png')
        self.mask = pg.sprite.Mask(self.image)
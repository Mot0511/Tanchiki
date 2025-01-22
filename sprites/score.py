import pygame as pg

from utils.load_image import load_image


class Score(pg.sprite.Sprite):
    def __init__(self, all, pos, player, value):
        super().__init__(all)
        self.value = value
        self.rect = pg.Rect(pos, (120, 30))
        self.player = player
        self.font = pg.font.Font(None, 50)
        self.icon = pg.transform.scale(load_image(f'tank{self.player}.png'), (30, 30))


    def update(self):
        self.image = pg.Surface((120, 30), pg.SRCALPHA)

        pg.font.init()
        text = self.font.render(str(self.value), True, (255, 255, 255))
        self.image.blit(text, (0, 0))

        self.image.blit(self.icon, (80, 0))
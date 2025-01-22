import pygame as pg


class Text(pg.sprite.Sprite):
    def __init__(self, all, text, size, width, pos, color):
        super().__init__(all)
        self.width = width
        self.size = size
        self.image = pg.Surface((width, size), pg.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.color = color

        self.font = pg.font.Font(None, size)
        text = self.font.render(text, True, color)
        self.image.blit(text, (0, 0))

    def setValue(self, value):
        self.image = pg.Surface((self.width, self.size), pg.SRCALPHA)
        text = self.font.render(value, True, self.color)
        self.image.blit(text, (0, 0))
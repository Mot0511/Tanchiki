import pygame as pg


class Text(pg.sprite.Sprite):
    def __init__(self, all, text, size, width, pos):
        super().__init__(all)
        self.image = pg.Surface((width, size), pg.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = pos

        font = pg.font.Font(None, size)
        text = font.render(text, True, (255, 255, 255))
        self.image.blit(text, (0, 0))
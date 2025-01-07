import pygame as pg


class Button(pg.sprite.Sprite):
    def __init__(self, all, text, pos, width, height, color):
        super().__init__(all)
        self.text = text
        self.image = pg.Surface((width, height), pg.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        pg.draw.rect(self.image, color, pg.Rect(0, 0, width, height), 0, 5)

        font = pg.font.Font(None, 45)
        text = font.render(text, True, pg.Color("white"))
        self.image.blit(text, (10, 10))
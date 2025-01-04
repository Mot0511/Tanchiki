import pygame as pg

from sprites.button import Button
from sprites.text import Text


class StartScreen:
    def __init__(self, width, height):

        self.bg = pg.Color('black')
        self.all = pg.sprite.Group()

        Text(self.all, 'Tanchiki', 100, 300, (width // 2, 200))
        play_btn = Button(self.all, 'Играть', ((width - 300) // 2, 300), 300, 50, pg.Color('darkgreen'))
        exit_btn = Button(self.all,'Выйти из игры', ((width - 300) // 2, 360), 300, 50, pg.Color('darkred'))

        self.btns = [play_btn, exit_btn]
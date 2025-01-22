import pygame as pg

from sprites.button import Button
from sprites.text import Text
from utils.load_image import load_image
import os


class StartScreen:
    def __init__(self, width, height):

        self.bg = load_image('main_menu_bg.jpg')
        self.bg = pg.transform.scale(self.bg, (width, height))
        self.all = pg.sprite.Group()

        Text(self.all, 'Танчики', 100, 300, (width // 2, 200), pg.Color('black'))
        

        play_btn = Button(self.all, 'Новая игра', ((width - 300) // 2, 360), 300, 50, pg.Color('darkgreen'))
        exit_btn = Button(self.all,'Выйти из игры', ((width - 300) // 2, 420), 300, 50, pg.Color('darkred'))

        self.btns = [play_btn, exit_btn]

        if os.path.exists('save.json'):
            continue_btn = Button(self.all, 'Продолжить игру', ((width - 300) // 2, 300), 300, 50, pg.Color('blue'))
            self.btns.append(continue_btn)
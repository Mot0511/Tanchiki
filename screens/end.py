import pygame as pg

from sprites.button import Button
from sprites.text import Text
from utils.load_image import load_image


class End:
    def __init__(self, width, height):
        self.bg = pg.Surface((width, height))
        self.bg.fill((0, 0, 0))
        self.all = pg.sprite.Group()
        self.width = width


        play_btn = Button(self.all, 'Играть снова', ((width - 300) // 2, 300), 300, 50, pg.Color('darkgreen'))
        exit_btn = Button(self.all,'Выйти из игры', ((width - 300) // 2, 360), 300, 50, pg.Color('darkred'))

        self.btns = [play_btn, exit_btn]

    def setWinner(self, player):
        if hasattr(self, 'text'): self.text.kill()
        match player:
            case 0:
                self.text = Text(self.all, 'Победила дружба!', 60, 400, (self.width // 2, 200), pg.Color('white'))
                return

            case 1:
                self.text = Text(self.all, 'Выиграл синий танк', 60, 420, (self.width // 2, 200), pg.Color('lightblue'))
                return

            case 2:
                self.text = Text(self.all, 'Выиграл красный танк', 60, 470, (self.width // 2, 200), pg.Color('red'))
                return
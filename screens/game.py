import pygame as pg
from sprites.borders import Border
from sprites.lucky import Lucky
from sprites.score import Score
from sprites.tank import Tank
from utils.initMap import initMap
from utils.load_image import load_image
from sprites.timer import Timer

class Game:
    def __init__(self, width, height):
        self.bg = pg.Surface((width, height))
        self.bg.fill(pg.Color('darkgreen'))
        self.all = pg.sprite.Group()
        solids = pg.sprite.Group()

        initMap(self.all, solids, width, height)

        self.score1 = Score(self.all, (width - 250, 10), 1)
        self.score2 = Score(self.all, (width - 120, 10), 2)

        self.tank1 = Tank(self.all, solids, 1, (10, 10), self.score1)
        self.tank2 = Tank(self.all, solids, 2, (width - 110, height - 90), self.score2)

        self.tank1.enemy = self.tank2
        self.tank2.enemy = self.tank1

        Border(self.all, solids, 0, 0, width, 0)
        Border(self.all, solids, 0, height - 0, width, height)
        Border(self.all, solids, 0, 0, 0, height) 
        Border(self.all, solids, width, 0, width, height)

        self.timer = Timer(self.all, width, 300)

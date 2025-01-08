import pygame as pg
from random import randrange
from sprites.borders import Border
from sprites.lucky import Lucky
from sprites.score import Score
from sprites.tank import Tank
from maps.map1 import map1
from maps.map2 import map2
from maps.map3 import map3
from maps.map4 import map4
from sprites.timer import Timer

class Game:
    def __init__(self, width, height):
        self.bg = pg.Surface((width, height))
        self.all = pg.sprite.Group()
        solids = pg.sprite.Group()

        maps = [
            map1,
            map2,
            map3,
            map4,
        ]

        bg_color = maps[randrange(len(maps))](self.all, solids, width, height)
        # bg_color = maps[3](self.all, solids, width, height)
        self.bg.fill(bg_color)

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
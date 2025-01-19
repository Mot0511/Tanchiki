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
import os
import json

class Game:
    def __init__(self, width, height):
        self.bg = pg.Surface((width, height))
        self.all = pg.sprite.Group()
        solids = pg.sprite.Group()

        if os.path.exists('save.json'):
            with open('save.json', 'r') as f:
                data = json.load(f)
        else:
            data = {}


        maps = [
            map1,
            map2,
            map3,
            map4,
        ]

        self.map_number = randrange(len(maps)) if not data else data['map']

        bg_color = maps[self.map_number](self.all, solids, width, height)
        # bg_color = maps[3](self.all, solids, width, height)
        self.bg.fill(bg_color)


        self.score1 = Score(self.all, (width - 250, 10), 1, data['tank1']['score'] if data else 0)
        self.score2 = Score(self.all, (width - 120, 10), 2, data['tank2']['score'] if data else 0)

        self.tank1 = Tank(self.all, solids, 1, (data['tank1']['x'], data['tank1']['y']) if data else (10, 10), 
                          (10, 10),
                          self.score1,
                          (data['tank1']['width'], data['tank1']['height']) if data else (70, 80),
                          data['tank1']['v'] if data else 5,
                          data['tank1']['bullet_v'] if data else 10)
        self.tank2 = Tank(self.all, solids, 2, (data['tank2']['x'], data['tank2']['y']) if data else (width - 110, height - 90), 
                          (width - 110, height - 90),
                          self.score2,
                          (data['tank2']['width'], data['tank2']['height']) if data else (70, 80),
                          data['tank2']['v'] if data else 5,
                          data['tank2']['bullet_v'] if data else 10)

        self.tank1.enemy = self.tank2
        self.tank2.enemy = self.tank1

        Border(self.all, solids, 0, 0, width, 0)
        Border(self.all, solids, 0, height - 0, width, height)
        Border(self.all, solids, 0, 0, 0, height) 
        Border(self.all, solids, width, 0, width, height)

        self.timer = Timer(self.all, width, 300 if not data else data['seconds'])
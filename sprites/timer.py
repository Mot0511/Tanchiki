import pygame as pg
from sprites.text import Text

class Timer:
    def __init__(self, all, width, init_value):
        self.value = int(init_value)
        self.running = True
        self.text = Text(all, str(f'{self.value // 60}:{self.value % 60}'), 50, 100, (width // 2, 30), pg.Color('white'))

    def decrement(self):
        if self.running:
            self.value -= 1
            self.text.setValue(str(f'{self.value // 60}:{self.value % 60}'))

        if self.value == 0:
            self.running = False
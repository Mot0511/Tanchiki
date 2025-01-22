import pygame as pg
from os import path


def load_sound(filename):
    sound = pg.mixer.Sound(path.join('assets', 'sounds', filename))
    return sound
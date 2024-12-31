import pygame as pg

from sprites.bullet import Bullet
from utils.load_image import load_image
from enums import Directions

class Tank(pg.sprite.Sprite):
    def __init__(self, all, solids, player, position):
        super().__init__(all)
        self.all = all
        self.solids = solids
        self.add(solids)
        self.player = player
        self.spawn_point = position
        self.base_image = load_image('tank_blue.png') if player == 1 else load_image('tank_red.png')
        self.base_image = pg.transform.scale(self.base_image, (90, 100))
        self.image = self.base_image
        self.image = pg.transform.rotate(self.base_image, 180)
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.v = 5
        self.vx = 0
        self.vy = 0
        self.bullet_v = 10
        self.direction = Directions.TOP

    def shoot(self):
        match self.direction:
            case Directions.TOP:
                Bullet(self.all, self.rect.center, 0, -self.bullet_v, -90, self)
            case Directions.LEFT:
                Bullet(self.all, self.rect.center, -self.bullet_v, 0, 0, self)
            case Directions.BOTTOM:
                Bullet(self.all, self.rect.center, 0, self.bullet_v, 90, self)
            case Directions.RIGHT:
                Bullet(self.all, self.rect.center, self.bullet_v, 0, 180, self)


    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        sprites = pg.sprite.spritecollide(self, self.solids, False)
        sprites.remove(self)
        if sprites:
            match self.direction:
                case Directions.TOP:
                    self.rect = self.rect.move(0, -self.vy)
                case Directions.LEFT:
                    self.rect = self.rect.move(-self.vx, 0)
                case Directions.RIGHT:
                    self.rect = self.rect.move(-self.vx, 0)
                case Directions.BOTTOM:
                    self.rect = self.rect.move(0, -self.vy)


    def set_direction(self, direction):
        match direction:
            case Directions.TOP:
                self.vx = 0
                self.vy = -self.v
                self.image = pg.transform.rotate(self.base_image, 180)
                self.direction = direction

            case Directions.BOTTOM:
                self.vx = 0
                self.vy = self.v
                self.image = pg.transform.rotate(self.base_image, 0)
                self.direction = direction
            case Directions.LEFT:
                self.vx = -self.v
                self.vy = 0
                self.image = pg.transform.rotate(self.base_image, -90)
                self.direction = direction
            case Directions.RIGHT:
                self.vx = self.v
                self.vy = 0
                self.image = pg.transform.rotate(self.base_image, 90)
                self.direction = direction

            case Directions.STOP:
                self.vx = 0
                self.vy = 0
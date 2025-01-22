import pygame as pg

from utils.load_sound import load_sound
from utils.load_image import load_image

class Bullet(pg.sprite.Sprite):
    def __init__(self, all, position, vx, vy, rotate, player):
        print(position)
        super().__init__(all)
        self.all = all
        self.player = player
        self.image = pg.transform.scale(load_image('bullet.png'), (20, 5))
        self.image = pg.transform.rotate(self.image, rotate)
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.vx = vx
        self.vy = vy

        self.shoot_on_wall_sound = load_sound('shoot_on_wall.mp3')

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        enemies = pg.sprite.spritecollide(self, self.all, False)
        if self.player in enemies: enemies.remove(self.player)
        if len(enemies) > 1:
            for enemy in enemies:
                if enemy == self:
                    enemy.kill()
                elif type(enemy).__name__ == 'Tank':
                    enemy.dead()
                else:
                    self.shoot_on_wall_sound.play()
from utils.load_image import load_image
import pygame as pg

class Explosion(pg.sprite.Sprite):
    def __init__(self, all, x, y, tank):
        super().__init__(all)
        self.frames = []
        self.cut_sheet(load_image('explosion.png'), 8, 3)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.tank = tank

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pg.Rect(0, 0, sheet.get_width() // columns, sheet.get_height() // rows)
        
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pg.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        # self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        print(self.cur_frame)
        print(len(self.frames))
        if self.cur_frame >= len(self.frames) - 4:
            self.tank.rect.topleft = self.tank.spawn_point
            self.kill()
            return

        self.image = self.frames[self.cur_frame]
        self.cur_frame += 1
from sprites.wall import Wall

def initMap(all, solids, width, height):
    Wall(all, solids, (100, 0), (30, 150))
    Wall(all, solids, (100, 150), (300, 30))
    Wall(all, solids, (0, 280), (300, 30))
    Wall(all, solids, (0, 410), (300, 30))
    Wall(all, solids, (270, 540), (30, 150))
    Wall(all, solids, (400, 150), (30, 100))
    Wall(all, solids, (400, 350), (30, 150))
    Wall(all, solids, (550, 500), (30, 150))
    Wall(all, solids, (550, 500), (30, 150))
    Wall(all, solids, (600, 250), (30, 100))
    Wall(all, solids, (width - 200, height - 130), (200, 30))
    Wall(all, solids, (750, 500), (30, 150))
    Wall(all, solids, (800, 350), (200, 30))
    Wall(all, solids, (width - 200, 200), (200, 30))
    Wall(all, solids, (width - 200, 100), (30, 100))
    Wall(all, solids, (580, 120), (200, 30))

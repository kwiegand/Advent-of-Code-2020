class Map2D:
    def __init__(self, map, startx=0, starty=0):
        self.map = map
        self.pos = [startx, starty]

    def move(self, x,y):
        self.pos[0] += x
        self.pos[1] += y

    



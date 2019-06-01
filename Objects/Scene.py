from Objects.Fenetre import *

WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)
BLUE = (0,0,255)

class Scene(Fenetre):

    def __init__(self, mySurface, title, Player):
        Fenetre.__init__(self, mySurface, title, Player)

    def draw(self):
        pass

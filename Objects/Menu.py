from Objects.Fenetre import *

WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)
BLUE = (0,0,255)

class Menu(Fenetre):

    def __init__(self, mySurface, title, Player):
        Fenetre.__init__(self, mySurface, title)
        self.Player = Player

    """
        Cette method permet de gerer la transition
        entre le Menu et Le jeux
    """
    def controller(self):
        pass

    """
        run menu
    """
    def started():
        pass

    """
        run game
    """
    def game(self, size):
        # Constant
        x, y = self.mySurface

        ## User entry
        x_col,y_line = size

        # Element of compare min and max
        horizontal, vertical = 0,0
        translate_h, translate_v = x/x_col, y/y_line

        # Boolean
        tracer = True
        tracer_line = True

        while tracer:
            self.pygame.draw.line(self.screen, BLACK, (horizontal, 0), (horizontal,y), 5)
            horizontal+= translate_h
            if horizontal > x:
                tracer = False

        while tracer_line:
            self.pygame.draw.line(self.screen, BLACK, (0, vertical), (x,vertical), 5)
            vertical+= translate_v
            if vertical > y:
                tracer_line = False

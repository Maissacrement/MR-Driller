from Objects.Fenetre import *

WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)
BLUE = (0,0,255)

class Menu(Fenetre):

    def __init__(self, mySurface, title, Player):
        Fenetre.__init__(self, mySurface, title)
        self.Player = Player
        self.button = None
        self.display = "menu"
        self.changed = False

    """
        Cette method permet de gerer la transition
        entre le Menu et Le jeux
    """
    def controller(self):
        if self.changed == True:
            self.changed = False
            self.screen.fill((255,255,255))
            if self.display == "menu":
                self.started()
                self.runAffichage()
            if self.display == "game":
                self.game([4,3])

    """
        run menu
    """
    def started(self):
        # Init
        #self.screen.fill(WHITE)
        self.pygame.font.init()
        self.font = self.pygame.font.SysFont("comicsansms", 32)
        self.text = self.font.render("Mr driller", True, BLACK)

    """
        gere l'impression ecran position et actualisation
    """
    def runAffichage(self):
        #get screen size
        x, y = self.mySurface
        x, y = x/2,y/2
        self.subfont = self.pygame.font.SysFont("comicsansms", 20)

        # button
        self.button = pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect((x - 30), (y + 100), 60, 30))

        # position du text
        self.screen.blit( self.text,
            (x - (self.text.get_width() // 2), (y - 100) - (self.text.get_height() // 2))
        )

        # set button text position
        self.screen.blit(self.subfont.render('Start', True, BLACK), ((x - 30), y + 100))

        # maj affichage
        pygame.display.flip()

    """
        Gere un click
    """
    def run(self, event):
        if self.button != None :
            btn_x, btn_y = self.button.x, self.button.y

            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                comp_x = (x > btn_x and x < btn_x + 60)
                comp_y = (y > btn_y and y < btn_y + 30)
                if comp_x and comp_y:
                    print('click')
                    self.display = "game"
                    self.button = None
                    self.changed = True

    def clear(self):
        self.screen.fill((255,255,255))
        pygame.display.update()

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

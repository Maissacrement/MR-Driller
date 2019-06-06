from Objects.Fenetre import *

mySurface = (1000, 500)
title = "Sim"
Player = "prout"


class Simulation(Fenetre):

    def __init__(self, mySurface, title, Player):
        Fenetre.__init__(self, mySurface, title)
        self.Player = Player


    def createPlayer(self):

        # get screen size
        x, y = self.mySurface
        x, y = x / 2, y / 2

        # Titre
        path = "Assets/Perso_and_Menu/Perso.gif"
        background_image = pygame.image.load(path).convert()
        self.screen.blit(background_image,
                         (x - (180 // 2), (y - 100) - (100 // 2)),
                      (0, 0, 30, 30))

        pygame.display.flip()


    def main(self):
        return 0
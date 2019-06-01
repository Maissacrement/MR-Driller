# Import
import pygame, sys

# Constante private
WHITE = (255,255,255)

class Fenetre():

    def __init__(self, mySurface, title, Player):
        # Constante
        self.mySurface = mySurface
        self.title = title
        self.pygame = pygame
        self.Player = Player

    # SET
    def setMySurface(self, newSize):
        self.mySurface = newSize

    def getScreen(self):
        return self.screen

    def config(self):
        self.pygame.init()

        # Propriete de l'ecran
        self.screen = self.pygame.display.set_mode(self.mySurface)
        self.pygame.display.set_caption(self.title)
        self.screen.fill(WHITE)

        # Init
        self.pygame.font.init()
        font = self.pygame.font.SysFont("comicsansms", 32)

    def exit(self):
        self.pygame.quit()

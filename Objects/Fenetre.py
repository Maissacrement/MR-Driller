# Import
import pygame, sys

# Constante private
WHITE = (255,255,255)

class Fenetre():

    def __init__(self, mySurface, title):
        # Constante
        self.mySurface = mySurface
        self.title = title
        self.pygame = pygame
        self.screen = None
        self.font = None

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
        self.insertBackg()

    def insertBackg(self):

        # Inserer un fond d'ecran
        path = "Assets/Backgrounds/background.png"
        background_image = pygame.image.load(path).convert()
        background_image = pygame.transform.scale(background_image, self.mySurface)
        self.screen.blit(background_image, [0, 0])

    def exit(self):
        self.pygame.quit()

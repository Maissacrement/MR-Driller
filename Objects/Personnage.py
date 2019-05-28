from Objects.Base import *

class Personnage(Base):

    """Creation d'un Personnage selon Base"""

    def __init__(self, name, position, img=None, air=100, vie=1):
        """Constante"""
        Base.__init__(self, position, vie) # Create a block
        self.img = img # img src du personnage non obligtoire a l'initialisation
        self.name = name # nom du personnage
        self.air = air # pourcentage d'air

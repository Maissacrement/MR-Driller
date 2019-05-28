from Objects.Base import *

class Capsule(Base):

    """Creation d'une capsule d'aire selon Base"""

    def __init__(self,position, vie=1):
        """Constante"""
        Base.__init__(self, position, vie=1) # Create a block

    def earnLife(self, Personnage, vie):
        Personnage.vie+= vie

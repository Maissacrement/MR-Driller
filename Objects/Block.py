from Objects.Base import *
import time

class Block(Base):

    """Creation d'un Block selon Base"""

    def __init__(self,couleur,position, vie=1, merge=True, expire=0):
        """Constante"""
        Base.__init__(self, position, vie)
        self.couleur = couleur
        self.merge = merge # Possibilité de fusionner avec un autre block
        self.expire = expire # Block not autoremove if value is 0
        """reject"""
        if type(couleur) is not str:
            raise NameError('Color doit etre une chaine de caractere')

        if type(merge) is not bool:
            raise NameError('Merge est la capacicté d\'un block a fusionner avec un autre \nLa valeur doit etre un boolean')

    def __del__(self):
        print("deleted")

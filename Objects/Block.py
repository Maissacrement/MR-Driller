from Objects.Base import *
import time

class Block(Base):

    """Creation d'un Block selon Base"""

    def __init__(self,couleur,position, vie=1, merge=True, expire=0):
        """reject"""
        self.reject(couleur, expire, merge) # Pass if args have good type
        """Constante"""
        Base.__init__(self, position, vie)
        self.couleur = couleur # represente la couleur du block
        self.merge = merge # Possibilité de fusionner avec un autre block
        self.expire = expire # Block not autoremove if value is 0

    # Methods

    # Functions

    """
        compare le block courrant au Blocks
        passer en passer en parametre
    """
    def compareBlock(self, Block):
        merge = False # Par defaut les block ne fusionne pas
        sameColor = (self.couleur == Block.couleur) # Si les block ont la meme couleur
        sideOf = self.sideOf(Block) # Si les Block sont cote a cote

        if (sameColor and sideOf):
            merge = True # les bock peuvent fusionner

        return merge

    """
        permet de savoir si le block passer en parametre
        est a cote du Block courant
    """
    def sideOf(self, Block):
        side = False # Par defaut le block ne sont pas cote a cote
        pos = self.sideOfMe() # get an array of position
        blockPosition = Block.position # assign constante block position
        i = 0

        while (i < len(pos) and side == False):
            print('position: ', pos[i],', block pos:', blockPosition)
            if pos[i] == blockPosition:
                side = True # les block sont proche

            i+=1

        return side

    """
        retourne les position disponible aux alentour
        du Block courant
        --------------------------
        @return Array<> of position
    """
    def sideOfMe(self):
        position = [] # Init an empty array
        x, y = self.position # On enregistre les coordonne dans des variable

        position.append([x, y - 1]) if  (y - 1 >= 0) else None # En haut
        position.append([x - 1, y]) if  (x - 1 >= 0) else None # A gauche
        position.append([x, y + 1]) # En bas
        position.append([x + 1, y]) # A droite

        return position # On retourne les coordonnée

    # Procedures
    def reject(self, couleur, expire, merge):
        if type(couleur) is not str:
            raise NameError('Color doit etre une chaine de caractere')

        if type(expire) is not int:
            raise NameError('Expire doit etre un entier')

        if type(merge) is not bool:
            raise NameError('Merge est la capacicté d\'un block a fusionner avec un autre \nLa valeur doit etre un boolean')

    def __del__(self):
        print("deleted")

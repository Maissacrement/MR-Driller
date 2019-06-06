import Functions.createGoodBlock as Block
import Functions.getRandomColor as Color
import random

class ArrayBlock():

    """Propriete generale d'un Block."""

    def __init__(self,l,c):
        """Constante"""
        self.blocks = []
        self.l = l # ligne
        self.c = c # colonne
        self.level = 1

        #Generate Array on creted instance
        self.generateArray()

        """End Init"""

    """
        Generate nitialise un tableau de taille (n,m),
        n étant la largeur (fixe) et m étant la longueur (modulable)
    """
    def generateArray(self, level=0):
        self.blocks.append([0] * self.c)
        for i in range(self.l):
            self.blocks.append([])
            for j in range(self.c):
                random = Color.getRandomColor(level)
                self.blocks[i+1].append(Block.createGoodBlock(random, [i, j]))
                if(j == self.c):
                    self.blocks[i+2].append(Block.createGoodBlock(Color.getRandomColor(level), [i, j]))

    """
        Get block size
    """
    def getSize(self):
        return [self.c, self.l]

    """
        set Block size
    """
    def setSize(self, l,c):
        self.l, self.c = l,c

    """
        Up level
    """
    def changeLevel(self):
        self.level+=1

    """
        Recuperer un block selon sa position
    """
    def getBlock(self, position):
        """reject"""
        if type(position) is not list:
            raise NameError('Position doit etre une list de forme [x,y]')

        else :
            if len(position) != 2 or (type(position[0]) is not int) or (type(position[1]) is not int):
                raise NameError('Assurer vous que vous n\'avez pas plus de 2 coordonne [x,y] et qu\' il s\'agit de 2 entiers')

            else:
                return self.blocks[position[0]][position[1]]

import Functions.createGoodBlock as Block
import Functions.getRandomColor as Color
import random

class ArrayBlock():

    """Propriete generale d'un Block."""

    def __init__(self,c,l):
        """Constante"""
        self.blocks = []
        self.c = c # colonne
        self.l = l # ligne

        """
            Boucle for qui : initialise un tableau de taille (n,m),
            n étant la largeur (fixe) et m étant la longueur (modulable)
        """
        for i in range(c):
            self.blocks.append([])
            for j in range(l):
                random = Color.getRandomColor()
                self.blocks[i].append(Block.createGoodBlock(random, [i, j]))
                if(i == l):
                    self.blocks[i+1].append(Block.createGoodBlock(Color.getRandomColor(), [i, j]))
                #index.blocks(nom de la sous-liste)
        """reject"""
        #if type(blocks) is not list:
            #raise NameError('Position doit etre une list de forme [x,y]')

    def getBlock(self, position):
        """reject"""
        if type(position) is not list:
            raise NameError('Position doit etre une list de forme [x,y]')

        else :
            if len(position) != 2 or (type(position[0]) is not int) or (type(position[1]) is not int):
                raise NameError('Assurer vous que vous n\'avez pas plus de 2 coordonne [x,y] et qu\' il s\'agit de 2 entiers')

            else:
                return self.blocks[position[0]][position[1]]
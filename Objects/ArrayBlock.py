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

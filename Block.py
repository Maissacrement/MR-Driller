class Block():

    """Propriete generale d'un Block."""

    def _init_(self,couleur,positionx,positiony):
        """Constante"""
        self.couleur = couleur
        if type(couleur) is not str:
            raise ValueError
        self.positionx = positionx
        if type(positionx) is not int:
            raise ValueError
        self.positiony = positiony
        if type(positiony) is not int:
            raise ValueError
        vie = int()
        if type(vie) is not int:
            raise ValueError

    """fonction qui detruit le l'Object block """
    def __del__():
        print("le block a ete detruit")


    """fonction verification si block est detruit ou pas """
    def isDead():
        # vartiable bool qui renvoie si le block est vivaant ou mort
        estvivant = True

        #vérification de la condition de mort
        if vie <= 0:
            estvivant = False
        return boolvivant

    """fonction qui tcheck si il y a un block autour du block"""
    """def nearOf(positionx,positiony):
        print("positionx")"""

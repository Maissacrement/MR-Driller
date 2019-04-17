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
        self.positiony positiony
        if type(positiony) is not int:
            raise ValueError
        vie = int()
        if type(vie) is not int:
            raise ValueError

    """fonction verification si block est detruit ou pas """
    def isDead():
        #bool qui
        estvivant = True
        if vie <= 0:
            estvivant = False
        return boolvivant

    """fonction qui tcheck si il y a un block autour du block"""
    def nearOf(positionx,positiony):

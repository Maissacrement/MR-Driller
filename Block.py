class Block():

    """Propriete generale d'un Block."""

    def __init__(self,couleur,position, vie=3):
        """Constante"""
        self.couleur = couleur
        self.position = position
        self.vie = int(vie)

        """reject"""
        if type(couleur) is not str:
            raise ValueError

        if type(position) is not list:
            raise ValueError

        if type(self.vie) is not int:
            raise ValueError

    """fonction verification si block est detruit ou pas """
    def isDead():
        #bool qui
        estvivant = True
        if self.vie <= 0:
            estvivant = False
        return boolvivant

    """fonction qui tcheck si il y a un block autour du block"""
    def nearOf(position):
        pass # Pas encore definie

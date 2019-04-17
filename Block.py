class Block():

    """Propriete generale d'un Block."""

    def __init__(self,couleur,position, vie=3):
        """Constante"""
        self.couleur = couleur
        self.position = position
        self.vie = int(vie)

        """reject"""
        if type(couleur) is not str:
            raise NameError('Color doit etre une chaine de caractere')

        if type(position) is not list:
            raise NameError('Position doit etre une list de forme [x,y]')

        else :
            if len(position) != 2 or (type(position[0]) is not int) or (type(position[1]) is not int):
                raise NameError('Assurer vous que vous n\'avez pas plus de 2 coordonne [x,y] et qu\' il s\'agit de 2 entiers')

        if type(vie) is not int:
            raise NameError('Vie doit un nombre')

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

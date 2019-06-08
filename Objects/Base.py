class Base():

    """
        Base est la propriete commune aux Block,
        Personnage et Capsule d'air
    """

    def __init__(self,position, vie=1):
        """Constante"""
        self.position = position
        self.vie = int(vie)

        """reject"""
        if type(position) is not list:
            raise NameError('Position doit etre une list de forme [x,y]')

        else :
            if len(position) != 2 or (type(position[0]) is not int) or (type(position[1]) is not int):
                raise NameError('Assurer vous que vous n\'avez pas plus de 2 coordonne [x,y] et qu\' il s\'agit de 2 entiers')

        if type(vie) is not int:
            raise NameError('Vie doit un nombre')


    # Methods

    # Functions

    """fonction verification si block est detruit ou pas """
    def isDead():
        # vartiable bool qui renvoie si le block est vivaant ou mort
        estvivant = True

        #vérification de la condition de mort
        if self.vie <= 0:
            estvivant = False
        return estvivant

    """fonction qui tcheck si il y a un block autour du block"""
    def nearOf(position):
        pass

    def setPosition(self, pos):
        self.position[0], self.position[1] = pos

    def incX(self, max):
        if self.position[1] < max :
            self.position[1] = self.position[1] + 1

    def incY(self, max):
        if self.position[0] < max:
            self.position[0] = self.position[0] + 1

    def decX(self):
        if self.position[1] > 0:
            self.position[1]-=1

    def decY(self):
        if self.position[0] > 0:
            self.position[0]-=1

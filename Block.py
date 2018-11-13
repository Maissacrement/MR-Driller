# Creation d'un Block
class Block():
    """Propriete generale d'un Block."""
    def __init__(self, nom):
        """Constante"""
        self.DIMENSION = 5,5
        self.FORCE = 5
        """Variable"""
        self.nom = nom

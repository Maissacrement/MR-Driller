# Creation de la class Score
class Score():
    """Propriete generale du score."""
    def __init__(self, score):
        """score argument"""
        self.score = score
        self._best_score = 0

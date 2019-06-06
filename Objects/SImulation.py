from Objects.Fenetre import *

mySurface = (1000, 500)
title = "Sim"
Player = "prout"


class Simulation(Fenetre):

    def __init__(self, mySurface, title, Player):
        Fenetre.__init__(self, mySurface, title)
        self.Player = Player

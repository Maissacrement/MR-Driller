# Import
from random import * # Get Random

# Constante of array color
REGULAR=['red', 'blue', 'green', 'yellow'] # Block au proprieté commune
SPECIAL=['brown', 'white', 'crystal'] # Block au proprieté commune

"""
    Renvoie aleatoirement une couleur
    selon un degree de proportionnalité.
    --------------------------------
    @return: Dict {
        "color" : String,
        "Special" : Bool
    }
"""
def getRandomColor():
    # Init
    isSpecial=False # say if the block is SPECIAL

    # Ici on choisit 1/5 pour les variable SPECIAL et 4/5 pour les REGULAR
    arrayOfColor = (REGULAR * 2) + SPECIAL + (REGULAR * 2)

    # Obtenir aleatoirement un nombre et l'ajouter à la variable index,
    # Selon un ensemble allant de 1 a taille de la variable arrayOfColor
    index = randint(1, len(arrayOfColor) - 1)

    # Color actual of the block
    color = arrayOfColor[index]

    # Check if the block is SPECIAL
    if color in SPECIAL:
        isSpecial = True

    return {
        "color" : color,
        "isSpecial" : isSpecial
    }

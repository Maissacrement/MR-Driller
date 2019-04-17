from Block import *

"""
    Renvoie un Block SPECIAL si isSpecial est vrai
    ou un block normal sinon
    --------------------------------
    @params:
        Dict : getRandomColor() {
            Couleur : String
            isSpecial : Bool
        }
        Position : Array<Int,Int>
            coordonne [x,y]
        Vie : Int
        merge : Bool
    --------------------------------
    @return: Object {
        Block
    }
"""
def createGoodBlock(Dict, position, vie=5, merge=True):
    # Si il s'agit d'un block special nous devrons gerer les different cas
    # Avec des conditions
    if Dict.isSpecial:
        return Block(merge, Dict.color, vie, position)

    #Sinon on garde les propriete general d'un block
    else:
        return Block(merge, Dict.color, vie, position)

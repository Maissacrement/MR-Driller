from Objects.Block import * # Recuperer l'object Block

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
def createGoodBlock(Dict, position, vie=1, merge=True):
    # Si il s'agit d'un block special nous devrons gerer les different cas
    # Avec des conditions
    print(Dict)
    if Dict['isSpecial']:
        if Dict['color'] == "brown":
            return Block(Dict['color'], position, 5) # Si le Block est marrons il a 5 vie
        if Dict['color'] == "white":
            return Block(Dict['color'], position, vie, False) # Les blocks blancs ne peuvent pas fusionner entre eux
        if Dict['color'] == "crystal":
            return Block(Dict['color'], position) # Pas finie

    #Sinon on garde les propriete general d'un block
    else:
        return Block(Dict['color'], position)

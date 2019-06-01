from Objects.Block import * # Recuperer l'object Block

"""
    Genere selon les propriete placee en
    parametre le bon bloc
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
        expire : int
    --------------------------------
    @return: Object {
        Block
    }
"""
def createGoodBlock(Dict, position, vie=1, merge=True, expire=5):
    # Si il s'agit d'un block special nous devrons gerer les different cas
    # Avec des conditions
    if Dict['isSpecial']:
        if Dict['color'] == "brown":
            return Block(Dict['color'], position, vie=5) # Si le Block est marrons il a 5 vie
        if Dict['color'] == "white":
            return Block(Dict['color'], position, vie, False) # Les blocks blancs ne peuvent pas fusionner entre eux
        if Dict['color'] == "crystal":
            return Block(Dict['color'], position, vie, True, expire) # Le bloc disparait au bout d'un certain temps

    #Sinon on garde les propriete general d'un block
    else:
        return Block(Dict['color'], position, vie)

# if Dict['color'] == 0:
#    return 0 # add empty case

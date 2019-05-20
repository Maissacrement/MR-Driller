"""
    Test.py est notre fichier de test il nous permettera de test facilement toutes
    les fonctions et Object que l'on aura cree a fin de determiner simplement si
    la fonction est utilisable.
"""

import sys # Afin de recuperer l'argument souhaitez
# Local import
from Objects.Block import * # Recuperer l'object Block
from Objects.ArrayBlock import * # Recuperer l'object Block
from Functions.getRandomColor import * # Recuperer la function getRandomColor()
from Functions.createGoodBlock import * # Recuperer la function createGoodBlock

if sys.argv[1] == "Block":
     monBlock = Block("red", [9,6])

     print('Basic on Blocks and args')
     print(monBlock)
     print(vars(monBlock))

if sys.argv[1] == "getRandomColor":
    generate = getRandomColor()

    print(generate)

if sys.argv[1] == "createGoodBlock":
    generate = getRandomColor()
    generateGoodBlock = createGoodBlock(generate, [1,1])

    print('Welcom on createGoodBlock')
    print(generateGoodBlock)
    print(vars(generateGoodBlock))

if sys.argv[1] == "ArrayBlock":
    tab = ArrayBlock(8,8)


    print('Welcom on ArrayBlock\n')
    print(tab, '\n')

    print('List of Blocks\n')
    for i in range(len(tab.blocks)):
        for j in range(len(tab.blocks[0])):
            print(vars(tab.blocks[i][j]))
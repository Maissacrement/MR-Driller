"""
    Test.py est notre fichier de test il nous permettera de test facilement toutes
    les fonctions et Object que l'on aura cree a fin de determiner simplement si
    la fonction est utilisable.
"""

import sys # Afin de recuperer l'argument souhaitez
# Local import
## Objects
from Objects.Block import * # Recuperer l'object Block
from Objects.Capsule import * # Recuperer l'object Capsule
from Objects.Personnage import * # Recuperer l'object Personnage
from Objects.ArrayBlock import * # Recuperer l'object Block
from Objects.Menu import * # Recuperer le Menu
from Objects.Simulation import *
## Function
from Functions.getRandomColor import * # Recuperer la function getRandomColor()
from Functions.createGoodBlock import * # Recuperer la function createGoodBlock

# Objects

if sys.argv[1] == "Block":
     monBlock = Block("red", [9,6], 1, True, 2)
     monBlock.kill()

     print('Basic on Blocks and args')
     print(monBlock)
     print(vars(monBlock))

if sys.argv[1] == "Capsule":
     maCapsule = Capsule([0,1])

     print('Create capsule Capsule')
     print(maCapsule)
     print(vars(maCapsule))

if sys.argv[1] == "Personnage":
     monPerso = Personnage("perso0",[0,1], "")

     print('Create capsule Capsule')
     print(monPerso)
     print(vars(monPerso))

if sys.argv[1] == "ArrayBlock":
    tab = ArrayBlock(8,8)


    print('Welcom on ArrayBlock\n')

    print('List of Blocks\n')
    for i in range(len(tab.blocks)):
        for j in range(len(tab.blocks[0])):
            print(vars(tab.blocks[i][j]))

    print('\n', tab.blocks)

# Functions

if sys.argv[1] == "getRandomColor":
    generate = getRandomColor()

    print(generate)

if sys.argv[1] == "createGoodBlock":
    generate = getRandomColor()
    generateGoodBlock = createGoodBlock(generate, [1,1])

    print('Welcom on createGoodBlock')
    print(generateGoodBlock)
    print(vars(generateGoodBlock))

if sys.argv[1] == "Simulation":
    inProgress = True
    simulation = Simulation(mySurface, title, Player)
    simulation.config()
    simulation.createPlayer()

    while inProgress:

        # Quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inProgress = False

        # Maj
        pygame.display.update()

    pygame.quit()


if sys.argv[1] == "Menu":
    print('Welcom in Menu Test')
    inProgress = True
    nb_col = 10

    # init
    tab = ArrayBlock(16, nb_col) # Generate Array
    perso1 = Personnage("myperso",[0,nb_col//2], "Assets/Blocks/air.png")

    printc = []
    for el in range(len(tab.blocks)):
        printc.append([])
        for blk in tab.blocks[el]:
            if not type(blk) == int:
                printc[el].append(blk.couleur)
            else:
                printc[el].append(0)

    print(printc)

    # Init plateform
    jeux = Menu((1000,500),"Mr driller") # Get Menu instance
    jeux.init(tab, perso1) # init game config

    # Start Menu of Game
    jeux.started()

    while inProgress:

        # Quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inProgress = False

            jeux.run(event) # gerer les evenement click
            jeux.controller() # gere les transition entre scene du jeux
            jeux.simulateAtClick(event)
            jeux.movePerso(event)

        # Maj
        pygame.display.update()

    pygame.quit()

from Objects.Personnage import * # Recuperer l'object Personnage
from Objects.ArrayBlock import * # Recuperer l'object Block
from Objects.Menu import * # Recuperer le Menu

def main():
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

if __name__ == "__main__":
    # execute only if run as a script
    main()

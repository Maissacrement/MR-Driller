from Objects.Fenetre import *
from Objects.Block import * # Recuperer l'object Block
from Objects.Personnage import * # Recuperer l'object Personnage
from time import *

WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)
BLUE = (0,0,255)
YELLOW = (240,176,16,1)

class Menu(Fenetre):

    def __init__(self, mySurface, title):
        Fenetre.__init__(self, mySurface, title)
        self.display = "menu"
        self.changed = False
        self.simulation = False
        self.display_line = 10 # Cut screen vertically in 10
        self.split = 3 # proportionnalité du partage d'ecran
        self.screenLimit = 6 # started draw block
        self.level = 1

    # Methods

    ## Procedures
    """
        init variable of games and run config
    """
    def init(self, array, perso):
        # Constant

        # Get screen size
        x, y = self.mySurface # Taille total de l'ecran
        # ecran scindé en longueur
        self.sizeFirstScreen = x - (x/self.split) # ecran1 : Jeux
        self.sizeSecondScreen = x - self.sizeFirstScreen # ecran2 : Score

        # Colonne, Line pour l'affichage
        x_col,y_line = array.c, self.display_line

        # Block size : width and height
        self.block_size = [self.sizeFirstScreen/x_col, y/y_line]

        # Save Array
        self.array = array

        # Perso
        self.perso = perso
        print(vars(self.perso))

        # Ajout du personnage sur la scene de jeux
        py,px = perso.position
        self.array.blocks[0][5] = perso

        print(self.array)

        # run config
        self.config()

    """
        run menu
    """
    def started(self):
        # Init
        self.pygame.font.init()
        self.font = self.pygame.font.SysFont("comicsansms", 32)
        self.text = self.font.render("Mr driller", True, BLACK)

        #get screen size
        x, y = self.mySurface
        x, y = x/2,y/2
        self.subfont = self.pygame.font.SysFont("comicsansms", 20)

        # Titre
        path = "Assets/Perso_and_Menu/Perso.gif"
        background_image = pygame.image.load(path).convert()
        self.screen.blit(background_image,
            (x - (180 // 2), (y - 100) - (100 // 2)),
        (160, 490, 180, 100))

        # cree le button et le positionner
        self.button = pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect((x - 30), (y + 100), 60, 30))

        # gerer la position du text du boutton
        self.screen.blit(self.subfont.render(' Start', True, BLACK), ((x - 30), y + 100))

        # maj affichage
        pygame.display.flip()

    """
        run game
    """
    def game(self):

        #GET Blocks
        list_of_blocks = self.array.blocks

        # Get block size
        block_size = self.block_size

        for y in range(len(list_of_blocks)):
            for x in range(len(list_of_blocks[y])):

                if not type(list_of_blocks[y][x]) == int:
                    if type(list_of_blocks[y][x]) == Block:
                        # Define image path
                        path = "Assets/Blocks/" + list_of_blocks[y][x].couleur + ".png"

                    elif type(list_of_blocks[y][x]) == Personnage:
                        path = "Assets/Blocks/air.png"

                    # Draw block
                    self.drawBlock([x, y + self.screenLimit], path)


    """
        Gerer la transition entre le Menu et Le jeux
    """
    def controller(self):
        if self.changed == True:
            self.changed = False
            self.insertBackg()
            if self.display == "menu":
                self.started()
            if self.display == "game":
                if self.array == None:
                    print('Game hasn\'t init')
                else:
                    # Lancer le jeux
                    self.game()

    """
        Gere un click
    """
    def run(self, event):
        if self.button != None :
            btn_x, btn_y = self.button.x, self.button.y

            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                comp_x = (x > btn_x and x < btn_x + 60)
                comp_y = (y > btn_y and y < btn_y + 30)
                if comp_x and comp_y:
                    print('click')
                    self.display = "game"
                    self.button = None
                    self.changed = True

    """
        Print graphical block
        ---------------------
        @params:
            pos: Array<Int,Int> as [x,y]
                -indiqué la position du block
            img: String
                - indique le path relatif a l'image
        @params optional:
            merged: boolean
                -indiqué si il s'agit d'un bloclie ou non
    """
    def drawBlock(self, pos, img, merged=False):
        x, y = 0,0 # image position

        # onMerge remove spaces
        if merged:
            x, y = 20, 8 # linked block

        #img path
        #display img on the window
        pos_x, pos_y = pos # GET Block position
        translate_h, translate_v = self.block_size  # Get Block size
        size = (x, y, translate_h, translate_v) # Define block dimension

        pos = [translate_h * pos_x, translate_v * pos_y]
        background_image = pygame.image.load(img) # Chargez l'image
        background_image = pygame.transform.scale(
            background_image, (1800, int(60))
        )
        self.screen.blit(background_image,
            pos, # Position
        size) # Taille

    """
        Deplace la scene de jeux vers le haut
    """
    def moveSceneTop(self):
        if self.screenLimit > 0:
            self.screenLimit-=1
        else:
            if len(self.array.blocks) > 0:
                self.array.blocks.pop(0)
                self.perso.position[0]-=1 # UPDATE PERSO POSITION
                #self.array.popBlockLie([[3, 0],[3,1]])
                print('remove')
            else:
                self.screenLimit=6
                self.array.generateArray(self.level)
                self.array.changeLevel()
                print('generate another tab')

        self.refreshScreen()

    """
    def movePerso(self, event):
        Perso = self.perso
        if event.type == pygame.KEYDOWN:
            py,px = Perso.position
            print('px: ', px)
            # On initialise la case precedante
            #del self.array.blocks[py][px]
            if event.key == pygame.K_LEFT:
                self.array.blocks[py][px] = 0
                Perso.position[1]-=1
                py,px = Perso.position
                self.array.blocks[py][px] = Perso
                print("LEFT")
            if event.key == pygame.K_RIGHT:
                self.array.blocks[py][px] = 0
                Perso.position[1]+=1
                py,px = Perso.position
                self.array.blocks[py][px] = Perso
                print("LEFT")
            if event.key == pygame.K_DOWN:
                print('DOWN')
                print([py,px])
                print(self.array.blocks)
                self.array.blocks[px][py] = 0
                Perso.position[0]+=1
                py,px = Perso.position
                self.array.blocks[px][py] = Perso
                self.moveSceneTop()

            self.insertBackg()
            self.game()
    """

    def refreshScreen(self):
        self.insertBackg()
        self.game()

    def movePerso2(self, event):
        Perso = self.perso # SAVE PERSO
        # KEYBOARD INPUT
        if event.type == pygame.KEYDOWN:
            py,px = Perso.position # GET POSITION
            if event.key == pygame.K_LEFT and px > 0:
                self.array.blocks[py][px] = 0
                Perso.position[1]-=1
                py,px = Perso.position
                self.array.blocks[py][px] = Perso
                self.refreshScreen()
            if event.key == pygame.K_RIGHT and px > len(self.array.blocks) - 1:
                self.array.blocks[py][px] = 0
                Perso.position[1]+=1
                py,px = Perso.position
                self.array.blocks[py][px] = Perso
                self.refreshScreen()
            if event.key == pygame.K_DOWN: # DOWN INPUT
                if py > 0: # Y COORDONATE > 0
                    print([py,px])
                    self.array.blocks[py-1][px] = 0 # REMOVE PREVIOUS BLOCK
                    self.array.blocks[py][px] = 0 # REMOVE BLOCK
                    self.array.blocks[py][px] = Perso # REPLACE 0 BY PERSO
                    self.perso.position[0]+=1 # CHANGE TO DOWN CASE
                else:
                    self.perso.position[0]+=1 # CHANGE TO DOWN CASE
                    self.array.blocks[py][px] = 0 # INIT CASE
                    self.array.blocks[py][px] = Perso # REMOVE BLOCK

                self.moveSceneTop()

    def movePerso(self, event):
        blocks = self.array.blocks
        maxX = len(blocks[0]) - 1
        maxY = len(blocks) - 1
        if event.type == pygame.KEYDOWN:
            py,px = self.perso.position
            print('px: ', [py,px])
            # On initialise la case precedante
            #del self.array.blocks[py][px]
            if event.key == pygame.K_LEFT:
                self.perso.decX()
                py,px = self.perso.position
                self.array.blocks[py][px+1] = 0
                self.array.blocks[py][px] = 0
                self.array.blocks[py][px] = self.perso
                print('px: ', [py,px])

                self.refreshScreen()
            if event.key == pygame.K_RIGHT:
                self.perso.incX(maxX)
                py,px = self.perso.position
                self.array.blocks[py][px-1] = 0
                self.array.blocks[py][px] = 0
                self.array.blocks[py][px] = self.perso
                print('px: ', [py,px])

                self.refreshScreen()
            if event.key == pygame.K_DOWN: # DOWN INPUT
                self.perso.incY(maxY)
                py,px = self.perso.position
                self.array.blocks[py-1][px] = 0 # REMOVE PREVIOUS BLOCK
                self.array.blocks[py][px] = 0 # REMOVE BLOCK
                self.array.blocks[py][px] = self.perso # REPLACE 0 BY PERSO
                print('py: ', [py,px])
                """
                if py > 0: # Y COORDONATE > 0
                    print([py,px])
                    self.array.blocks[py-1][px] = 0 # REMOVE PREVIOUS BLOCK
                    self.array.blocks[py][px] = 0 # REMOVE BLOCK
                    self.array.blocks[py][px] = self.perso # REPLACE 0 BY PERSO
                    # self.perso.position[0]+=1 # CHANGE TO DOWN CASE
                else:
                    # self.perso.position[0]+=1 # CHANGE TO DOWN CASE
                    self.array.blocks[py][px] = 0 # INIT CASE
                    self.array.blocks[py][px] = self.perso # REMOVE BLOCK
                """

                #Refresh when drill
                self.moveSceneTop()

    """
        Simuler la destruction d'un block
    """

    """
        Level up
    """

    """
        Test Function
        ---------------------------------------------------------
    """

    """
        Lancer la simulation de la chute de blocks
        au Click
        ------------------------------------------
        @params:
            - event : permet de recuperer un evenement sur la fenetre
    """
    def simulateAtClick(self, event):
        # BlockLie
        array = [
            [3,4],
            [3,1],
            [3,3],
            [3,2],
            [4,4],
            [4,5]
        ]
        # Init  simulation

        if self.display == "game":
            #self.mergeBlocks(array)
            if event.type == pygame.MOUSEBUTTONUP and self.simulation == True:
                #self.chuteSimulation(array)
                self.moveSceneTop()

            self.simulation = True

    """
        Simulation de la chute d'un ensemble de block
        ---------------------------------------------
        @params:
            - blockLie : Tableu de position
    """
    def chuteSimulation(self, blockLie):
        newArray = []
        blockLie.sort()

        for el in blockLie:
            newArray.append([el[0], el[1] + 1])

        print(newArray)
        self.insertBackg()
        #self.mergeBlocks(newArray) # maj graphique du jeux

        # maj affichage
        pygame.display.flip()

    """
        The array need sorted !
        Create auto chechk
        -----------------------
        @params:
            - blockLie : Tableu de position
    """
    def canIMoveDown(self, blockLie):
        i = 0
        iCan = True
        emplacement = self.getBlockWhoWantMove(blockLie)
        blocks = self.array.blocks

        while i < len(emplacement) and iCan:
            x,y = emplacement[i]
            if not blocks[x][y] == None:
                iCan = False

        return iCan

    """
        Recuperer un tableau de position
        representant l'emplacement des
        block de dernier rang
        -------------------------------
        @params:
            - blockLie : Tableu de position
    """
    def getBlockWhoWantMove(self, blockLie):
        blocks = []
        y = getYCoord(blockLie)
        i = 0

        while i < len(blockLie):
            if blockLie[i][0] == y:
                # Apply + [1,0] and add on block
                blocks.append([blockLie[i][0] + 1, blockLie[i][1]])

        return blockLie

    """
        Get last Y coordonate in an array of position
    """
    def getYCoord(self, array):
        return array[len(array) - 1][0]

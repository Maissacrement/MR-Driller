from Objects.Fenetre import *
from time import *

WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)
BLUE = (0,0,255)
YELLOW = (240,176,16,1)

class Menu(Fenetre):

    def __init__(self, mySurface, title, Player):
        Fenetre.__init__(self, mySurface, title)
        self.Player = Player
        self.array = None
        self.button = None
        self.display = "menu"
        self.changed = False
        self.chute = False
        self.simulation = False
        self.split = 6

    # Methods

    ## Procedures

    """
        init games params
    """
    def init(self):
        # Constant
        x, y = self.mySurface # recuperer la taille de l'ecran
        self.sizeFirstScreen = x - (x/self.split) # ecran scindé en longueur
        self.sizeSecondScreen = x - self.sizeFirstScreen

        ## User entry
        x_col,y_line = self.array.getSize()

        # Size of block as width and height of screen
        self.block_size = [x//x_col, y//y_line]

        self.config()

    """
        Set Array
    """
    def setArray(self, anArray):
        self.array = anArray

    """
        Gerer la transition entre le Menu et Le jeux
    """
    def controller(self):
        if self.changed == True:
            self.changed = False
            self.insertBackg()
            # self.clear()
            if self.display == "menu":
                self.started()
            if self.display == "game":
                if self.array == None:
                    print('Ajouter un array')
                else:
                    self.game() # partie logique du jeux
                    #self.chuteSimulation()
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

        # gerer la position du Titre Mr driller
        #self.screen.blit( self.text,
        #    (x - (self.text.get_width() // 2), (y - 100) - (self.text.get_height() // 2))
        #)

        # gerer la position du text du boutton
        self.screen.blit(self.subfont.render(' Start', True, BLACK), ((x - 30), y + 100))

        # maj affichage
        pygame.display.flip()

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
        reinitialise une fenetre
    """
    def clear(self):
        self.screen.fill((255,255,255))
        pygame.display.update()

    """
        run game
    """
    def game(self):

        #GET Blocks
        list_of_blocks = self.array.blocks

        # Get block size
        block_size = self.block_size

        # maj affichage
        pygame.display.flip()

        # Test de block lie
        array = [
            [3,4],
            [3,1],
            [3,3],
            [3,2],
            [4,4],
            [4,5]
        ]

        self.mergeBlocks(array) # maj graphique du jeux

        for blocks in list_of_blocks:
            for block in blocks:

                # size block_size [0]: longueur, [1]: largeur
                size = (0, 0, block_size[0], block_size[1])
                #img path
                path = "Assets/Blocks/" + block.couleur + ".png"
                #display img on the window

                if not block.position in array:
                    print(block.position)
                    self.insert(path, block.position, block_size, size)

    """
        Inserer un fond d'ecran
    """
    def insert(self, img, block_size, block_pos, size, zoom=(1400, int(60))):
        pos_x, pos_y = block_size # GET Block position
        translate_h, translate_v = block_pos  # Get Block size

        pos = [translate_h * pos_x, translate_v * pos_y]
        background_image = pygame.image.load(img) # Chargez l'image
        background_image = pygame.transform.scale(background_image, zoom) # Zoom
        self.screen.blit(background_image,
            pos, # Position
        size) # Taille

    """
        fusionner graphiquement les blocks
        ---------------------------------
        @params: {
            block_size : taille d'un block
            list: list de block lie
        }
    """
    def mergeBlocks(self, list):

        # Rangez la list dans l'ordre
        list.sort()

        # Get deplacement
        nb = len(list) # nb de blocks a fusionne

        """ Representation graphique """
        path = "Assets/Blocks/yellow.png" # Path of image

        size = self.block_size # position of a block in array of block

        #background_image = pygame.image.load(block['path']).convert() # Chargez l'image
        for nb in range(len(list)):
            rect_conf = (size[0] * list[nb][0], size[1] * list[nb][1], size[0], size[1])
            background_image = pygame.draw.rect(
                self.screen,
                YELLOW,
                pygame.Rect(rect_conf)
            )
            self.insert(path, list[nb], size, (5, 5, size[0] + 5, size[1] -10), (1400, int(80)))

    """
        Lancer la simulation de la chute de blocks
        au Click
        ------------------------------------------
        @params:
            - event : permet de recuperer un evenementsur la fenetre
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

        if self.display == "game":
            if event.type == pygame.MOUSEBUTTONUP and self.simulation == True:
                print('click here')
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
        self.mergeBlocks(newArray) # maj graphique du jeux

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

    """
        Deplace la scene de jeux vers le haut
    """
    def moveSceneTop(self):
        self.array.blocks.pop(0)
        self.insertBackg()
        self.game()

    """
        Simuler la destruction d'un block
    """

    ## Functions

    """
        Traduire un deplacement en coordonée
        Cree une fonction qui me permet de faire
        -1 et +1 dans un array
        ---------------------------------------
        @params:
            - tab: Array de position
        @return:
            - result: coordonée de deplacement
    def directionForFusion(self, tab):
        result = []

        for x in range(len(tab) - 1):

            x,y = (tab[x+1][0] - tab[x][0]), (tab[x+1][1] - tab[x][1])
            result.append([x,y])

        return result
    """

    # size pour 1 block block_size [0]: longueur, [1]: largeur
    #size = (0, 0, block_size[0], block_size[1])
    #path = "Assets/Blocks/yellow.png"
    #self.insert(path, list[0], block_size, size, (1250, int(60 * nb)))

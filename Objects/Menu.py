from Objects.Fenetre import *

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
        self.split = 6

    # Methods

    ## Procedures

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
        # Constant
        x, y = self.mySurface # recuperer la taille de l'ecran
        x = x - (x/self.split) # ecran scindé en longueur
        i=0 # itteration

        ## User entry
        x_col,y_line = self.array.getSize()

        # Element of compare min and max
        translate_h, translate_v = x//x_col, y//y_line
        block_size = [translate_h, translate_v]

        #GET Blocks
        list_of_blocks = self.array.blocks

        # maj affichage
        pygame.display.flip()

        array = [
            [3,4],
            [3,1],
            [3,3],
            [3,2],
            [4,4],
            [4,5]
        ]

        self.mergeBlocks(block_size, array) # maj graphique du jeux

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
        background_image = pygame.image.load(img).convert() # Chargez l'image
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
    def mergeBlocks(self, block_size, list):

        # Rangez la list dans l'ordre
        list.sort()

        # Get deplacement
        deplacement = self.directionForFusion(list)
        nb = len(list) # nb de blocks a fusionne

        block_display = {}

        """ Representation graphique """
        # size pour 1 block block_size [0]: longueur, [1]: largeur
        block_display['size'] = block_size # taille des blocks
        block_display['path'] = "Assets/Blocks/yellow.png" # Path of image

        """ Representation Logique """
        block_display['pos_of_linked_blocks'] = list # Tab of position
        block_display['deplacement'] = deplacement # represente les deplacements logique a affectue pour affiché les bloc lie

        self.drawMergeBlock(block_display)

    """
        affiche un block la fusion des bloc
        -----------------------------------
        @params: Block: {
            'size' : position of a block in array of block
            'block_size' : taille des blocks
            'path' : Path of image
            'pos_of_linked_blocks' : Tab of position
            'deplacement' : represente les deplacements logique a affectue pour affiché les bloc lie
        }
    """
    def drawMergeBlock(self, block):
        print(block)
        size = block['size'] # position of a block in array of block
        list = block['pos_of_linked_blocks'] # get position of linked block

        #background_image = pygame.image.load(block['path']).convert() # Chargez l'image
        for nb in range(len(list)):
            rect_conf = (size[0] * list[nb][0], size[1] * list[nb][1], size[0], size[1])
            background_image = pygame.draw.rect(
                self.screen,
                YELLOW,
                pygame.Rect(rect_conf)
            )

    ## Functions

    """
        Traduire un deplacement en coordonée
        Cree une fonction qui me permet de faire
        -1 et +1 dans un array
    """
    def directionForFusion(self, tab):
        result = []

        for x in range(len(tab) - 1):

            x,y = (tab[x+1][0] - tab[x][0]), (tab[x+1][1] - tab[x][1])
            result.append([x,y])

        return result

    # size pour 1 block block_size [0]: longueur, [1]: largeur
    #size = (0, 0, block_size[0], block_size[1])
    #path = "Assets/Blocks/yellow.png"
    #self.insert(path, list[0], block_size, size, (1250, int(60 * nb)))

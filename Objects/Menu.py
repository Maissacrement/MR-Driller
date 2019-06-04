from Objects.Fenetre import *

WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)
BLUE = (0,0,255)

class Menu(Fenetre):

    def __init__(self, mySurface, title, Player):
        Fenetre.__init__(self, mySurface, title)
        self.Player = Player
        self.array = None
        self.button = None
        self.display = "menu"
        self.changed = False
        self.split = 6

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
        self.screen.blit(self.subfont.render('Start', True, BLACK), ((x - 30), y + 100))

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
        Inserer un fond d'ecran
    """
    def insert(self, img, block_size, block_pos, size, zoom=(1250, int(58))):
        pos_x, pos_y = block_size # GET Block position
        translate_h, translate_v = block_pos  # Get Block size

        pos = [translate_h * pos_x, translate_v * pos_y]
        background_image = pygame.image.load(img).convert() # Chargez l'image
        background_image = pygame.transform.scale(background_image, zoom) # Zoom
        self.screen.blit(background_image,
            pos, # Position
        size) # Taille

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

        for blocks in list_of_blocks:
            for block in blocks:

                # size block_size [0]: longueur, [1]: largeur
                size = (0, 0, block_size[0], block_size[1])
                #img path
                path = "Assets/Blocks/" + block.couleur + ".png"
                #display img on the window

                if block.position != [3,3] and block.position != [3,4]:
                    print(block.position)
                    self.insert(path, block.position, block_size, size)

        self.mergeBlocks(block_size) # maj graphique du jeux


    """
        Cree une fonction qui me permet de faire
        -1 et +1 dans un array
    """

    """
        1. fonction permettant de retirer un block et de prolonger
        la taille du block adjacent
        2. pouvoir integrer un tableau de position
        3. essayer d'integrer la fonction a self.insert
        --------------------------------------------
    """
    def mergeBlocks(self, block_size):
        list = [
            [3,3],
            [3,4]
        ]

        print(list)

        # size block_size [0]: longueur, [1]: largeur
        size = (0, 0, block_size[0], block_size[1]  * 2)
        path = "Assets/Blocks/yellow.png"
        self.insert(path, list[0], block_size, size, (1250, int(120)))

        """
        for pos in list:

            # size block_size [0]: largeur, [1]: longueur
            size = (0, 0, block_size[0], block_size[1])
            path = "Assets/Blocks/yellow.png"
            self.insert(path, pos, block_size, size)
        """
    """
    # horizontal, vertical = 0,0
    # tracer = True
    # tracer_line = True
    while i < (x_col * y_line) + 1:
        size = (0, 0, translate_h, translate_v)
        path = "Assets/Blocks/yellow.png"
        self.insert(path, [horizontal, vertical], size)
        if i !=0:
            horizontal+= translate_h
            if(i % x_col == 0):
                vertical+= translate_v
                horizontal = 0
            # path = "Assets/Blocks/"+color[i-1]+".png"
            #if i < len(color) and color[i-1] != None:

        i+=1
        print('i:',i,vertical, horizontal)
    """

    """
    while tracer or tracer_line:
            size = (0, 0, translate_h, translate_v)

        if horizontal < x:

            self.pygame.draw.line(self.screen, BLACK, (horizontal, 0), (horizontal,y), 5)

            self.insert("Assets/Blocks/green.png", [horizontal, translate_v], size)

            horizontal+= translate_h

        elif tracer == True:
            tracer = False

        if vertical < y:
            self.pygame.draw.line(self.screen, BLACK, (0, vertical), (x,vertical), 5)

            vertical+= translate_v
        elif tracer_line == True:
            tracer_line = False
    """

    """
    def game(self, size):
        # Constant
        x, y = self.mySurface # recuperer la taille de l'ecran
        x = x - (x/6) # cree un espace pour le score

        ## User entry
        x_col,y_line = size

        # Element of compare min and max
        horizontal, vertical = 0,0
        translate_h, translate_v = x/x_col, y/y_line

        # Boolean
        tracer = True
        tracer_line = True

        while tracer:
            self.pygame.draw.line(self.screen, BLACK, (horizontal, 0), (horizontal,y), 5)
            horizontal+= translate_h
            if horizontal > x:
                tracer = False

        while tracer_line:
            self.pygame.draw.line(self.screen, BLACK, (0, vertical), (x,vertical), 5)
            vertical+= translate_v
            if vertical > y:
                tracer_line = False
    """

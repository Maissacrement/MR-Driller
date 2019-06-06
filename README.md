# MR Driller : 1DEV

## Jeux


News :  `Ajout d'un fichier Test.py permettant des tester rapidement un object ou une fonction. Afin de lancer un test suivre les indication enfin de chaques sous chapitre de documentation.`

### A faire

```

3. Completer Personnage :
    - ajout de la fonction de drill
    - fonction mouvements (Avec les spécificités)
    - objet à part =/= d'un bloc

5. ArrayBlock complete le tableau avec les bonne proportionnalite:
    - popBlock : supression d'un block
    - Update : faire descandre les blocs qd il y a des espaces vide
      (en gros gravité, besoin d'un check si un espace vide est en dessous d'un bloc)
    - Chute : En fonction de coordonné dire si un block peut descendre ou non
    - Lie : Renvoie true si un block peut etre lie a un autre
    - getBlockLie : Retourne un tableau de block selon le block passer en parametre
    - addBlockLie : Ajoute au tableau de block lie une liste de block
                    relie selon lie et compareBlock dans Block
    - popBlockLie : qui suprime tous les block lie du tableau

7. Menu:
    - Simuler la destruction d'un block

9. Stucture :
    - Init un tableau de block random, dont la proportionnalité peut être changée
      facilement en fonction du level.
    - Faire des fonctions pour chaque règle de jeu :
        -La fusion des blocs quand 3 ou plus
        -la destruction des blocs quand 3 ou plus
        -La chute des blocs
        -La mort quand plus d'air
        -Le game over quand plus de vie
        -la Mort quand écrasé par un bloc
        -La Pause!
```

### 1. Base

Intro: Cette class regroupe propriete commune entre les Blocks, Capsules, Personnages

```
    Class Base:
       Propriete : Params(position, vie)
         - Vie : Int
         - Position : Array<Int,Int>
             init [x,y]
       Methode:
          function:
          - isDead : Bool
          - nearOf : Array<Int, Int>
```

### 2. Creation des Blocks ✔

Into : Un block est un Object ayant une couleur, un nombre de vie, une position, une valeur reflettant sa capacité a pourvoir fusionner avec un autre block.

```
   Class Block(Base):
      Propriete: Param(couleur, position, vie, merge, expire)
        - merge : Bool
        - Couleur : String
        - expire : Int
        - Heritage Base:
          - Vie : Int
          - Position : Array<Int,Int>
              init [x,y]
      Methods:
        Function:
          - compareBlock(Blocs) : Bool
          - sideOf :Bool
          - sideOfMe : Bool
          - isDead : Bool
          - nearOf : Array<Int, Int>
          - Delete : Bool

      Détail methods:
        compareBlock : compare si ce Blocs peut etre Lie a selui
                       en parametre et renvoie un Boolean
        sideOf : permet de savoir si le block passer en parametre
                 est a cote du Block courant
        sideOfMe : retourne les position disponible aux
                   alentour du Block courant
        isDead : Si le bloc est vivant
        nearOf : Renvoie uniquement les coordonnées des blocs aux alentours
                Remarque : un block ne peut avoir des coordonnées où x < 0 ou x > n et y < 0 ou y > n
        Delete : Renvoie true si l'object a bien été supprimé
```

test : `python3 Test.py Block`

### 2.1. Creation de la fonction getRandomColor() ✔

Intro: Cette fonction renvoie une couleur aleatoirement selon une certaine proportionalité

```
  @return: Dict {
      "color" : String,
      "Special" : Bool
  }
```

test : `python3 Test.py getRandomColor`

### 2.2. Creation de la function createGoodBlock() ✔

Intro: En fonction de la couleur du block on cree un block avec des proprieté pouvant par example etre specifique

```
  @return : Block()
```

test : `python3 Test.py createGoodBlock`

### 2.3. Creation de la procedure delBlock()

Intro: Cette procedure supprime un block passer en parametre

### 2.4. Creation de la procedure de generateRandomBlock()

Intro: Cette procedure de genere aleatoirement des Block

## 3. Personnage ✔

Intro: L'Object Personnage traduit les actions du joueur qui le possede.
Le Personnage interagit directement avec les elements qui ont la meme base que lui.

```
  Class Personnage(Base):
     Propriete : Params(name, position, img, air, vie)
       - name : string
       - img : string
       - air : Int
       - Heritage Base:
         - Vie : Int
         - Position : Array<Int,Int> as [x, y]
     Methode:
       Procedure:
         - drill(Block)
         - mouvement

     Détail methods:
        drill : Supprimer un block
        mouvement :
        isDead : Si le bloc est vivant
        nearOf : Renvoie uniquement les coordonnées des blocs aux alentours
                Remarque : un block ne peut avoir des coordonnées où x < 0 ou x > n et y < 0 ou y > n
        Delete : Renvoie true si l'object a bien été supprimé
```

## 4. Capsule ✔

Intro: Capsule est une classe heritant de base et pouvant donner de la vie a un Personnage

```
  Class Capsule(Base):
     Propriete : Params(position, vie=1)
       - Heritage Base:
         - Vie : Int
         - Position : Array<Int,Int> as [x, y]
     Methode:
       Function:
         - getBlock([x,y])
         - isDead : Bool
         - nearOf : Array<Int, Int>
       Procedure:
         - earnLife
```

## 5. ArrayBlock

Intro: Il s'agit d'un tableau composé de Block

```
   Class ArrayBlock:
      Propriete et Params: (n, m)
        - blocks : Array<Block> as taille n x m
        - blocksLie : Array<> as []
      Methode:
        Function:
          - chute : Boolean
          - Lie : Boolean
        Procedure:
          - Update
          - popBlock()
          - getBlockLie(Block)
          - popBlockLie(ArrayofBlock)
          - addBlockLie(Block)

      Détail methods:
        chute : Boolean representant la posibilité pour un block de descendre ou non
        Lie : Renvoie true si un block peut etre lie a un autre
        getBlockLie : Retourne un tableau de block selon le block passer en parametre
        Update : faire descandre les blocs qd il y a des espaces vide
        popBlockLie : qui suprime tous les block lie du tableau
        addBlockLie : Ajoute au tableau de block lie une liste de block
                      relie selon lie et compareBlock dans Block
```

test : `python3 Test.py ArrayBlock`

## 6. Fenetre

Intro: Il s'agit d'une page blanche mère du menu et de la scene de jeu

```
    Class Fenetre:
      Propriete: Params(surface, pygame)
        - surface : Tuple(int, int) taille Longueur x Largeur en pixel
        - pygame : add pygame as property
      Methode:
        Procedure :
          - config(name) : init pygame
            - name : String
          - exit : fermee le jeux

      Détail methods:
        config : initialise une fenetre pygame
        exit : permet de gere la sortie
```

## 7. Menu

Intro: Il s'agit du menu

```
    Class Menu(Affichage):
      Propriete: Params(surface, pygame, Personnage)
        - button  : None
        - display : String
        - changed : Bool
        - pygame = pygame
        - Personnage : Blocks
          - surface : Tuple(int, int) taille Longueur x Largeur en pixel
          - pygame : add pygame as property

      Methode:
        Procedure:
          - init(Array)
          - started
          - game
          - controller
          - run

      Détail methods:
        init : initialisation des variable du jeux and run config
        started: demmarer le menu du jeux
        controller : assure la redirection entre le jeux et menu
        run: Gere le click du boutton du menu du jeux
        game :  Lancer la scene de jeux
        drawBlock : Affiche un block sur la scene selon des coordonnées
        moveSceneTop: Deplace la scene du jeux vers le haut et
        permet aussi de generer un nouveau tableau + niveau

        config : initialise une fenetre pygame
        exit : permet de gere la sortie
```

## 8. Main


## 9. Asset

We take `Asset` file on a github repo :
  - `https://github.com/Chessy-Cakes/mr-driller`

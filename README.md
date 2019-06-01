# MR Driller : 1DEV

## Jeux


News :  `Ajout d'un fichier Test.py permettant des tester rapidement un object ou une fonction. Afin de lancer un test suivre les indication enfin de chaques sous chapitre de documentation.`

### A faire

```

les "--" representent les propositions de changement

2. Les blocs : ✔
    compareBlock(Blocs) : compare si ce Blocs peut etre Lie a celui en parametre et renvoie un Boolean
    -- La fonction de fusion de blocs (comment representer la fusion, un block indepant ne connais pas la scene de jeux ?)
    -- La fonction de chute de blocs
      (juste l'info qui lui dit "je peux tomber", donc seulement l'info SI il peut tomber,
       non pas la chute en elle même, gérée par la scène)
      1. Un block neut peux pas savoir ou il est dans le tableau,
        sachant qu'il est independant du tableau, possibilité de deplace vers arrayBlock
    (Les blocks ont tous les memes propiete peut importe leur couleur seul la valeur de la propieté change)
    ou
    (On cree des class pour tous les differents block que l'on range dans un dossier sousBlocks)
    - Les différents blocs de couleurs / propriétés différentes
    - les blocs de crystal (décrits dans le sujet)
    - Les blocs blancs
    - Les blocs marrons
2.3 delBlock: ✔
    - Faire une fonction "destruction de blocs"
2.4 generateRandomBlock()
    - Cette procedure de genere aleatoirement des Block
3. Completer Personnage :
    - ajout de la fonction de drill
    - fonction mouvements (Avec les spécificités)
    - objet à part =/= d'un bloc
5. ArrayBlock complete le tableau avec les bonne proportionnalite:
    - faire en sorte que la difficulté puisse etre changée en fonction de l'avancée dans le jeu (le niveau)
    - Update : faire descandre les blocs qd il y a des espaces vide
      (en gros gravité, besoin d'un check si un espace vide est en dessous d'un bloc)
    - Chute : En fonction de coordonné dire si un block peut descendre ou non
    - Lie : Renvoie true si un block peut etre lie a un autre
    - getBlockLie : Retourne un tableau de block selon le block passer en parametre
    - addBlockLie : Ajoute au tableau de block lie une liste de block
                    relie selon lie et compareBlock dans Block
    - popBlockLie : qui suprime tous les block lie du tableau
6 . Fenetre:
    - Il s'agit uniquement d'une page blanche mere du menu et de la scene de jeu
    - Simple affichage vide pygame page blanche
7. Scene:
  Affichage provenant de fenetre
    - Separée en 2 partie sur un ecran scindé "jeu" et "information relative au jeu" (score,
      air restant, vie restantes, niveau actuel, option pause?)
    - Utilliser affichage pour créer la scène grapgiquement (init de la page blanche)
    - Methode permettant de generer graphiquement un scene en fonction d'un tableau (idem qu'au dessus non?) +
      qui relie les infos prises dans la scène de jeu pour y appliquer des sprites (faire en sortes qui si cette
      fonction voit qu'il y a un bloc rouge en [x,y] elle affiche un bloc rouge à cet endroit)
    - affiche l'etat de la scene, donc un tableau qui traduit les positions / les couleurs / etc... ce qu'il se passe dans le jeu en gros.
8. Menu:
  Affichage provenant de fenetre
9. Stucture :
    - Init un tableau de block random, dont la proportionnalité peut être changée facilement en fonction du level.
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
        - Personnage : Blocks
          - surface : Tuple(int, int) taille Longueur x Largeur en pixel
          - pygame : add pygame as property

      Methode:
        Procedure:
          - controller
          - started
          - game(Array)

      Détail methods:
        controller : assure la redirection entre le jeux et menu
        game : initialisée la scene de jeux graphique en fonction d'un tableau
        started: afficher le menu
        config : initialise une fenetre pygame
        exit : permet de gere la sortie
```


## 8. main.py

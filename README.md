# MR Driller : 1DEV

## Jeux


News :  `Ajout d'un fichier Test.py permettant des tester rapidement un object ou une fonction. Afin de lancer un test suivre les indication enfin de chaques sous chapitre de documentation.`

### A faire

ArrayBlock les Blocks devront tomber:
  - Object : Ajouter aussi des espaces blancs aux tableaux dans le jeux
  - Stucture : mettre a jour la position des blocks



### 1. Creation des Blocks ✔

Into : Un block est un Object ayant une couleur, un nombre de vie, une position, une valeur reflettant sa capacité a pourvoir fusionner avec un autre block.

```
   Class Block:
      Propriete && Parametre:
        - merge : Bool
        - Couleur : String
        - Vie : Int
        - Position : Array<Int,Int>
            init [x,y]
      Methode:
        function:
        - isDead : Bool
        - nearOf : Array<Int, Int>
        - Delete : Bool
```

test : `python3 Test.py Block`

#### Methods
```
  isDead : Si le block est vivant
  nearOf : Renvoie uniquement les coordonne des block aux alentours
           Remarque : un block ne peut avoir des coordonne où x < 0 ou x > n et y < 0 ou y > n
  Delete : Renvoie true si l'object a bien ete supprimer
```

### 1.1. Creation de la fonction getRandomColor() ✔

Intro: Cette fonction renvoie une couleur aleatoirement selon une certaine proportionalité

```
  @return: Dict {
      "color" : String,
      "Special" : Bool
  }
```

test : `python3 Test.py getRandomColor`

### 1.2. Creation de la function createGoodBlock() ✔

Intro: En fonction de la couleur du block on cree un block avec des proprieté pouvant par example etre specifique

```
  @return : Block()
```

test : `python3 Test.py createGoodBlock`

## ArrayBlock ✔

Intro: Il s'agit d'un tableau composé de Block

```
   Class ArrayBlock:
      Propriete et Params: (n, m)
        - blocks : Array<Block>
            init [] de taille n x m
      Methode:
        function:
          - getBlock([x,y])
```

test : `python3 Test.py ArrayBlock`

#### Methods
```
  getBlock([x,y]): Retourne un blocks selon les coordonne d'un tableau [x,y]
```

# Constraint

### Contrainte principal

#### Blocks

Into : `Les block qui sont emporté par la gravité fusionne avec les block adjacent si il sont de la meme couleur et sans arreter dans leur chute`

-Qd un block est `detruit` ses voisin de m couleurs le sont aussi
-si 4 block fusionnent ils `disparaissent`

-Les Marrons : `5 coup` pour disparaitre et doit etre `perce un a un`.
Recupere les proprite d'un block classique une fois emporte par la gravite

-Les blancs: ils ne fusionnent pas avec les block de la meme couleur

-les crystaux : ils ont une courte duree de vie avant de disparaitre


#### Personnage

-Deplacement : `droite gauche`
-Score : `Augmente a cheque Block fore, avec des capsule d'aire et en terminant un niveau`
-Air : `Guain ou paire de ressource Air`
        `Capsule : +20% air`
-Vie : `Guain ou Perte`
-Si l'alimentation en air tombe à zéro pour cent ou si le foreur est écrasé par un bloc qui tombe, le joueur perd une vie et redémarre à la même profondeur avec une alimentation en air complète.
Game over:
-Lorsque le joueur perd ses trois vies, la partie est terminée

#### Fin de Jeux

Win:
  -Il gagne s'il atteint tous les niveaux.


## Fonctionalité du jeu:
    Level:
    -Le jeu comprend 10 level
    -la profondeur du jeu augmente au fur et a mesure que le niveau est eleve
    -diminution du nombre de capsule d'aire plus le niveau est eleve
    -les types de block sont genere aleatoirement
    Score:
    -Afficher le score du joueur max deja obtenue
    Pause:
    -Le joueur doit pouvoir suspendre une partie en cours

# Git

## HELP HOW TO USE GIT

```

General command to use before do anything

- `git add .` : afin d'ajouter a git toute nos modification
- `git commit -m 'message'` : marquer par une note chaque modification

Pousser un projet

- `git push origin` : ajouter son code

OU

Recuperer les info sur la branch master

- `git fetch origin` : Recuperer le dossier distant
- `git merge origin/master` : Fusionner les repertoire


```

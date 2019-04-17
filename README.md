# MR Driller : 1DEV

## Jeux

### 1. Creation des Blocks

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
```

#### Methods
  isDead : Si le block est vivant
  nearOf : Renvoie uniquement les coordonne des block aux alentours
  -------- Remarque : un block ne peut avoir des coordonne où x < 0 ou x > n et y < 0 ou y > n

### 1.1. Creation de la fonction getRandomColor()

Intro: Cette fonction renvoie une couleur aleatoirement selon une certaine proportionalité

```
  @return: Dict {
      "color" : String,
      "Special" : Bool
  }
```

test : `python3 getRandomColor.py`

### 1.2. Creation de la function createGoodBlock()

Intro: En fonction de la couleur du block on cree un block avec des proprieté pouvant par example etre specifique

```
  @return : Block()
```

## ArrayBlock

Intro: Il s'agit d'un tableau composé de Block

```
   Class ArrayBlock:
    Propriete:
      - blocks : Array<Block>
          init []
    Methode:
      function:
        - isBlock() : Bool
      procedure:
        - addBlock
```

#### Methods
  isBlock : Si l'element recuperer est bien un block
  addBlock : Ajouter un block au tableau 

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

    -Deplacement : si meme niveau gauche droite, sinon entraine vers le bas par la gravite

    Air:
    -Moins 1% air chaque seconde
    -Block Marrons : Moins 20% d'air d'un coup
    -Capsule : +20% air
    Score:
    -Chaque bloc foré ou disparu après la fusion apporte des points. Le joueur augmente également son score de collecter des capsules d'air. Il a enfin un bonus  après avoir terminé un niveau.
    Vie:
    -Si l'alimentation en air tombe à zéro pour cent ou si le foreur est écrasé par un bloc qui tombe, le joueur perd une vie
     et redémarre à la même profondeur avec une alimentation en air complète.
    Game over:
    -Lorsque le joueur perd ses trois vies, la partie est terminée
    Win:
    -Il gagne s'il atteint tous les niveaux.

  2. Fonctionalité du jeu:
    Level:
    -Le jeu comprend 10 level
    -la profondeur du jeu augmente au fur et a mesure que le niveau est eleve
    -diminution du nombre de capsule d'aire plus le niveau est eleve
    -les types de block sont genere aleatoirement
    Score:
    -Afficher le score du joueur max deja obtenue
    Pause:
    -Le joueur doit pouvoir suspendre une partie en cours


```

## HELP HOW TO USE GIT

### General command to use before do anything

- `git add .` : afin d'ajouter a git toute nos modification
- `git commit -m 'message'` : marquer par une note chaque modification

#### Pousser un projet

- `git push origin` : ajouter son code

### OU

### Recuperer les info sur la branch master

- `git fetch origin` : Recuperer le dossier distant
- `git merge origin/master` : Fusionner les repertoire

m# MR Driller : 1DEV

## HOW USE GIT

### General command to use before do anything

- `git add .` : afin d'ajouter a git toute nos modification
- `git commit -m 'message'` : marquer par une note chaque modification

#### Pousser un projet

- `git push origin` : ajouter son code

### OU

### Recuperer les info sur la branch master

- `git fetch origin` : Recuperer le dossier distant
- `git merge origin/master` : Fusionner les repertoire

## Requirement

- `Create class Perso`
- `Create class Block`
- `Create an AssemblyBlock`
- `Create class Fenetre`
- `Create class Arme`

## Constraint

- FR :
```
  1. Contrainte principal
    Deplacement : si meme niveau gauche droite, sinon entraine vers le bas par la gravite
    Block:
    -si un block voisin d'autre block de la meme couleur est perce ceci son perce aussi, tous les autres block subissent la gravite
     Les block qui sont emporté par la gravité fusionne avec les block adjacent si il sont de la meme couleur et son arreter dans leur chute
     si 4 block fusionnent ils disparaissent
    -Les Marrons : 5 coup pour disparaitre et doit etre perce un a un. Cependant il fusionne apres sa chute avec le proprite d'un block classique
    -Les blancs: ils ne fusionnent pas avec les block de la meme couleur
    -les crystaux : ils ont une courte duree de vie avant de disparaitre
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

## Comment resoudre le problem



## Class assumption

gravity
score

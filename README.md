# MR Driller : 1DEV

## Jeux


News :  `Ajout d'un fichier Test.py permettant des tester rapidement un object ou une fonction. Afin de lancer un test suivre les indication enfin de chaques sous chapitre de documentation.`

### A faire

```
1. Completé Personnage :
  - ajout de la fonction de drill
  - ...
2. Affichage cree un Base d'affichage espace blanc
3. ArrayBlock complete le tableau avec les bonne proportionnalite:
  - Object : Ajouter aussi des espaces blancs aux tableaux dans le jeux
  - Stucture : mettre a jour la position des blocks
  - Update : faire descandre les blocs qd il y a des espaces vide
  - ...
4. Utilisé l'affichage pour cree une scene separe en 2 partie
   d'un cote le jeux et de l'autre les info relative a l'evolution du
   joueur dans le jeux
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
       function:
         - getBlock([x,y])
         - isDead : Bool
         - nearOf : Array<Int, Int>
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

## 5. ArrayBlock ✔

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

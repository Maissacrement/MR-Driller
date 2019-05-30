# MR Driller : 1DEV

## Jeux


News :  `Ajout d'un fichier Test.py permettant des tester rapidement un object ou une fonction. Afin de lancer un test suivre les indication enfin de chaques sous chapitre de documentation.`

### A faire

```
1. Completer Personnage :
    - ajout de la fonction de drill
    - fonction mouvements (Avec les spécificités)
    - objet à part =/= d'un bloc
2. Random proportionalité et block:
    - Object : Ajouter aussi des espaces blancs aux tableaux dans le jeu
    - Faire une fonction "destruction de blocs"
3. ArrayBlock complete le tableau avec les bonne proportionnalite:
    - faire en sorte que la difficulté puisse etre changée en fonction de l'avancée dans le jeu (le niveau)
    - Update : faire descandre les blocs qd il y a des espaces vide (en gros gravité, besoin d'un check si un espace vide est en dessous d'un bloc)
4 . Affichage: 
    - Simple affichage vide pygame page blanche
    - Fonction qui relie les infos prises dans la scène de jeu pour y appliquer des sprites (faire en sortes qui si 
    cette fonction voit qu'il y a un bloc rouge en [x,y] elle affiche un bloc rouge à cet endroit)
5. Scene:
    - Separée en 2 partie sur un ecran scindé "jeu" et "information relative au jeu" (score,
      air restant, vie restantes, niveau actuel, option pause?)
    - Utilliser affichage pour créer la scène grapgiquement
    - Methode permettant de generer graphiquement un scene en fonction d'un tableau (idem qu'au dessus non?)
    - affiche l'etat de la scene, donc un tableau qui traduit les positions / les couleurs / etc... ce qu'il se passe dans le jeu en gros.
5. Stucture : 
    - Init un tableau de block random, dont la proportionnalité peut être changée facilement en fonction du level.
    - Faire des fonctions pour chaque règle de jeu : 
        -La fusion des blocs quand 3 ou plus
        -la destruction des blocs quand 3 ou plus
        -La chute des blocs
        -La mort quand plus d'air
        -Le game over quand plus de vie
        -la Mort quand écrasé par un bloc
        -La Pause!
6. Les blocs :
    - Les différents blocs de couleurs / propriétés différentes
    - La fonction de fusion de blocs
    - La fonction de chute de blocs (juste l'info qui lui dit "je peux tomber", donc seulement l'info SI il peut tomber, non pas la chute en elle même, gérée par la scène)
    - les blocs de crystal (décrits dans le sujet)
    - Les blocs blancs
    - Les blocs marrons
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
  isDead : Si le bloc est vivant
  nearOf : Renvoie uniquement les coordonnées des blocs aux alentours
           Remarque : un block ne peut avoir des coordonnées où x < 0 ou x > n et y < 0 ou y > n
  Delete : Renvoie true si l'object a bien été supprimé
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

GAME-NAME : Bomberman
AUTHOR : Samyak Jain (20161083, UG-2)

####################################################

REQUIREMENTS:

1. python/python3 compiler
2. python-termcolor module

####################################################

ENTITIES:

1. Wall : ####
          ####

2. Bricks : ////
            ////

3. Bomberman : BBBB
               BBBB

4. Enemy : EEEE
           EEEE

5. Bomb : [NN]
          [NN] where N is countdown number.

6. Explosion : ^^^^
               ^^^^

####################################################

INSTRUCTIONS :

1. To Run the game enter the following line :

   python/python3 game.py

2. Controls:

   W : Move Up
   A : Move Left
   S : Move Down
   D : Move Right
   B : Plant Bomb
   Q : Quit The Game

3. You have 3 lives and unlimited Bombs and 3 levels to play.

4. You lose a life if you get caught in an explosion or if an enemy kills you.

5. Game is over when you lose all the 3 lives.

6. You level up if you kill all Enemies using your bombs in a particular level.

7. Exploding a brick will fetch you 20 points.

8. Killing an enemy will fetch you 100 points.

9. Each level number of bricks and enemies increases.

####################################################


BONUS FEATURES IMPLEMENTED :

1. Different color code for different entities within the game.

2. Bomb countdown (3 seconds) to explosion displayed.

3. 3 levels are implemented

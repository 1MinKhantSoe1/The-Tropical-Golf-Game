# The-Tropical-Golf-Game

This is a Python program for a game of Tropical Golf. The player will be attempting to get the ball in the hole using the least amount of swings.

    The rules and gameplay for the program are as follows:
      o The game asks for the player’s name, then welcomes the player, the numerical value of par, 
      the distance to the hole, and then displays the menu
      o The main menu displays 3 options “Instructions”, “Play Game”, and “Quit”
      o If the player chooses “I” the instructions are displayed
      o If the player chooses “P” the game is played:
        ▪ The ball starts at the distance to the hole specified by the player
        ▪ The player chooses one of three clubs, each of which hits a different average distance
      ▪ Every hit travels directly towards the hole in a straight line (this is a simple golf game, 
      we’re only playing in 2D)
        ▪ Distance of ball travel after a hit are only whole numbers (125, 250, etc)
        ▪ Once the ball is in the hole the player is told how many swings it took and whether 
      they are over or under par
        • ‘Par’ is the estimate of how many swings a game should take
        ▪ The player may use as many swings as is necessary to get the ball in the hole
      o After every menu choice OTHER than ‘Q’ the menu is displayed again.
      o Once the player enters “Q” the game thanks the player by name and says goodbye

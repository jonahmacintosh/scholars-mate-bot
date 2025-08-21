# scholars-mate-bot
a simple chess bot that plays scholars mate

## features
-the bot will try to play e4, Qh5, Bc4, Qxf7++
-if at any point those moves aren't legal, or:
-if when it plays Qxf7 the game doesn't end to checkmate:
-the bot will continue playing completely random legal moves until the game is over
-then, the game will be saved to a PGN file 

### versions
-the first version of this bot can play against you
-the second version will go against a bot who plays completely random moves

### performance
-in 7 simulated matches against the random moves bot, the scholarsbot:
-drew 6 times via 50 move rule
-won once via scholarsmate
-average accuracy: 31.3%
-suprsingly, the bot had the lowest accuracy on the game it won, at 12%

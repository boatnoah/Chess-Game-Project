CHESS GAME PROJECT
------------
#This project is my initial attempt at creating a fully functional chess game. This first version will include the basic rules and movements of chess, such as piece movement, capturing, and checkmating --- 5/14/23

#Added board (prints and updates board), piece (added a pawn class that validates its moves), const files  --- 5/15/23

#Added valid moves for rook. --- 5/16/23

#Added valid moves for queen, bishop, knight --- 5/17/23

#Added a main file more, functionality, a working game --- 5/22/23

#Added complete functionality to all pieces --- 5/26/23

#Added checks and check mate --- 6/1/23

#Improved checkmates --- 6/2/23

#Reworked checkmates --- 6/4/23

Challenges
------------
The main challenges I encountered while developing this project were implementing the functionality for checks, checkmates, and pinned pieces. The complexity lies in accurately determining whether a player's king is under threat and identifying a checkmate scenario. Initially, I had the idea of scanning through the vision of the king in check to detect any attacking pieces. However, this approach proved cumbersome and failed to detect knights due to their irregular movement. To overcome this challenge, I implemented a method for each piece that generates a list of legal moves based on the current state of the board. By checking if the opponent's king is present in any of these legal moves, I could simplify the process of detecting checks. Ensuring that a player's move choice doesn't put them in check was something to consider as well. To achieve this, I created a test board method that deep copies the board, objects, and the hashmap holding the locations of the white and black pieces. This allowed me to simulate scenarios in the background and determine checks without modifying the working game. This method proved valuable in determining checkmates and resolving issues related to pinned pieces because each move that the player inputs can be tested before displaying it onto the real board. This ultimately maintained the validity of each move. This approach helped in implementing checks effectively. With the checks in place, developing checkmates simply involved testing all possible moves on the king's side to see if any of them would put the player out of check.

Limitations of the game
------------
As of 6/4/23 this game does not have:
- Pawn promotions
- En Passant 
- Does not detect stalemates
- Possible edge cases not considered or forseen.
- no UI/UX (termial game)


How to Play:
Played locally on the terminal where it takes text input to choose and move pieces using alegabraic notation.
EX:
- Select a white piece: e2
- Select a position to move to: e4

- Select a black piece: e7
- Select a position to move to: e5



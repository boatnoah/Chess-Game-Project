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
The main challenges I encountered while developing this project was implementing the checks, checkmates, and pin pieces functionality. The complexity lies in accurately determining whether a player's king is under threat and identifying a checkmate scenario. My original idea was to find the king that is in check and scan through the vision of the king and see if there was any attack pieces. The issue with this idea is that it fails to detect knights due to its irregular movement and detecting that was complex and cumbersome. The idea that I ended up implenting was to create a method for each of the pieces that generates a list of legal moves in the current state of the board. Using this list I can simply check if the king is in any of the legal moves of the opposite pieces. This simplifies the process of finding checks. After determining if a player is in check, ensuring that the players move choice still didn't put them in check was important. Creating a test board method that deep copies the board, the objects, and the hashmap that holds the location of the white and black pieces. With this copy, it can easily play out sceneraios in the background and determine checks without updating the working game. This method can also be used to determine checkmates and resolves my issues of pinned pieces. Ensuring that every move is valid and does not put the player in check was very resource in this project. For example if there are "legal moves" for a piece that the player chose it can play those legal moves and determine if these particular set of moves puts the player in check. With having checks working developing checkmates was simply to test all the moves on king's side and seeing if any of them puts the player out of check.

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
Select a white piece: e2
Select a position to move to: e4

Select a black piece: e7
Select a position to move to: e5



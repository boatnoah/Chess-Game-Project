#display and update the board
from const import *

class Board:
     
#display the board
    def display_board(self):
        print("     a    b    c    d    e    f    g    h")                                       
        print("   -----------------------------------------") 
        j = 8          
        for i, row in enumerate(board, 1):
            print(end=str(j) + "    ")
            j -= 1
            for col in row:
                print(col, end="    ")
            print()
        print("   -----------------------------------------")                  
        print("     a    b    c    d    e    f    g    h")
        print()
        
        
           
#updates board with new piece     
    def update_board(self, position: str, position2move: str):
        current_position = algebraic_notation[position] 
        position_to_move = algebraic_notation[position2move]
        global board
        
        board[position_to_move[0]][position_to_move[1]] = board[current_position[0]][current_position[1]]
        board[current_position[0]][current_position[1]] = "-"
        
       

        




        
        
        
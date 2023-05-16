#display and update the board
import const

class Board:
     
    def __init__(self):
       self.board = [
    ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"],
    ["♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟"],
    ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"]
    ]
   

        

#display the board
    def display_board(self):
        print("     a    b    c    d    e    f    g    h")                                       
        print("   -----------------------------------------")                  
        for i, row in enumerate(self.board, 1):
            print(end=str(i) + "    ")
            for col in row:
                print(col, end="    ")
            print()
        print("   -----------------------------------------")                  
        print("     a    b    c    d    e    f    g    h")
        print()
        
        
           
#updates board with new piece     
    def update_board(self, position: str, position2move: str):
        current_position = self.algebraic_notation[position] 
        position_to_move = self.algebraic_notation[position2move]
        
        self.board[position_to_move[0]][position_to_move[1]] = self.board[current_position[0]][current_position[1]]
        self.board[current_position[0]][current_position[1]] = "-"
        
        
        
        
     
        
        
        




        
        
        
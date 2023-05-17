from const import *
import math
class Piece:
    def __init__(self, color: str, position: str):
        self.color = color
        self.position = algebraic_notation[position]
        self.is_taken = False
        self.is_pinned = False
    
    def check_is_pinned(self, position: str):
        x = algebraic_notation[position]
        
        
        if self.color == "white":
            if board[x[0] + 1][x[1]] == "♚":
                self.is_pinned = True
            else:
                self.is_pinned = False
        else:
            if board[x[0] - 1][x[1]] == "♔":
                self.is_pinned = True
            else:
                self.is_pinned = False
    
    def is_king_in_check(self, kingposition: str):
        k_current_position = current_position["king"][self.color][kingposition][0]
        k_current_position = algebraic_notation[k_current_position]
        
        #check the king's vision and find if it detects any enemy piece
        for i in range(k_current_position[0]):
            if board[k_current_position[0] - i][k_current_position[1]] != "-":
                if board[k_current_position[0] - i][k_current_position[1]] == "♚":
                    return True
                else:
                    break
        
        
        
             
                
                
        
        
    
class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.move_two_spaces = True
    
    def is_valid_move(self, position: list, position2move: list):
        x = algebraic_notation[position]
        y = algebraic_notation[position2move]
        diff = [abs(x[0] - y[0]), abs(x[1] - y[1])]
        
        if diff != [1, 0] and diff != [1, 1]:
            if diff == [2, 0] and self.move_two_spaces:
                self.move_two_spaces = False
                return True
            else:
                return False
        else:
            if board[y[0]][y[1]] != "-":
                if diff[0] == 1 and diff[1] == 0:
                    return False
                else:
                    if self.is_pinned:
                        return False
                    return True
            else:
                if diff[0] == 1 and diff[1] == 1:
                    return False
                else:
                    return True
            
             
    def move(self, position: str, position2move: str):
        self.current_position["pawn"][self.color][position] = position2move
        self.moves_played.append(position2move)
        
    
    def capture(self):
        pass
    
    
        
class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        
    def is_valid_move(self, position, position2move):
        x = algebraic_notation[position]
        y = algebraic_notation[position2move]
        #check if position2move is a friendly piece if it is return false
        if self.color == "white":
            if board[y[0]][y[1]] in white_piceces:
                return False
        else:
            if board[y[0]][y[1]] in black_pieces:
                return False
        #check the position of where the player wants to move and see if there is no piece in the way
        #if there is a piece in the way, return False (vertical)
        if x[0] < y[0]:
            for i in range(x[0]+1, y[0]):
                if board[i][x[1]] != "-":
                    return False
        else:
            for i in range(y[0]+1, x[0]):
                if board[i][x[1]] != "-":
                    return False
        
        #horizontal
        if x[1] < y[1]:
            for i in range(x[1]+1, y[1]):
                if board[x[0]][i] != "-":
                    return False
        else:
            for i in range(y[1]+1, x[1]):
                if board[x[0]][i] != "-":
                    return False
        
        
        
        diff = [abs(x[0] - y[0]), abs(x[1] - y[1])]
        if diff[1] == 0 or diff[0] == 0:
            if self.is_pinned:
                return False
            return True
            
        else: 
            return False
        
        
        
rook = Rook("white", "a1")
print(rook.is_valid_move("e4", "c6"))



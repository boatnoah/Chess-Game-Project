from const import *
import math



class Piece:
    def __init__(self, color: str, position: str):
        self.color = color
        self.position = position
        self.is_pinned = False
    
    
    def update_piece_position(self, position: str):
        self.position = position
        
    def check_if_pin(self):
        pass
    
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
            
             

        
class Knight(Piece):
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
            
        diff = [abs(x[0] - y[0]), abs(x[1] - y[1])]
        
        #differnce should [2,1] or [1,2]
        if diff == [2,1] or diff == [1,2]:
            return True
        return False
    
            
    
    
        
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
        
class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        
    def is_valid_move(self, position, position2move):
        x = algebraic_notation[position]
        y = algebraic_notation[position2move]
        
        #check if the position2move is a friendly piece if it is return false
        if self.color == "white":
            if board[y[0]][y[1]] in white_piceces:
                return False
        else:
            if board[y[0]][y[1]] in black_pieces:
                return False
            
        #check if there is any piece in the way between the two positions if so return false
        if x[0] < y[0]:
            if x[1] < y[1]:
                for i in range(x[0]+1, y[0]):
                    for j in range(x[1]+1, y[1]):
                        if board[i][j] != "-":
                            return False
            else:
                for i in range(x[0]+1, y[0]):
                    for j in range(y[1]+1, x[1]):
                        if board[i][j] != "-":
                            return False     
        else:
            if x[1] < y[1]:
                for i in range(y[0]+1, x[0]):
                    for j in range(x[1]+1, y[1]):
                        if board[i][j] != "-":
                            return False
            else:
                for i in range(y[0]+1, x[0]):
                    for j in range(y[1]+1, x[1]):
                        if board[i][j] != "-":
                            return False
                        
        diff = [abs(x[0] - y[0]), abs(x[1] - y[1])] 
        
        #check if the difference list and check if index 0 and 1 are the same
        """The reason why we are checking if index 0 and 1 are the same is because all valid moves of a bishop have the same difference no matter how long."""
        if diff[0] == diff[1] and self.is_pinned != True:
            return True
        return False  
    
    
    
    
class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        
    def is_valid_move(self, position, position2move):
        x = algebraic_notation[position]
        y = algebraic_notation[position2move]
        
        #check if the position2move is a friendly piece if it is return false
        if self.color == "white":
            if board[y[0]][y[1]] in white_piceces:
                return False
        else:
            if board[y[0]][y[1]] in black_pieces:
                return False
        
        #reuse logic from rook and bishop
        #vertical
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
                
                
        #diagonal
        if x[0] < y[0]:
            if x[1] < y[1]:
                for i in range(x[0]+1, y[0]):
                    for j in range(x[1]+1, y[1]):
                        if board[i][j] != "-":
                            return False
            else:
                for i in range(x[0]+1, y[0]):
                    for j in range(y[1]+1, x[1]):
                        if board[i][j] != "-":
                            return False     
        else:
            if x[1] < y[1]:
                for i in range(y[0]+1, x[0]):
                    for j in range(x[1]+1, y[1]):
                        if board[i][j] != "-":
                            return False
            else:
                for i in range(y[0]+1, x[0]):
                    for j in range(y[1]+1, x[1]):
                        if board[i][j] != "-":
                            return False
        diff = [abs(x[0] - y[0]), abs(x[1] - y[1])]
        
        if diff[0] == diff[1] or diff[0] == 0 or diff[1] == 0 and self.is_pinned != True:
            return True
        return False
    
class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.is_in_check = False
        self.can_castle = False
    
    def is_valid_move(self, position, position2move):
        x = algebraic_notation[position]
        y = algebraic_notation[position2move]
        diff = [abs(x[0] - y[0]), abs(x[1] - y[1])]
        #check if position2move is a friendly piece if it is return false
        if self.color == "white":
            if board[y[0]][y[1]] in white_piceces:
                return False
        else:
            if board[y[0]][y[1]] in black_pieces:
                return False
        
        
        #check if the distance is from x to y is [1, 0] or [0, 1] or [1, 1]      
        if diff == [1, 1] or diff == [1, 0] or diff == [0, 1]:
            return True
        return False






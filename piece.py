from const import *
import math



class Piece:
    def __init__(self, color: str, position: str, piece_type: str):
        self.color = color
        self.position = position
        self.is_in_check = False
        self.piece_type = piece_type
    
    def update_piece_position(self, position: str):
        temp = self.position
        self.position = position
        if self.color == "white": 
            del location_of_white[temp]
            location_of_white[self.position] = self.piece_type 
            
        else:
            del location_of_black[temp]
            location_of_black[self.position] = self.piece_type
        
    
        
        
    
class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position, "pawn")
        self.move_two_spaces = True
    
    def is_valid_move(self, position: list, position2move: list):
        global board
        
        x = algebraic_notation[position]
        y = algebraic_notation[position2move]
        diff = [x[0] - y[0], x[1] - y[1]]
        if self.color == "white":
            if diff == [1, 0]:
                if board[y[0]][y[1]] != "-":
                    return False
                else:
                    self.move_two_spaces = False
                    
                    return True
            elif diff == [1, -1] or diff == [1, 1]:
                if board[y[0]][y[1]] in black_pieces:
                    self.move_two_spaces = False
                    
                    return True
                else:
                    return False
            else:
                if diff == [2, 0] and self.move_two_spaces:
                    self.move_two_spaces = False
                    return True
                return False
        else:
            if diff == [-1, 0]:
                if board[y[0]][y[1]] != "-":
                    return False
                else:
                    self.move_two_spaces = False   
                    return True
            elif diff == [-1, 1] or diff == [-1, -1]:
                if board[y[0]][y[1]] in white_piceces:
                    self.move_two_spaces = False   
                    return True
                else:
                    self.move_two_spaces = False   
                    return False
            else:
                if diff == [-2, 0] and self.move_two_spaces:
                    self.move_two_spaces = False
                    return True 
                return False
            
        
            
             

        
class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, position, "knight")
        
    def is_valid_move(self, position, position2move):
        global board
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
        super().__init__(color, position, "rook")
        
    def is_valid_move(self, position, position2move):
        global board
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
            return True
            
        else: 
            return False
        
class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, position, "bishop")
        
    def is_valid_move(self, position, position2move):
        global board
        x = algebraic_notation[position][:]
        y = algebraic_notation[position2move][:]
        
        #check if the position2move is a friendly piece if it is return false
        if self.color == "white":
            if board[y[0]][y[1]] in white_piceces:
                return False
        else:
            if board[y[0]][y[1]] in black_pieces:
                return False
            
        diff = [abs(x[0] - y[0]), abs(x[1] - y[1])]
        if diff[0] == diff[1]:
            #diagonal down right 
            while x[0] < y[0] and x[1] < y[1]:
                x[0] += 1
                x[1] += 1
                
                if board[x[0]][x[1]] != "-" and x[0] != y[0] and x[1] != y[1]:
                    return False
                
            #diagonal down left  
            while x[0] < y[0] and x[1] > y[1]:
                x[0] += 1
                x[1] -= 1
                
                if board[x[0]][x[1]] != "-" and x[0] != y[0] and x[1] != y[1]:
                    return False
            
            #diagonal up right
            while x[0] > y[0] and x[1] < y[1]:
                x[0] -= 1
                x[1] += 1
                
                if board[x[0]][x[1]] != "-" and x[0] != y[0] and x[1] != y[1]:
                    print("here")
                    return False
            
            #diagnoal up left
            while x[0] > y[0] and x[1] > y[1]:
                x[0] -= 1
                x[1] -= 1
                
                if board[x[0]][x[1]] != "-" and x[0] != y[0] and x[1] != y[1]:
                    return False
            
            return True
                        
        else:
            return False
    
    
        """The reason why we are checking if index 0 and 1 are the same is because all valid moves of a bishop have the same difference no matter how long."""
          
    
    
    
    
class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(color, position, "queen")
        
    def is_valid_move(self, position, position2move):
        global board
        
        x = algebraic_notation[position][:]
        y = algebraic_notation[position2move][:]
    
        diff = [abs(x[0] - y[0]), abs(x[1] - y[1])]
        
        #check if the position2move is a friendly piece if it is return false
        if self.color == "white":
            if board[y[0]][y[1]] in white_piceces:
                return False
            elif diff == [1, 0] or diff == [0, 1] or diff == [1, 1]:
                return True
                
        elif self.color == "black":
            if board[y[0]][y[1]] in black_pieces:
                return False
            elif diff == [1, 0] or diff == [0, 1] or diff == [1, 1]:
                return True
            
        
        
        #up or down
        if diff[1] == 0:
            if x[0] < y[0]:
                for i in range(x[0]+1, y[0]):
                    if board[i][x[1]] != "-":
                        return False
            elif x[0] > y[0]:
                for i in range(y[0]+1, x[0]):
                    if board[i][x[1]] != "-":
                        return False       
            return True    
           
        elif diff[0] == 0:
            if x[1] < y[1]:
                for i in range(x[1]+1, y[1]):
                    if board[x[0]][i] != "-":
                        return False
            elif x[1] > y[1]:
                for i in range(y[1]+1, x[1]):
                    if board[x[0]][i] != "-":
                        return False
            return True    
                 
        elif diff[0] == diff[1]:
            if x[0] > y[0]:
                if x[1] > y[1]:
                    while x[0] != y[0] and x[1] != y[1]:
                        x[0] -= 1
                        x[1] -= 1
                        
                        if board[x[0]][x[1]] != "-" and x[0] != y[0] and x[1] != y[1]:
                            return False
    
                    
       
                    return True
                
                elif x[1] < y[1]:
                    while x[0] != y[0] and x[1] != y[1]:
                        x[0] -= 1
                        x[1] += 1
                        
                        if board[x[0]][x[1]] != "-" and x[0] != y[0] and x[1] != y[1]:
                            return False
                    
                    return True
                        
            elif x[0] < y[0]:
                if x[1] > y[1]:
                    while x[0] != y[0] and x[1] != y[1]:
                        x[0] += 1
                        x[1] -= 1
                        
                        if board[x[0]][x[1]] != "-" and x[0] != y[0] and x[1] != y[1]:
                            return False
                    
                    return True
                
                elif x[1] < y[1]:
                    while x[0] != y[0] and x[1] != y[1]:
                        x[0] += 1
                        x[1] += 1
                        
                        if board[x[0]][x[1]] != "-" and x[0] != y[0] and x[1] != y[1]:
                            return False
                    
                    return True
        else:
            return False
            
                        
        
    
    def is_attacking_king(self, king_position):
        global board
        x = algebraic_notation[self.position]
        y = algebraic_notation[king_position]
        
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
       
        if self.is_valid_move(self.position, king_position):
            return True
        else:
            return False        
        
    
class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position, "king")
        
    
    def is_valid_move(self, position, position2move):
        global board
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

    def can_castle(self, position2move):
        if self.position != "e1" and self.position != "e8":
            return False
        
        if position2move != "c1" and position2move != "g1" and position2move != "c8" and position2move != "g8":
            return False
        
        x = algebraic_notation[self.position]
        y = algebraic_notation[position2move]

        if position2move == "g1":
            r = algebraic_notation["h1"]
            if board[r[0]][r[1]] != "♖":
                return False
        elif position2move == "c1":
            r = algebraic_notation["a1"]
            if board[r[0]][r[1]] != "♖":
                return False
        elif position2move == "g8":
            r = algebraic_notation["h8"]
            if board[r[0]][r[1]] != "♜":
                return False
        elif position2move == "c8":
            r = algebraic_notation["a8"]
            if board[r[0]][r[1]] != "♜":
                return False
        
        if x[1] < r[1]:
            for i in range(x[1]+1, r[1]):
                if board[x[0]][i] != "-":
                    return False
        else:
            for i in range(r[1]+1, x[1]):
                if board[x[0]][i] != "-":
                    return False 
        
            
        if position2move == "g1":
            return [self.position, "g1", "h1", "f1"]
        elif position2move == "c1":
            return [self.position, "c1", "a1", "d1"]
        elif position2move == "g8":
            return [self.position, "g8", "h8", "f8"]
        elif position2move == "c8":
            return [self.position, "c8", "a8", "d8"]
        
        
        
        
                    

   
        
        
    








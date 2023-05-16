from const import *
import math
class Piece:
    def __init__(self, color: str, position: str):
        self.color = color
        self.position = algebraic_notation[position]
        self.is_taken = False
        self.is_pinned = False
        
    
    
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
    
    
        
    
p = Pawn("white", "e2")
print(p.is_valid_move("a2", "a4"))





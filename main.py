from board import Board
from const import *
from piece import *


class Game:
    game = Board()
    Wpawn1 = Pawn("white", "a2")
    Wpawn2 = Pawn("white", "b2")
    Wpawn3 = Pawn("white", "c2")
    Wpawn4 = Pawn("white", "d2")
    Wpawn5 = Pawn("white", "e2")
    Wpawn6 = Pawn("white", "f2")
    Wpawn7 = Pawn("white", "g2")
    Wpawn8 = Pawn("white", "h2")
    Wrook1 = Rook("white", "a1")
    Wrook2 = Rook("white", "h1")
    Wknight1 = Knight("white", "b1")
    Wknight2 = Knight("white", "g1")
    Wbishop1 = Bishop("white", "c1")
    Wbishop2 = Bishop("white", "f1")
    Wqueen = Queen("white", "d1")
    Wking = King("white", "e1")
    Bpawn1 = Pawn("black", "a7")
    Bpawn2 = Pawn("black", "b7")
    Bpawn3 = Pawn("black", "c7")
    Bpawn4 = Pawn("black", "d7")
    Bpawn5 = Pawn("black", "e7")
    Bpawn6 = Pawn("black", "f7")
    Bpawn7 = Pawn("black", "g7")
    Bpawn8 = Pawn("black", "h7")
    Brook1 = Rook("black", "a8")
    Brook2 = Rook("black", "h8")
    Bknight1 = Knight("black", "b8")
    Bknight2 = Knight("black", "g8")
    Bbishop1 = Bishop("black", "c8")
    Bbishop2 = Bishop("black", "f8")
    Bqueen = Queen("black", "d8")
    Bking = King("black", "e8")
    ALL_PIECES = [Wpawn1, Wpawn2, Wpawn3, Wpawn4, Wpawn5, Wpawn6, Wpawn7, Wpawn8, Wrook1, Wrook2, Wknight1, Wknight2, Wbishop1, Wbishop2, Wqueen, Wking, Bpawn1, Bpawn2, Bpawn3, Bpawn4, Bpawn5, Bpawn6, Bpawn7, Bpawn8, Brook1, Brook2, Bknight1, Bknight2, Bbishop1, Bbishop2, Bqueen, Bking]

    

    def __init__(self):
        self.turn = 0
        self.white = ""
        self.white2move = ""
        self.black = ""
        self.black2move = ""
    
    def validate_piece_choice(self, color: str):
        if color == "white":
            self.white = input("Select a white piece: ")
            while True:
                if self.white not in location_of_white:
                    print("Invalid input try again. vader")
                    self.white = input("Select a white piece: ")
                else:
                    break
        else:
            self.black = input("Select a black piece: ")
            while True:
                if self.black not in location_of_black:
                    print("Invalid input try again. clan ")
                    self.black = input("Select a black piece: ")
                else:
                    break 
            
        
    def validate_piece_move(self, color: str):
        if color == "white":
            self.white2move = input("Select a position to move to: ")
            while True:    
                if self.white2move in location_of_white or self.white2move not in algebraic_notation:
                    print("Invalid input try again. boba ")
                    self.white2move = input("Select a position to move to: ")
                else:
                    break
        else:
            self.black2move = input("Select a position to move to: ")
            while True:   
                if self.black2move in location_of_black or self.black2move not in algebraic_notation:
                    print("Invalid input try again. batman")
                    self.black2move = input("Select a position to move to: ")
                else:
                    break
            
    def turns(self):
        if self.turn % 2 == 0:
            self.validate_piece_choice("white")
            self.validate_piece_move("white")
                    
        else:
            self.validate_piece_choice("black")
            self.validate_piece_move("black")
            
            
                    
                    
                    
        
    def find_piece(self, piece):
        for p in self.ALL_PIECES:
            if p.position == piece:
                return p
        return None

    def move_piece(self):
        if self.turn % 2 == 0:
            w = self.find_piece(self.white)
            y = algebraic_notation[self.white2move]
            if w.is_valid_move(self.white, self.white2move):
               
                if board[y[0]][y[1]] != "-":
                    del location_of_black[self.white2move]
                    self.find_piece(self.white2move).position = "-"
                    
                    


                self.game.update_board(self.white, self.white2move)
                w.update_piece_position(self.white2move)
                return True
            else:   
                print("Invalid move try again.")
                return False
                        
        else:
            b = self.find_piece(self.black)
            y = algebraic_notation[self.black2move]
            if b.is_valid_move(self.black, self.black2move):
                if board[y[0]][y[1]] != "-":
                    del location_of_white[self.black2move]
                    self.find_piece(self.black2move).position = "-"
                    
                    
                   
                b.update_piece_position(self.black2move)
                self.game.update_board(self.black, self.black2move)
                return True
            else:  
                print("Invalid move try again.")
                return False
    
            
    def play(self):
        while True:
            self.game.display_board()
            self.turns()
            if self.move_piece():
                self.turn += 1
            
            
            
            
            
            
            
                
            
        
            
        
        
    

            
                
                
g = Game()
g.play()
        


        





    
    
from board import Board
from const import *
from piece import *
import copy



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
        
        return "Piece not found."
        

    def move_piece(self):
        if self.turn % 2 == 0:
            w = self.find_piece(self.white)
            y = algebraic_notation[self.white2move]
            if w.piece_type == "king":
                if w.is_valid_move(self.white, self.white2move):
                    if board[y[0]][y[1]] != "-":
                        del location_of_black[self.white2move]
                        self.find_piece(self.white2move).position = "-"
                        
                        
                    w.update_piece_position(self.white2move)
                    self.game.update_board(self.white, self.white2move)
                    return True
                else:   
                    boolean_or_list = w.can_castle(self.white2move)
                    if boolean_or_list == False:
                        print("Invalid move try again.")
                        return False 
                    else:
                        king = self.find_piece(self.white)
                        rook = self.find_piece(boolean_or_list[2])
                        king.update_piece_position(boolean_or_list[1])
                        rook.update_piece_position(boolean_or_list[3])
                        self.game.update_board(boolean_or_list[0], boolean_or_list[1])
                        self.game.update_board(boolean_or_list[2], boolean_or_list[3])
                        return True
                
            else: 
                if w.is_valid_move(self.white, self.white2move):
                    if w.piece_type == "pawn":
                        w.move_two_spaces = False
                        
                    if board[y[0]][y[1]] != "-":
                        del location_of_black[self.white2move]
                        self.find_piece(self.white2move).position = "-"
                    
                    w.update_piece_position(self.white2move)    
                    self.game.update_board(self.white, self.white2move)
                    return True
                else:   
                    print("Invalid move try again.")
                    return False                  
        else:
            b = self.find_piece(self.black)
            y = algebraic_notation[self.black2move]
            if b.piece_type == "king":
                if b.is_valid_move(self.black, self.black2move):
                    if board[y[0]][y[1]] != "-":
                        del location_of_white[self.black2move]
                        self.find_piece(self.black2move).position = "-"
                        
                        
                    
                    b.update_piece_position(self.black2move)
                    self.game.update_board(self.black, self.black2move)
                    return True
                else:
                    boolean_or_list = b.can_castle(self.black2move)
                    if boolean_or_list == False:
                        print("Invalid move try again.")
                        return False 
                    else:
                        king = self.find_piece(self.black)
                        rook = self.find_piece(boolean_or_list[2])
                        king.update_piece_position(boolean_or_list[1])
                        rook.update_piece_position(boolean_or_list[3])
                        self.game.update_board(boolean_or_list[0], boolean_or_list[1])
                        self.game.update_board(boolean_or_list[2], boolean_or_list[3])
                        return True
                        
            else:
                if b.is_valid_move(self.black, self.black2move):
                    if b.piece_type == "pawn":
                        b.move_two_spaces = False
                        
                    if board[y[0]][y[1]] != "-":
                        del location_of_white[self.black2move]
                        self.find_piece(self.black2move).position = "-"
                        
                        
                    
                    b.update_piece_position(self.black2move)
                    self.game.update_board(self.black, self.black2move)
                    return True
                else:  
                    print("Invalid move try again.")
                    return False
                
    def test_board(self, position, position2move):
        #the purpose of this function to play the scenario out on a copy board and see if the king is in check or not. This can also help determine checkmates for future use.
        copy_board = copy.deepcopy(board)
        copy_obj = copy.deepcopy(self.ALL_PIECES)
        copy_location_of_white = copy.deepcopy(location_of_white)
        copy_location_of_black = copy.deepcopy(location_of_black)
        
        #convert the algebraic notation to the index of the board
        current_position = algebraic_notation[position] 
        position_to_move = algebraic_notation[position2move]
        
        #update the copy board
        copy_board[position_to_move[0]][position_to_move[1]] = copy_board[current_position[0]][current_position[1]]
        copy_board[current_position[0]][current_position[1]] = "-"
        
        
        #update the copy object
        for p in copy_obj:
            if p.position == position:
                obj = p
                obj.update_piece_position_test(position2move, copy_location_of_white, copy_location_of_black)
                break
            
    
        #check if the king is in check
        if self.turn % 2 == 0:
            for p in copy_obj:
                if p.piece_type == "king" and p.color == "white":
                    copy_king = algebraic_notation[p.position]
                    break
                
            #find if any piece can attack the king
            for p in copy_obj:
                if p.color == "black":
                    temp = p.legal_moves_test(copy_board)
                    if copy_king in temp:
                        return False
            
            return True
        else:
            for p in copy_obj:
                if p.piece_type == "king" and p.color == "black":
                    copy_king = algebraic_notation[p.position]
                    break
                
            #find if any piece can attack the king
            for p in copy_obj:
                if p.color == "white":
                    temp = p.legal_moves_test(copy_board)
                    if copy_king in temp:
                        return False
            return True
        
                
            
            
        
        
        
        
            
            
            
                
       
        
    def is_check(self):
        if self.white != "" and self.black != "": 
            if self.turn % 2 == 0:
                curr_king_pos = algebraic_notation[self.Wking.position][:]
                
                for p in self.ALL_PIECES:
                    if p.color == "black":
                        if curr_king_pos in p.legal_moves():
                            return True
                return False
            
            else:
                curr_king_pos = algebraic_notation[self.Bking.position][:]
                for p in self.ALL_PIECES:
                    if p.color == "white":
                        if curr_king_pos in p.legal_moves():
                            return True
                return False
        else:
            return False

            
    def pace(self):
        self.game.display_board()
        self.turns()
        if self.move_piece():
            self.turn += 1           
          
            
    def checkmate(self):
        #check for legal moves of king and if there are none then check if any piece can block the check or take the piece that is checking the king
        if self.turn % 2 == 0:
           king = self.Wking
           white_moves = []
           black_moves = []
           for p in self.ALL_PIECES:
               if p.color == "white" and p.position != "-":
                   temp = p.legal_moves()
                   for i in temp:
                       white_moves.append(i)
               else:
                   if p.position != "-":
                       temp = p.legal_moves()
                       for i in temp:
                           black_moves.append(i)
                   
        else:
            king = self.Bking
            white_moves = []
            black_moves = []
            for p in self.ALL_PIECES:
               if p.color == "white" and p.position != "-":
                   temp = p.legal_moves()
                   for i in temp:
                       white_moves.append(i)
               else:
                   if p.position != "-":
                       temp = p.legal_moves()
                       for i in temp:
                           black_moves.append(i)
                     
    
        if len(king.legal_moves()) == 0:
            for m in white_moves:
                if m in black_moves:
                    return False
        return True
        
    def play(self):
        while True:
            self.pace()
            if self.is_check():
                if self.checkmate():
                    if self.turn % 2 == 0:
                        self.game.display_board()
                        print("CHECKMATE! BLACK WINS!")
                        quit()
                    else:
                        self.game.display_board()
                        print("CHECKMATE! WHITE WINS!")
                        quit()
                        
                print("CHECK")
                self.game.display_board()
                self.turns()
                while True:
                    if self.turn % 2 == 0:
                        if self.test_board(self.white, self.white2move):
                            if self.move_piece():
                                self.turn += 1
                                break
                            
                        else:
                            if self.checkmate():
                                print("CHECKMATE! BLACK WINS!")
                                quit()
                                
                            print("Invalid move try again.")
                            self.turns()
                    else:
                        if self.test_board(self.black, self.black2move):
                            if self.move_piece():
                                self.turn += 1
                                break
                        else:
                            if self.checkmate():
                                print("CHECKMATE! WHITE WINS!")
                                quit()
                                    
                            print("Invalid move try again.")
                            self.turns()
                            
                                
                            
                            
                            
                        
                    
            
                    
                    
                
                
                


            
            
            
            
   
                 
g = Game()
g.play()


        


        





    
    
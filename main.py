import chess
import random
import chess.pgn
from datetime import datetime

board = chess.Board()
game = chess.pgn.Game()
node = game
game.headers["White"] = "Player"
game.headers["Black"] = "Garfield Bot"
game.headers["Date"] = datetime.now().strftime("%Y.%m.%d")
game.headers["Event"] = "Garfield Bot vs. Player"

PIECE_VALUES = {
    chess.PAWN: 1, 
    chess.KNIGHT: 2.75,
    chess.BISHOP: 3.25,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 1000000,
}
def greedy_move(board):
    best_value = -1
    best_moves = []

    for move in board.legal_moves:
        if board.is_capture(move):
            captured_piece = board.piece_at(move.to_square)
            if captured_piece:
                value = PIECE_VALUES[captured_piece.piece_type]
                if value > best_value:
                    best_value = value
                    best_moves = [move]

                elif value == best_value:
                    best_moves.append(move)


    if best_moves:
        return random.choice(best_moves)
    else:
        return random.choice(list(board.legal_moves))
    

while not board.is_game_over():
    print(board)
    if board.turn == chess.WHITE:
        white_move = input("Your move: ")
        try:
            move = board.parse_san(white_move)
            if move in board.legal_moves:
                board.push(move)
                node = node.add_variation(move)
            else:
                print("ILLEGAL ILLEGAL ILLEGAL TRY AGAIN")
        except:
            print("Invalid notation, please try again.")

    else:
        move = greedy_move(board)
        print(f"Garfield Bot plays: {board.san(move)}")
        board.push(move)
        node = node.add_variation(move)
        

   
print(("GAME OVER, " + board.result()))
game.headers["Result"] = board.result()
print(board)

with open("garfield_bot_game.pgn", "w") as pgn:
    print(game, file = pgn)
print("Game saved as garfield_bot_game.pgn")
print(game)





import chess
import random
import chess.pgn
from datetime import datetime

board = chess.Board()
game = chess.pgn.Game()
game.headers["White"] = "ScholarBot"
game.headers["Black"] = "Player"
game.headers["Event"] = "Scholar's Mate Bot vs Player"
game.headers["Site"] = "?"
game.headers["Date"] = datetime.now().strftime("%Y.%m.%d")
game.headers["Round"] = "?" 
node = game
scholars_mate_moves = ["e2e4", "d1h5", "f1c4", "h5f7"]
move_index = 0

while not board.is_game_over():
    print(board.transform(chess.flip_vertical).transform(chess.flip_horizontal))
    print()

    if board.turn == chess.WHITE:
        if move_index < len(scholars_mate_moves):
            move_uci = scholars_mate_moves[move_index]
            move = chess.Move.from_uci(move_uci)
            
            if move in board.legal_moves:
                san_move = board.san(move)
                print(f"White plays: {san_move}")
                board.push(move)
                node = node.add_variation(move)
                move_index += 1
            
            else:
                print("White's plan is blocked! Generating random move:")
                move = random.choice(list(board.legal_moves))
                san_move = board.san(move)
                print(f"White plays: {san_move}")
                board.push(move)
                node = node.add_variation(move)

        else:
            move = random.choice(list(board.legal_moves))
            san_move = board.san(move)
            print(f"White plays: {san_move}")
            board.push(move)
            node = node.add_variation(move)

    #black's turn! (you)
    else:
        while True:
            your_move = input("Your move: ")
            try:
                move = board.parse_san(your_move) # this converts the SAN so the bot can read it
                if move in board.legal_moves:
                    board.push(move)
                    node = node.add_variation(move)
                    break

                else:
                    print("ILLEGAL MOVE, TRY AGAIN")
                
            except ValueError:
                print("Invalid move format. Please use SAN input (e.g., e4, Nf3, etc.)")






# Set the final result after the game is over
game.headers["Result"] = board.result()

with open("scholars_mate_game.pgn", "w") as pgn:
    print(game, file=pgn)
print("Game saved as scholars_mate_game.pgn")


print("\nFinal Position:")
print(board.transform(chess.flip_vertical).transform(chess.flip_horizontal))
print(f"Result: {board.result()}")

print()

print(game)

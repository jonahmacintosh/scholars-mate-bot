import chess
import random
import chess.pgn
from datetime import datetime

board = chess.Board()
game = chess.pgn.Game()
game.headers["White"] = "ScholarBot"
game.headers["Black"] = "RandomBot"
game.headers["Event"] = "Scholar's Mate Simulation"
game.headers["Site"] = "?"
game.headers["Date"] = datetime.now().strftime("%Y.%m.%d")
game.headers["Round"] = "?" 
node = game
scholars_mate_moves = ["e2e4", "d1h5", "f1c4", "h5f7"]
move_index = 0

while not board.is_game_over():
    print(board)
    print()

    if board.turn == chess.WHITE:
        if move_index < len(scholars_mate_moves):
            move_uci = scholars_mate_moves[move_index]
            move = chess.Move.from_uci(move_uci)
            
            if move in board.legal_moves:
                print(f"White plays: {move}")
                board.push(move)
                node = node.add_variation(move)
                move_index += 1
            
            else:
                print("White's plan is blocked! Generating random move:")
                move = random.choice(list(board.legal_moves))
                board.push(move)
                node = node.add_variation(move)

        else:
            move = random.choice(list(board.legal_moves))
            board.push(move)
            node = node.add_variation(move)

    else:
        move = random.choice(list(board.legal_moves))
        node = node.add_variation(move)
        board.push(move)


# Set the final result after the game is over
game.headers["Result"] = board.result()

with open("scholars_mate_game.pgn", "w") as pgn:
    print(game, file=pgn)
print("Game saved as scholars_mate_game.pgn")


print("\nFinal Position:")
print(board)
print(f"Result: {board.result()}")

print()

print(game)

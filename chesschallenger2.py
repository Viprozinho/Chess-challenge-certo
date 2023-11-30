import chess
from stockfish import Stockfish

def get_stockfish_move(board, stockfish_path='stockfish-windows-x86-64-avx2'):
    stockfish = Stockfish(stockfish_path)

    stockfish.set_fen_position(board.fen())
    best_move = stockfish.get_best_move()
    
    return chess.Move.from_uci(best_move)

def main():
    board = chess.Board()

    while not board.is_game_over():
        print(board)

        if board.turn == chess.WHITE:
            move_uci = input("Enter your move (in UCI format): ")
            move = chess.Move.from_uci(move_uci)

            if move in board.legal_moves:
                board.push(move)
            else:
                print("Invalid move. Try again.")
        else:
            ai_move = get_stockfish_move(board)
            board.push(ai_move)
            print(f"AI plays: {ai_move.uci()}")

    print("Game over!")
    print("Result: ", board.result())

if __name__ == "__main__":
    main()

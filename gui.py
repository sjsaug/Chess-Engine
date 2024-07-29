import arcade
from typing import Tuple

class Piece:
    Nothing = 0
    King = 1
    Pawn = 2
    Knight = 3
    Bishop = 4
    Rook = 5
    Queen = 6
    White = 8
    Black = 16

# Constants
SCREEN_WIDTH = 512
SCREEN_HEIGHT = 512
SCREEN_TITLE = "Chess Engine"
PIECE_IMAGES = {
    'wP': 'pieces/wPawn.png',
    'wR': 'pieces/wRook.png',
    'wN': 'pieces/wKnight.png',
    'wB': 'pieces/wBishop.png',
    'wQ': 'pieces/wQueen.png',
    'wK': 'pieces/wKing.png',
    'bP': 'pieces/bPawn.png',
    'bR': 'pieces/bRook.png',
    'bN': 'pieces/bKnight.png',
    'bB': 'pieces/bBishop.png',
    'bQ': 'pieces/bQueen.png',
    'bK': 'pieces/bKing.png'
}
board = [
        ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
        ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
        ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
        ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
        ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
        ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
        ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
        ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
    ]

def draw_piece(piece, column, row):
    if piece in PIECE_IMAGES:
        texture = arcade.load_texture(PIECE_IMAGES[piece])
        x = (column * 64) + 32
        y = (row * 64) + 32
        texture.draw_scaled(x, y, 1)

def draw_board(board):
    for row in range(8):
        for column in range(8):
            if (row + column) % 2 == 0:
                color = arcade.color.WHITE_SMOKE
            else:
                color = arcade.color.BLACK_OLIVE
            x = (column * 64) + 32
            y = (row * 64) + 32
            arcade.draw_rectangle_filled(x, y, 64, 64, color)
            draw_piece(board[row][column], column, row)

def setup_window():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.WHITE)
    return window

def main():
    window = setup_window()
    arcade.start_render()
    draw_board(board)
    arcade.finish_render()
    arcade.run()

if __name__ == "__main__":
    main()
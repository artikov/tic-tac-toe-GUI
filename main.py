from board import Board
from logic import Game


def main():
    game = Game()
    board = Board(game)
    board.mainloop()


if __name__ == "__main__":
    main()
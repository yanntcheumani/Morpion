from Board import *

Board = Board()


def main():
    print("welcometo the Tic Tac Toe game")
    print("the boxes are count from left to right")
    Board.Board(Board.board)
    while not Board.BoardFull(Board.board):
        if not Board.Winner(Board.board, "O"):
            Board.UserMove()
            Board.Board(Board.board)
        else:
            print("Sorry, my AI won this time :)")
            break
        if not Board.Winner(Board.board, "X"):
            move = Board.AImove()
            if move == 0:
                print("Tie Game!")
            else:
                Board.InsertLetter("O", move)
                print("Ai placed an \'O\' in position", move)
                Board.Board(Board.board)
        else:
            print("Good job, you win ")
            break
    if Board.BoardFull(Board.board):
        print("Tie Game !")


main()

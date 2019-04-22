'''
Class: CPSC 427
Team Member 1: Kathrine Gibson
Team Member 2: Kasey Davis
Submitted By Kathrine Gibson
GU Username: kgibson2
File Name: main.py
Creates the interface for a game of Othello

Usage 1:  python3 <program name>
          python3 main.py
'''
import othello_board
import ColorPrinter as cp


def main():
    new_board = othello_board.OthelloBoard()
    print(new_board.board)


if __name__ == "__main__":
    main()

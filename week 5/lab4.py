import argparse
import os
from dotenv import load_dotenv
load_dotenv()



parser = argparse.ArgumentParser(description="A Connect-4 game")
parser.add_argument("-r", "--rows", type=int, default=6)
args = parser.parse_args() # takes any command line arguments and adds them to the 'agrs' object

ROWS = args.rows
EMPTY = ""
USER = "o "
COMPUTER = "x"



 # Check negatively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True
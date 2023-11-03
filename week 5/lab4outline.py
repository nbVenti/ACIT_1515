"""

    ACIT 1515 - Lab 4

    For Lab 4 you will be implementing and debugging a command-line version of Connect 4, a game consisting of a vertically suspended board where players take turns dropping a colored token into columns with the aim of forming a vertical, horizontal, or diagonal line of four of their tokens.

    See https://en.wikipedia.org/wiki/Connect_Four for more info

    ---

    For this implementation, the board will be square (6 rows by 6 columns by default) and the colored tokens will be represented by the following strings:
        • for an empty space
        o for a user token
        x for the computer opponent token

    Below is an example empty board:

    •   •   •   •   •   •  

    •   •   •   •   •   •  

    •   •   •   •   •   •  

    •   •   •   •   •   •  

    •   •   •   •   •   •  

    •   •   •   •   •   •
        
    And an example of a board where the user has won by forming a diagonal line of four tokens:

    •   •   •   •   •   •

    •   •   •   •   •   •  

    •   •   •   o   •   •  

    •   •   o   x   •   •  

    •   o   o   x   •   •  

    o   x   x   x   o   •   


    PART 1
    ---------------------------------------------------------------------------
    
    The main function in this script will be responsible for repeatedly asking the player to choose a position (alternating as the 'user' then the 'computer'), validating the position, updating the board if the position is valid, and then printing the board to the command-line. 
    
    IMPORTANT: just like the vertical, physical version of the game, the player should not be allowed to choose a position with an empty space below it, i.e. the following game board would be considered invalid:

        0   1   2   3   4   5

    0   •   •   •   •   •   •

    1   •   •   •   •   •   •  

    2   •   •   •   o   •   •      <-- this position (column 3, row 2) has an empty space below it

    3   •   •   o   •   •   •  

    4   •   o   o   x   x   •  

    5   o   x   x   x   o   • 

    Implementation details are provided below in the respective functions


    PART 2
    ---------------------------------------------------------------------------

    Once the program functions correctly, you must refactor the code as necessary to accept any size of board.

    The size (ROWS) value must be supplied as a command-line argument when the script is invoked, e.g.
        py lab4.py --rows 7

    ---
    
    RULES for this submission:

    You CAN:
        - add parameters to functions if necessary
        - move repetitive code into a new function
        - modify the code in the main() function as needed
        - import any necessary modules (from the standard library only!)

    You MUST:
        - only use the print_board function to output the board (i.e. print(board) is not allowed except for debugging purposes)
        - remove any hard-coded values (e.g. use the ROWS, EMPTY, USER, and COMPUTER variables)
        - use the prompt() function we previously defined to handle error checking and valid input

"""

# from <your module name> import prompt

ROWS = 6
EMPTY = "• "
USER = "o "
COMPUTER = "x "

def valid_move(board, position):
    """
    board: a two-dimensional list of strings (• for empty, o for user, * for computer)
    position: the numeric position of the users next move (e.g. 0 - 35 for a 6x6 board)
    """
    if board[position] != EMPTY:
        # Return a tuple with two values: False, and a string indicating to the player that the position is already occupied (see example below)
        return

    # Add an additional check that ensures that IF the chosen position is not in the bottom row of the grid, a token already exists below it - if not, return a tuple with two values: False, and a string indicating to the player that the position is not valid
    
    # If neither of the above conditions are true, the position must be valid
    return True

def update_board(position, symbol):
    """
    position: the numeric position of the users move (e.g. 0 - 35 for a 6x6 board)
    symbol: a string representing the player (o for user, x for computer)
    """
    # Update the board at the specified position with the symbol
    pass

def print_board(board):
    """
    board: a two-dimensional list of strings (• for empty, o for user, * for computer)
    """
    # Print the (nicely formatted) board to the console, see example output above
    pass

def check_state(board):
    """
    board: a two-dimensional list of strings (• for empty, o for user, * for computer) 
    """
    
    # After each turn (player or user), the check_state() function must check to see if there are still (non-empty) positions to play. If all positions are filled, return False, otherwise return True

    # OPTIONAL: for an additional challenge, implement the code necessary to check for a win state (a player who has formed a vertical, horizontal, or diagonal line of four tokens). If a win state is detected, modify the return value (and main function) if necessary such that a message is printing indicating the game has been won, and stop the program
    pass

def main():
    board = [
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]
    ]

   # Begin the game by printing the board (using the print_board function)

    game_over = False

    while not game_over:
        move = prompt("Please enter user move:", range(36), int)
        valid = valid_move(board, move)
        
        if not valid[0]:
            # print the message returned from valid_move
            # print the board
            pass
        else:
            # update the board, storing the USER symbol to the chosen position
            # check the board state and continue or end the game
            pass

        # repeat the steps above for the COMPUTER player  

if __name__ == "__main__":
    main()
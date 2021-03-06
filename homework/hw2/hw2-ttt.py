import sys

# CONSTANTS
PLAYER_NAMES = ["Nobody", "X", "O"] 

# FUNCTIONS
def player_name(player_id):
    '''return the name of a player with a specified ID

    Looks up the name in the PLAYER_NAMES global list

    Parameters
    ----------
    player_id: int
        player's id, which is an index into PLAYER_NAMES

    Returns
    -------
    string
        the player's name

    '''
    return PLAYER_NAMES[player_id]


def display_board(board):
    '''display the current state of the board

    board layout:
    1 | 2 | 3
    4 | 5 | 6
    7 | 8 | 9

    Numbers are replaced by players' names once they move. 
    Iterate through the board and choose the right thing
    to display for each cell.

    Parameters
    ----------
    board: list
        the playing board

    Returns
    -------
    None
    '''

    board_to_show = "" # string that will display the board, starts empty
    for i in range(len(board)):
        if board[i] == 0: # 0 means unoccupied
            # displayed numbers are one greater than the board index
            board_to_show += str(i + 1) # display cell number
        else:
            board_to_show += player_name(board[i]) # display player's mark
        if (i + 1) % 3 == 0: # every 3 cells, start a new row
            board_to_show += "\n"
        else:
            board_to_show += " | " # within a row, divide the cells
    print()
    print(board_to_show)


def make_move(player, board):
    '''allows a player to make a move in the game

    displays who's move it is (X or O)
    prompts the user to enter a number 1-9
    validates input, repeats until valid input is entered
    checks move is valid (space is unoccupied), repeats until valid move
    is entered

    Parameters
    ----------
    player: int
        the id of the player to move (1 = X, 2 = O)

    board: list
        the board upon which to move
        the board is modified in place when a valid move is entered
    '''
    x = 0 # this is the counter for our function. We break out of it with valid attempts. We stay in it with invalid attempts.
    while x < 9:
        print("=" * 45)
        response = input(f"Type \"quit\" to quit.\n{player_name(player)}'s move: ")
        if response.isnumeric(): # input takes this if the input registers as numeric characters
            position = int(response)
            if 0 < position < 10:
                if board[position - 1] == 0: 
                # the line above is saying IF THE INDEXED VALUE OF THE BOARD AT THE TIME OF TURN EQUALS ZERO 
                # (which it should for a valid turn) then let 'em occupy it!!!!!!!!
                    board[position - 1] = player # the user's selection is indexed and sent to update board list
                    x += 1
                    break
                elif board[position - 1] != 0:
                    board = board
                    x = x
                    print(f"That's an invalid input, {player_name(player)}. Try again.")
                    display_board(board)
            elif position < 1:
                x = x
                print("Enter a number between 1 and 9.")
                display_board(board)
            elif position > 9:
                x = x
                print("Enter a number between 1 and 9.")
                display_board(board)

        elif response.isalpha():
            position = str(response)
            if position == "quit":
                sys.exit(0)
            elif position != "quit":
                x = x
                print("Enter a number between 1 and 9.")
                display_board(board)
        else:
            x = x
            print("Enter a number between 1 and 9.")
            display_board(board)
        # even though the assignment instructions don't include a printed board after 
        # an "arrrrgh!" input (because it's read as neither alpha nor numeric),
        # I included a display_board() function here so that no matter how far along a user
        # is in the game, and no matter their input, they can see the board's status.


def check_win_horizontal(board):
    '''checks if a player is fully occupying any rows

    if a player occupies the three spaces of a given row
    the board is indexed to find which player wins

    Parameters
    ----------
    board: list
        the board to determine equivalency of player's ID

    Returns
    ----------
    int
        the int is either the number of the corresponding 
        winning player (i.e. 1 = X and 2 = O)
        or 0, which means no one has won.
    '''
    if (board[0] != 0 and 
        board[0] == board[1] and 
        board[0] == board[2]):
        return board[0]
    if (board[3] != 0 and
        board[3] == board[4] and 
        board[3] == board[5]):
        return board[3]
    if (board[6] != 0 and
        board[6] == board[7] and 
        board[6] == board[8]):
        return board[6]
    return 0


def check_win_vertical(board):
    '''checks if a player is fully occupying any columns

    if a player occupies the three spaces of a given column
    the board is indexed to find which player wins

    Parameters
    ----------
    board: list
        the board to determine equivalency of player's ID

    Returns
    ----------
    int
        the int is either the number of the corresponding 
        winning player (i.e. 1 = X and 2 = O)
        or 0, which means no one has won.
    '''
    if (board[0] != 0 and 
        board[0] == board[3] and 
        board[0] == board[6]):
        return board[0]
    if (board[1] != 0 and
        board[1] == board[4] and 
        board[1] == board[7]):
        return board[1]
    if (board[2] != 0 and
        board[2] == board[5] and 
        board[2] == board[8]):
        return board[2]
    return 0


def check_win_diagonal(board):
    '''checks if a player is fully occupying either of the two diagonals

    if a player occupies the three spaces of a diagonal 
    (board numbers 1, 5, 9 -OR- 3, 5, 7)
    the board is indexed to find which player wins

    Parameters
    ----------
    board: list
        the board to determine equivalency of player's ID

    Returns
    ----------
    int
        the int is either the number of the corresponding 
        winning player (i.e. 1 = X and 2 = O)
        or 0, which means no one has won.
    '''
    if (board[0] != 0 and 
        board[0] == board[4] and 
        board[0] == board[8]):
        return board[0]
    if (board[2] != 0 and
        board[2] == board[4] and 
        board[2] == board[6]):
        return board[2]
    return 0


def check_win(board):
    '''checks a board to see if there's a winner

    delegates to functions that check horizontally, vertically, and 
    diagonally to see if there is a winner. Returns the first winner
    found in the case of multiple winners.

    Parameters
    ----------        
    board: list
        the board to check

    Returns
    -------
    int
        the player ID of the winner. 0 means no winner found.
    '''

    winner = check_win_horizontal(board)
    if (winner != 0):
        display_board(board)
        print(f"Game over! {player_name(player)} wins!")
        return winner
    
    winner = check_win_vertical(board)
    if (winner != 0):
        display_board(board)
        print(f"Game over! {player_name(player)} wins!")
        return winner
   
    winner = check_win_diagonal(board)
    if (winner != 0):
        display_board(board)
        print(f"Game over! {player_name(player)} wins!")
        return winner

    return 0


def next_player(current_player):
    '''determines who goes next

    given the current player ID, returns the player who should 
    go next

    Parameters
    ----------        
    current_player: int
        the id of the player who's turn it is now

    Returns
    -------
    int
        the id of the player to go next
    '''
    if moves_left % 2 == 1:
    	return 2 
    if moves_left % 2 == 0:
    	return 1

# MAIN PROGRAM (INDENT LEVEL 0)

# GLOBAL VARIABLES
board = [0, 0, 0,   # top row:    indices 0, 1, 2
         0, 0, 0,   # middle row: indices 3, 4, 5
         0, 0, 0]   # bottom row: indices 6, 7, 8

player = 1          # X goes first
moves_left = 9      # number of moves so far 
winner = 0          # "Nobody" is winning to start

while(moves_left > 0 and winner == 0):
    display_board(board)
    make_move(player, board)
    winner = check_win(board)
    player = next_player(player)
    moves_left -= 1
    if moves_left == 0:
        display_board(board)
        print("Game over! Nobody wins!")
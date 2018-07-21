#Project 2 Ryan Cox ID#1953949

import connectfour

def print_board(game_board: [[int]]) -> 'printboard':
    ''' prints out the board '''

    #Print column numbers
    for num in range(connectfour.BOARD_ROWS + 1):
        print(num + 1, end = '  ')
    print()

    for row in range(0, connectfour.BOARD_ROWS):
        for col in range(0, connectfour.BOARD_COLUMNS):
            if game_board[col][row] == 0: #NONE
                print('.', end = '  ')
            elif game_board[col][row] == 1: #RED
                print('R', end = '  ')
            elif game_board[col][row] == 2: #YELLOW
                print('Y', end = '  ')
            else:
                pass
        print()
    
def change_turn(turn:str) -> str:
    ''' changes turn depending on the current turn '''
    red = "Turn: RED"
    yellow = "Turn: YELLOW"

    if turn == red:
        return yellow
    else:
        return red

def winner_print(gamestate: connectfour.GameState) -> str:
    ''' prints out winner when one is given '''
    statement = 'No Winner'
    
    if connectfour.winner(gamestate) == 1:
        statement = "RED player has WON"
    elif connectfour.winner(gamestate) == 2:
        statement = "YELLOW player has WON"

    return statement

def move_column_choose(col_max: int) -> int:
    ''' choose col to drop in as long as it exists '''
    while True:
        try:
            choice = int(input("Please choose a column (1-7): "))
            choice = choice - 1
            if choice >= 0 and choice <= col_max:
                return choice
            else:
                move_column_choose()
        except ValueError:
            col_num_string = str(col_max)
            print("The value you entered does not work. Please enter a number between 1 and " + col_num_string)

def drop_or_pop () -> str:
    ''' user chooses to drop or pop '''
    while True:
        choice = input("Choose to DROP or POP a piece: ")
        choice = choice.strip().upper()
        if choice == "DROP" or choice == "POP":
            return choice
        else:
            print("Your choice was not valid. Choose to DROP or POP.")

def drop(gamestate: connectfour.GameState, column_choice: int) -> connectfour.GameState:
    ''' executes drop move'''
    gamestate = connectfour.drop(gamestate, column_choice)
    return gamestate

def pop(gamestate: connectfour.GameState, column_choice: int) -> connectfour.GameState:
    ''' executes pop move '''
    gamestate = connectfour.pop(gamestate, column_choice)
    return gamestate


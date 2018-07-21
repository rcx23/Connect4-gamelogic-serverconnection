#Project 2 Ryan Cox ID# 31953949

import connectfour
import project2socket
import project2

def main_runner():
    ''' executes the game to run '''
    print("Welcome to Connect 4 versus AI. To start a game use:")
    print("Host: woodhouse.ics.uci.edu")
    print("Port: 4444")
    print()

    gamestate = connectfour.new_game()
    start = start_game()

    while connectfour.winner(gamestate) == 0:
        turn = gamestate.turn
        if start == None:
            break
        if turn == 1:
            gamestate = red(gamestate, start)
        elif turn == 2:
            gamestate = yellow(gamestate, start)           
        else:
            break

    print(project2.winner_print(gamestate))
    project2socket.close_connection(start)
    
        
def start_game() -> project2socket.Connection:
    ''' establishes connection with the server to play the game '''
    try:
        host = project2socket.read_host()
        port = project2socket.read_port()

        print("Establishing connection...")
        print("Connecting to the Host: {} (Port: {})".format(host, port))

        connection = project2socket.connect(host, port)

        print("You have been CONNECTED")
        print(project2socket.login(connection))
        print(project2socket.AI_connect(connection))

        return connection
    except:
        print("The program was not able to connect. Please try again.")

##### AI movement #####

def yellow(gamestate: connectfour.GameState, connection: project2socket.Connection) -> connectfour.GameState:
    ''' handles the AI move '''
    move = project2socket.AI_move(connection)
    print(move)
    move = move.split()
    column_choice = int(move[1])-1

    if move[0] == "DROP":
        gamestate = project2.drop(gamestate, column_choice)
        project2.print_board(gamestate.board)
    elif move[0] == "POP":
        gamestate = project2.pop(gamestate, column_choice)
        project2.print_board(gamestate.board)
    else:
        project2socket.close_connection(connection)

    _yellow(connection)

    return gamestate
                
def _yellow(connection: project2socket.Connection) -> None:
    ''' handles the readline '''
    move = project2socket.AI_move(connection)
    if move == "READY":
        print("READY")

###### Player Movement #####

def red(gamestate: connectfour.GameState, connection: project2socket.Connection) -> connectfour.GameState:
    ''' handles the player move '''
    while True:
        move = project2.drop_or_pop()
        column_choice = project2.move_column_choose(connectfour.BOARD_COLUMNS)

        if move == 'DROP':
            try:
                gamestate = project2.drop(gamestate, column_choice)
                project2.print_board(gamestate.board)
                break
            except connectfour.InvalidMoveError:
                print("This move is invalid.")
        elif move == 'POP':
            try:
                gamestate = project2.pop(gamestate, column_choice)
                project2.print_board(gamestate.board)
                break
            except connectfour.InvalidMoveError:
                print("This move is invalid.")
        else:
            project2socket.close_connection(connection)
    _red(connection, move, column_choice)
    return gamestate

def _red(connection:project2socket.Connection, move: str, column: int) -> None:
    ''' handles the readline '''
    move = project2socket.send_move(connection, move + ' ' + str(column + 1))
    if move == "OKAY":
        print("OKAY")

#################################################################################                

if __name__ == '__main__':
    main_runner()

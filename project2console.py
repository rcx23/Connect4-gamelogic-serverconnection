#Project 2 console Ryan Cox ID#31953949

import connectfour
import project2

#Gamestate format: GameState = collections.namedtuple('GameState', ['board', 'turn'])

def user_interface():
    columns = connectfour.BOARD_COLUMNS
    rows = connectfour.BOARD_ROWS
    gamestate = connectfour.new_game()

    print("Welcome to connect 4. Red Player will go first.")

    turn = "Turn: YELLOW"
    turn = project2.change_turn(turn)

    while connectfour.winner(gamestate) == 0:
        drop_or_pop = project2.drop_or_pop()
        column_choice = project2.move_column_choose(columns)

        if drop_or_pop == "DROP":
            try:
                gamestate = project2.drop(gamestate, column_choice)
                project2.print_board(gamestate.board)
                turn = project2.change_turn(turn)
                if connectfour.winner(gamestate) == 1 or connectfour.winner(gamestate) == 2:
                    break
                print(turn)
            except connectfour.InvalidMoveError:
                print("THIS MOVE IS INVALID")
        elif drop_or_pop == "POP":
            try:
                gamestate = project2.pop(gamestate, column_choice)
                project2.print_board(gamestate.board)
                turn = project2.change_turn(turn)
                if connectfour.winner(gamestate) == 1 or connectfour.winner(gamestate) == 2:
                    break
                print(turn)
            except connectfour.InvalidMoveError:
                print("THIS MOVE IS INVALID")

    print(project2.winner_print(gamestate))
        

if __name__ == '__main__':
    user_interface()

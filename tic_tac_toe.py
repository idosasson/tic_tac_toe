from random import randint


def print_board(board):
    print()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == None:
                print("|   |", end='   ')
            else:
                print(f"| {board[i][j]} |", end='   ')
        print()

def user_input(used_positions, is_player_one_turn):
    while True:
        try:
            if is_player_one_turn:
                print("\nPlayer 1 turn!")
            else:
                print("\nPlayer 2 turn!")
            position = input("\nPlease enter your position(0-8):  ")
            position = int(position)
            if(position < 0 or position > 8):
                e = Exception("\nPosition out of range")
                raise e
            elif(position in used_positions):
                e = Exception("\nPosition already in use")
                raise e
        except Exception as e:
            print(e)
            print("\nPlease enter a valid position")
            continue
        return position

def change_into_valid_position(board, position):
    row = int(position / 3)
    col = position % 3
    return (row, col)

def player_move(board, used_positions, is_player_one_turn, player_one_symbol_is_X, play_against_computer):
    chosen_position = None
    if play_against_computer and not is_player_one_turn:
        while True:
            chosen_position = randint(0, 8)
            if chosen_position not in used_positions:
                break

    else:
        chosen_position = user_input(used_positions, is_player_one_turn)
    used_positions.append(chosen_position)
    valid_position = change_into_valid_position(board, chosen_position)
    print(valid_position)
    if (is_player_one_turn and player_one_symbol_is_X) or (not player_one_symbol_is_X and not is_player_one_turn):
        board[valid_position[0]][valid_position[1]] = 'X'
    else:
        board[valid_position[0]][valid_position[1]] = 'O'
    print_board(board)


def check_win(board):

    if (board[0][0] == board[1][1] == board[2][2]) and board[0][0] is not None:
        return True

    elif (board[0][2] == board[1][1] == board[2][0]) and board[2][0] is not None:
        return True

    for i in range(len(board)):
        if (board[i][0] == board[i][1] == board[i][2]) and board[i][0] is not None:
            return True
        elif (board[0][i] == board[1][i] == board[2][i]) and board[0][i] is not None:
            return True

    return False


def game(is_player_one_turn, player_one_symbol_is_X, play_against_computer):


    board = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]
    used_positions = []


    someone_won = False

    print_board(board)
    for i in range(9):
        player_move(board, used_positions, is_player_one_turn, player_one_symbol_is_X, play_against_computer)
        if(i > 3):
            if check_win(board):
                if (is_player_one_turn):
                    print("\nPlayer 1 wins!")
                    someone_won = True
                    break
                elif(play_against_computer):
                    print("\nThe computer wins!")
                    someone_won = True
                    break
                else:
                    print("\nPlayer 2 wins!")
                    someone_won = True
                    break
        is_player_one_turn = not is_player_one_turn
    if not someone_won:
        print("\nThe ended in a draw!")

def start_game():
    is_player_one_turn = None
    player_one_symbol_is_X = None
    play_against_computer = None
    print("\nWelcome to my Tic TcToe game!\n")
    while True:
        player_one_name = input("\nPlayer 1 please enter your name: ")
        print(f"welcome {player_one_name}!")
        print("\n Press 'X' to play as 'X'")
        print("\n Press 'O' to play as 'O'")
        print("\n Press anything else to get a random symbol")

        player_one_symbol = input(f"\n{player_one_name} please enter your simbol:")

        if player_one_symbol == 'X':
            is_player_one_turn = True
            player_one_symbol_is_X = True
        elif player_one_symbol == 'O':
            is_player_one_turn = False
            player_one_symbol_is_X = False
        else:
            is_player_one_turn = bool(randint(0, 1))
            player_one_symbol_is_X = is_player_one_turn

        input_against_computer = input("\nDo you want to play against the computer? press 'Y' for yes or anything else for no: ")
        if input_against_computer == 'Y':
            play_against_computer = True
        else:
            play_against_computer = False
            player_two_name = input("\nPlayer 2 please enter your name: ")
            print(f"welcome {player_two_name}!")

        game(is_player_one_turn, player_one_symbol_is_X, play_against_computer)
        restart = input("\nDo you want to play again? press 'Y' for yes or anything else for no: ")
        if(restart == "Y"):
            continue
        break
    print("\nGame ended!")
    print("\nThank you for playing!")


if __name__ == '__main__':
    start_game()

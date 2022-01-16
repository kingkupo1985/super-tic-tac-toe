import random

players = {
    'p1': {'ishuman': False, 'marker': 'o'},
    'p2': {'ishuman': False, 'marker': 'x'}
}

gameBoard = {'1':' ', '2': ' ', '3': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '7': ' ', '8': ' ', '9': ' '}

player_one = list(players.keys())[0]
player_two = list(players.keys())[1]

# print game board when a move gets
def print_board():
    # Smart Tic Tac Toe Board
    print_string = ''
    print_board_string = ''
    i = 0
    # Loop through each key in the length of the dictonary
    while i < len(gameBoard):
        # Check for 3,6,9 to break line and store to price
        if list(gameBoard.keys())[i] == '3' or list(gameBoard.keys())[i] == '6' or list(gameBoard.keys())[i] == '9':
            # Annoying redundance but no other way I could figure out to check for null key values and print key or value
            if gameBoard[list(gameBoard.keys())[i]] == ' ':
                # if key valueis null print KEY in place holder
                print_string += list(gameBoard.keys())[i]
            else:
                # if key value is not null use value in place holder
                print_string += gameBoard[list(gameBoard.keys())[i]]
            # Checking if it's the end of game board
            if list(gameBoard.keys())[i] == '9':
                print_board_string += print_string
                print_string = ''
            else:
                # break line, reset string for next tic-tac-toe-line
                print_board_string += print_string + '\n' + '-+-+-' + '\n'
                print_string = ''
        # check all other keys for null values in dict if not 3,6,9
        elif gameBoard[list(gameBoard.keys())[i]] == ' ':
            # if key value is null use key for place holder
            print_string += list(gameBoard.keys())[i] + '|'

        elif gameBoard[list(gameBoard.keys())[i]] != ' ':
            # if not null value use value for place holder
            print_string += gameBoard[list(gameBoard.keys())[i]] + '|'
        i += 1
    # print board to screen
    print(print_board_string)

# If CPU player have them make move on open space
def make_cpu_move(player):
    # cpu_move = range(9)
    if not player['ishuman']:
        # cpu choice random based on gameboard keys
        move_choice = random.randint(1,9)
        if gameBoard[str(move_choice)] == ' ':
            x_or_o = player['marker']
            gameBoard[str(move_choice)] = x_or_o
            print('CPU Move Below:')
            print_board()
        else:
            print('CPU move Already Taken')
            make_cpu_move(player)

# Have human players make move on open space
def make_human_move(player):
    move_choice = input(f'Chose from the board using\n 1,2,3 \n 4,5,6 \n 7,8,9 \nEnter a choice: ')
    if gameBoard[move_choice] != ' ':
        print('Player Move Already Taken')
        make_human_move(player)
    else:
        x_or_o = player['marker']
        gameBoard[move_choice] = x_or_o
        if x_or_o == 'o':
            player_turn = list(players.keys())[0]
        else:
            player_turn = list(players.keys())[1]
        print(f"{player_turn}'s Move Below:")
        print_board()
        return player_turn

# decide if human players or CPU player is needed based on selection
def player_select():
    player_select = int(input('How many human players 1 or 2?: '))
    if player_select == 1:
        players['p1']['ishuman'] = True
        players['p2']['ishuman'] = False
    elif player_select == 2:
        players['p1']['ishuman'] = True
        players['p2']['ishuman'] = True

# checking if current player won
def check_win_condition(player):
    if player == 'p1':
        player = 'player one'
    elif player == 'p2':
        player = 'player two'
# checking all possible tic-tac-toe combinations
    if gameBoard['1'] == gameBoard['2'] == gameBoard['3'] != ' ':
        print(f'You win {player}')
        return True
    elif gameBoard['4'] == gameBoard['5'] == gameBoard['6'] != ' ':
        print(f'You win {player}')
        return True
    elif gameBoard['7'] == gameBoard['8'] == gameBoard['9'] != ' ':
        print(f'You win {player}')
        return True
    elif gameBoard['1'] == gameBoard['4'] == gameBoard['7'] != ' ':
        print(f'You win {player}')
        return True
    elif gameBoard['2'] == gameBoard['5'] == gameBoard['8'] != ' ':
        print(f'You win {player}')
        return True
    elif gameBoard['3'] == gameBoard['6'] == gameBoard['9'] != ' ':
        print(f'You win {player}')
        return True
    elif gameBoard['1'] == gameBoard['5'] == gameBoard['9'] != ' ':
        print(f'You win {player}')
        return True
    elif gameBoard['3'] == gameBoard['5'] == gameBoard['7'] != ' ':
        print(f'You win {player}')
        return True
    return False

# run the game
def run_game():
    # setting win condition for game loop
    win_condition = False
    # getting player key for turn rotation
    whos_turn = list(players.keys())[0]
    turn = 0
    # start game loop
    while not win_condition:
        # Checking if current player is human or not
        if not players[whos_turn]['ishuman']:
            # not human player make a CPU move
            make_cpu_move(players[whos_turn])
            turn += 1
        else:
            # make a human player move
            make_human_move(players[whos_turn])
            turn += 1
        win_condition = check_win_condition(whos_turn)
        if turn == 9:
            print("It's a draw!")
            win_condition = True
        # check who just went and rotate to new players turn
        if whos_turn == 'p1':
            whos_turn = list(players.keys())[1]
        else:
            whos_turn = list(players.keys())[0]
    # Someone won ask if they want to play again
    play_again()

# play again function to reset game board and player selection
def play_again():
    # asking if they want to play another round
    again = input('Do you want to play again? Y or N: ').lower()
    if again == 'y':
        # get global variable
        global gameBoard
        # reset gameBoard
        gameBoard = {'1': ' ', '2': ' ', '3': ' ',
                     '4': ' ', '5': ' ', '6': ' ',
                     '7': ' ', '8': ' ', '9': ' '}
        player_select()
        run_game()
    else:
        exit()

# initalize the game for the first time
player_select()
run_game()
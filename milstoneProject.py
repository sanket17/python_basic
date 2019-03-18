# create a tic tac game for two player

# Algo

# 1  accept  X or 0 for player one
# 2  assign alternate sign for player two
# 3  display empty board
# 4  check of all position are filled, if not then go to step 5 else go to step 14
# 5  accept position from player one
# 6  dipslay board marked with player one Sign
# 7  check if player one win, if he won go to step 12 else go to step 8  
# 8  accept position from player two
# 9  check if player two win, if he won then go to step 12 else go to step 11
# 10 display board marked with player two sign
# 11 if no player wins go to step 4
# 12 display wiining message, go to step 12
# 13 ask if he wants to replay then go to step 1
# 14 dislay message that no player won and go to step

player_one_sign = ''
player_two_sign = ''
player_one_position = 0
player_two_position = 0
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
replay_flag = False

def accept_player_one_position():
    assign_flag = True

    while assign_flag:
        player_one_position = int(input('Enter Player 1 position: '))
        if board[player_one_position-1] != 'X' or board[player_one_position-1] != 'O':
            board[player_one_position-1] = player_one_sign
        else:
            print('\nEntered Position is marked already! Please select another Position\n')
            assign_flag = False
        
def accept_player_two_position():
    assign_flag = True

    while assign_flag:
        player_two_position = int(input('Enter Player 2 position: '))
        if board[player_two_position-1] != 'X' or board[player_two_position-1] != 'O':
            board[player_two_position-1] = player_two_sign
        else:
            print('\nEntered Position is marked already! Please select another Position\n')
            assign_flag = False

def accept_player_one_sign():
    sign = input('Enter Player 1 sign (X or O): ')
    global player_one_sign 
    global player_two_sign 
    player_one_sign = sign.upper()
    
    if player_one_sign == 'X':
        player_two_sign = '0'
    else:
         player_two_sign = 'X'

def display_board():
    print('\n')
    print(board[6] +'|'+ board[7] +'|'+ board[8] )
    print('-----')
    print(board[3] +'|'+ board[4] +'|'+ board[5] )
    print('-----')
    print(board[0] +'|'+ board[1] +'|'+ board[2] )
    print('\n')

def replay():
    message = input('Do you want to play again (y = Yes | n = No): ')
    if message == 'y' or message.lower() == 'y':
        return True
    else:
        return False

def show_win_message(player):
    print(f'Congrulations! Player {player} won the game!')

def check_win(player_sign):
    
    global board
    if (board[0] == player_sign and board[1] == player_sign and board[2] == player_sign):
        return True
    elif (board[3] == player_sign and board[4] == player_sign and board[5] == player_sign):
        return True
    elif (board[6] == player_sign and board[7] == player_sign and board[8] == player_sign):
        return True
    elif (board[0] == player_sign and board[3] == player_sign and board[6] == player_sign):
        return True
    elif (board[1] == player_sign and board[4] == player_sign and board[7] == player_sign):
        return True
    elif (board[2] == player_sign and board[5] == player_sign and board[8] == player_sign):
        return True
    elif (board[0] == player_sign and board[4] == player_sign and board[8] == player_sign):
        return True 
    elif (board[2] == player_sign and board[4] == player_sign and board[6] == player_sign):
        return True
    else:
        return False

def play_game():
    play_flag = False
    winning_player = 0

    print('Welcome to tic-tac-toe!!')
    accept_player_one_sign()
    display_board()
    
    global player_one_sign
    global player_two_sign

    while not play_flag:
        
        accept_player_one_position()
       
        play_flag = check_win(player_one_sign)
        if play_flag == True:
            winning_player = 1
            break        
        display_board()
        
        accept_player_two_position()
        play_flag = check_win(player_two_sign)
        if play_flag == True:
            winning_player = 2
            break
        display_board()

        play_flag = ' ' not in board
        if play_flag == True:
            print('The Match is drawn!!')
            replay_flag = replay() 
            winning_player = 0
            break

    if winning_player != 0:
        print(f'Congrulations! Player {winning_player} won the game!')
        replay_flag = replay()
    
def tic_tac_toe():
    play_game()
    while replay_flag:
        play_game()

tic_tac_toe()



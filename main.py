
# TIC TAC TOE!!
# AUTHOR: COLBY CLARK

import random
import time

def one_player():

    # BOARD
    board_layout = [' ', '7', ' ', '|', ' ', '8', ' ', '|', ' ', '9', ' ', '\n',
                    ' ', '4', ' ', '|', ' ', '5', ' ', '|', ' ', '6', ' ', '\n',
                    ' ', '1', ' ', '|', ' ', '2', ' ', '|', ' ', '3', ' ']

    available_positions = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    # GAME STATE BOOLS
    game_loop = True
    player1_turn = True
    player2_turn = True

    # HAVE PLAYER GUESS COIN TOSS FOR FIRST TURN
    heads_tails = input("Let\'s decide who goes first with a coin toss! Heads or tails? --> ")
    heads_tails_choice_player = 0
    coin = [1, 2]
    coin_toss_result = random.choice(coin)

    while True:

        if heads_tails == "Heads" or heads_tails == "heads" or heads_tails == "HEADS":
            heads_tails_choice_player += 1
            break

        elif heads_tails == "Tails" or heads_tails == "tails" or heads_tails == "TAILS":
            heads_tails_choice_player += 2
            break

        else:
            heads_tails = input("Let\'s decide who goes first! Heads or tails? --> ")

    if heads_tails_choice_player == coin_toss_result:
        print("You win the coin toss! You get the first turn.")
        time.sleep(3)
        print(''.join(board_layout))

        # PLAYER FIRST - GAME EXECUTION

        while game_loop:

            # PLAYER 1 TURN
            while player1_turn:

                time.sleep(1)
                print('')
                print("Choose a number that corresponds with where you wish to place your marker and press ENTER!")
                print('')

                player_choice = input(' ')
                if player_choice.isnumeric() and player_choice in board_layout:
                    marker_index = board_layout.index(player_choice)
                    board_layout.remove(player_choice)
                    board_layout.insert(marker_index, 'X')
                    available_positions.remove(player_choice)
                    print(''.join(board_layout))
                    player1_turn = False
                else:
                    print('')
                    print('Please use a valid input and press ENTER.')
                    print('')
                    time.sleep(1)
                    print(''.join(board_layout))
                    print('')

            # CHECK FOR PLAYER 1 WIN

            # HORIZONTALS
            if board_layout[0:11].count('X') == 3:
                print('')
                print('Player 1 wins!')
                print('Player 1 wins!')
                print('Player 1 wins!')
                player2_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[12:22].count('X') == 3:
                print('')
                print('Player 1 wins!')
                print('Player 1 wins!')
                print('Player 1 wins!')
                player2_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[23:34].count('X') == 3:
                print('')
                print('Player 1 wins!')
                print('Player 1 wins!')
                print('Player 1 wins!')
                player2_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()

            # DIAGONALS
            elif board_layout[1] == 'X' and board_layout[17] == 'X' and board_layout[33] == 'X':
                print('')
                print('Player 1 wins!')
                print('Player 1 wins!')
                print('Player 1 wins!')
                player2_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[9] == 'X' and board_layout[17] == 'X' and board_layout[25] == 'X':
                print('')
                print('Player 1 wins!')
                print('Player 1 wins!')
                print('Player 1 wins!')
                player2_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()

            # VERTICALS
            elif board_layout[1] == 'X' and board_layout[13] == 'X' and board_layout[25] == 'X':
                print('')
                print('Player 1 wins!')
                print('Player 1 wins!')
                print('Player 1 wins!')
                player2_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[5] == 'X' and board_layout[17] == 'X' and board_layout[29] == 'X':
                print('')
                print('Player 1 wins!')
                print('Player 1 wins!')
                print('Player 1 wins!')
                player2_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[9] == 'X' and board_layout[21] == 'X' and board_layout[33] == 'X':
                print('')
                print('Player 1 wins!')
                print('Player 1 wins!')
                print('Player 1 wins!')
                player2_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout.count('X') >= 5 or board_layout.count('O') >= 5:
                print('')
                print('It\'s a draw!')
                print('')
                time.sleep(2)
                main()
            else:
                player1_turn = True

            # CPU TURN
            while player2_turn:

                print('')
                print('CPU turn...')
                time.sleep(2)
                print('')

                cpu_choice = random.choice(available_positions)
                marker_index = board_layout.index(cpu_choice)
                board_layout.remove(cpu_choice)
                board_layout.insert(marker_index, 'O')
                available_positions.remove(cpu_choice)
                print(''.join(board_layout))
                player2_turn = False

            # CHECK FOR CPU WIN

            # HORIZONTALS
            if board_layout[0:11].count('O') == 3:
                print('')
                print('CPU wins!')
                print('CPU wins!')
                print('CPU wins!')
                player1_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[12:22].count('O') == 3:
                print('')
                print('CPU wins!')
                print('CPU wins!')
                print('CPU wins!')
                player1_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[23:34].count('O') == 3:
                print('')
                print('CPU wins!')
                print('CPU wins!')
                print('CPU wins!')
                player1_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()

            # DIAGONALS
            elif board_layout[1] == 'O' and board_layout[17] == 'O' and board_layout[33] == 'O':
                print('')
                print('CPU wins!')
                print('CPU wins!')
                print('CPU wins!')
                player1_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[9] == 'O' and board_layout[17] == 'O' and board_layout[25] == 'O':
                print('')
                print('CPU wins!')
                print('CPU wins!')
                print('CPU wins!')
                player1_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()

            # VERTICALS
            elif board_layout[1] == 'O' and board_layout[13] == 'O' and board_layout[25] == 'O':
                print('')
                print('CPU wins!')
                print('CPU wins!')
                print('CPU wins!')
                player1_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[5] == 'O' and board_layout[17] == 'O' and board_layout[29] == 'O':
                print('')
                print('CPU wins!')
                print('CPU wins!')
                print('CPU wins!')
                player1_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[9] == 'O' and board_layout[21] == 'O' and board_layout[33] == 'O':
                print('')
                print('CPU wins!')
                print('CPU wins!')
                print('CPU wins!')
                player1_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            else:
                player2_turn = True

    else:

        print("You lose the coin toss! The computer will go first...")
        time.sleep(2)
        print(''.join(board_layout))

        # CPU FIRST - EXECUTION

        while game_loop:

            # CPU TURN
            while player2_turn:

                print('')
                print('CPU turn...')
                time.sleep(2)
                print('')

                cpu_choice = random.choice(available_positions)
                marker_index = board_layout.index(cpu_choice)
                board_layout.remove(cpu_choice)
                board_layout.insert(marker_index, 'O')
                available_positions.remove(cpu_choice)
                print(''.join(board_layout))
                player2_turn = False

            # CHECK FOR CPU WIN

            # HORIZONTALS
            if board_layout[0:11].count('O') == 3:
                print('')
                print('CPU wins!')
                print('CPU wins!')
                print('CPU wins!')
                player1_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[12:22].count('O') == 3:
                print('')
                print('CPU wins!')
                print('CPU wins!')
                print('CPU wins!')
                player1_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[23:34].count('O') == 3:
                print('')
                print('CPU wins!')
                print('CPU wins!')
                print('CPU wins!')
                player1_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()

            # DIAGONALS
            elif board_layout[1] == 'O' and board_layout[17] == 'O' and board_layout[33] == 'O':
                print('')
                print('CPU wins!')
                print('CPU wins!')
                print('CPU wins!')
                player1_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[9] == 'O' and board_layout[17] == 'O' and board_layout[25] == 'O':
                print('')
                print('CPU wins!')
                print('CPU wins!')
                print('CPU wins!')
                player1_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()

            # VERTICALS
            elif board_layout[1] == 'O' and board_layout[13] == 'O' and board_layout[25] == 'O':
                print('')
                print('CPU wins!')
                print('CPU wins!')
                print('CPU wins!')
                player1_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[5] == 'O' and board_layout[17] == 'O' and board_layout[29] == 'O':
                print('')
                print('CPU wins!')
                print('CPU wins!')
                print('CPU wins!')
                player1_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[9] == 'O' and board_layout[21] == 'O' and board_layout[33] == 'O':
                print('')
                print('CPU wins!')
                print('CPU wins!')
                print('CPU wins!')
                player1_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout.count('X') >= 5 or board_layout.count('O') >= 5:
                print('')
                print('It\'s a draw!')
                print('')
                time.sleep(2)
                main()
            else:
                player2_turn = True

            # PLAYER 1 TURN
            while player1_turn:

                time.sleep(1)
                print('')
                print("Choose a number that corresponds with where you wish to place your marker and press ENTER!")
                print('')

                player_choice = input(' ')
                if player_choice.isnumeric() and player_choice in board_layout:
                    marker_index = board_layout.index(player_choice)
                    board_layout.remove(player_choice)
                    board_layout.insert(marker_index, 'X')
                    available_positions.remove(player_choice)
                    print(''.join(board_layout))
                    player1_turn = False
                else:
                    print('')
                    print('Please use a valid input and press ENTER.')
                    print('')
                    time.sleep(1)
                    print(''.join(board_layout))
                    print('')

            # CHECK FOR PLAYER 1 WIN

            # HORIZONTALS
            if board_layout[0:11].count('X') == 3:
                print('')
                print('Player 1 wins!')
                print('Player 1 wins!')
                print('Player 1 wins!')
                player2_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[12:22].count('X') == 3:
                print('')
                print('Player 1 wins!')
                print('Player 1 wins!')
                print('Player 1 wins!')
                player2_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[23:34].count('X') == 3:
                print('')
                print('Player 1 wins!')
                print('Player 1 wins!')
                print('Player 1 wins!')
                player2_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()

            # DIAGONALS
            elif board_layout[1] == 'X' and board_layout[17] == 'X' and board_layout[33] == 'X':
                print('')
                print('Player 1 wins!')
                print('Player 1 wins!')
                print('Player 1 wins!')
                player2_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[9] == 'X' and board_layout[17] == 'X' and board_layout[25] == 'X':
                print('')
                print('Player 1 wins!')
                print('Player 1 wins!')
                print('Player 1 wins!')
                player2_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()

            # VERTICALS
            elif board_layout[1] == 'X' and board_layout[13] == 'X' and board_layout[25] == 'X':
                print('')
                print('Player 1 wins!')
                print('Player 1 wins!')
                print('Player 1 wins!')
                player2_turn = False
                game_loop = False
                print('')
                main()
            elif board_layout[5] == 'X' and board_layout[17] == 'X' and board_layout[29] == 'X':
                print('')
                print('Player 1 wins!')
                print('Player 1 wins!')
                print('Player 1 wins!')
                player2_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[9] == 'X' and board_layout[21] == 'X' and board_layout[33] == 'X':
                print('')
                print('Player 1 wins!')
                print('Player 1 wins!')
                print('Player 1 wins!')
                player2_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            else:
                player1_turn = True

def two_player():

    # BOARD
    board_layout = [' ', '7', ' ', '|', ' ', '8', ' ', '|', ' ', '9', ' ', '\n',
                    ' ', '4', ' ', '|', ' ', '5', ' ', '|', ' ', '6', ' ', '\n',
                    ' ', '1', ' ', '|', ' ', '2', ' ', '|', ' ', '3', ' ']

    available_positions = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    # GAME STATE BOOLS
    game_loop = True
    player1_turn = True
    player2_turn = True

    # HAVE PLAYER GUESS COIN TOSS FOR FIRST TURN
    heads_tails = input("Let\'s decide who goes first with a coin toss! Heads or tails? --> ")
    heads_tails_choice_player = 0
    coin = [1, 2]
    coin_toss_result = random.choice(coin)

    while True:

        if heads_tails == "Heads" or heads_tails == "heads" or heads_tails == "HEADS":
            heads_tails_choice_player += 1
            break

        elif heads_tails == "Tails" or heads_tails == "tails" or heads_tails == "TAILS":
            heads_tails_choice_player += 2
            break

        else:
            heads_tails = input("Let\'s decide who goes first! Heads or tails? --> ")

    if heads_tails_choice_player == coin_toss_result:
        print("PLAYER 1 wins the coin toss! They get the first turn.")
        print('')
        time.sleep(3)
        print(''.join(board_layout))

        # PLAYER ONE FIRST - GAME EXECUTION

        while game_loop:

            # PLAYER 1 TURN
            while player1_turn:

                time.sleep(1)
                print('')
                print('PLAYER 1\'s turn!')
                print('')
                print("Choose a number that corresponds with where you wish to place your marker and press ENTER!")
                print('')

                player_choice = input(' ')
                if player_choice.isnumeric() and player_choice in board_layout:
                    marker_index = board_layout.index(player_choice)
                    board_layout.remove(player_choice)
                    board_layout.insert(marker_index, 'X')
                    available_positions.remove(player_choice)
                    print(''.join(board_layout))
                    player1_turn = False
                else:
                    print('')
                    print('Please use a valid input and press ENTER.')
                    print('')
                    time.sleep(1)
                    print(''.join(board_layout))
                    print('')

            # CHECK FOR PLAYER 1 WIN

            # HORIZONTALS
            if board_layout[0:11].count('X') == 3:
                print('')
                print('Player 1 wins!')
                print('Player 1 wins!')
                print('Player 1 wins!')
                player2_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[12:22].count('X') == 3:
                print('')
                print('Player 1 wins!')
                print('Player 1 wins!')
                print('Player 1 wins!')
                player2_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[23:34].count('X') == 3:
                print('')
                print('Player 1 wins!')
                print('Player 1 wins!')
                print('Player 1 wins!')
                player2_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()

            # DIAGONALS
            elif board_layout[1] == 'X' and board_layout[17] == 'X' and board_layout[33] == 'X':
                print('')
                print('Player 1 wins!')
                print('Player 1 wins!')
                print('Player 1 wins!')
                player2_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[9] == 'X' and board_layout[17] == 'X' and board_layout[25] == 'X':
                print('')
                print('Player 1 wins!')
                print('Player 1 wins!')
                print('Player 1 wins!')
                player2_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()

            # VERTICALS
            elif board_layout[1] == 'X' and board_layout[13] == 'X' and board_layout[25] == 'X':
                print('')
                print('Player 1 wins!')
                print('Player 1 wins!')
                print('Player 1 wins!')
                player2_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[5] == 'X' and board_layout[17] == 'X' and board_layout[29] == 'X':
                print('')
                print('Player 1 wins!')
                print('Player 1 wins!')
                print('Player 1 wins!')
                player2_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[9] == 'X' and board_layout[21] == 'X' and board_layout[33] == 'X':
                print('')
                print('Player 1 wins!')
                print('Player 1 wins!')
                print('Player 1 wins!')
                player2_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout.count('X') >= 5 or board_layout.count('O') >= 5:
                print('')
                print('It\'s a draw!')
                print('')
                time.sleep(2)
                main()
            else:
                player1_turn = True

            # PLAYER 2 TURN
            while player2_turn:

                time.sleep(1)
                print('')
                print('PLAYER 2\'s turn!')
                print('')
                print("Choose a number that corresponds with where you wish to place your marker and press ENTER!")
                print('')

                player_choice = input(' ')
                if player_choice.isnumeric() and player_choice in board_layout:
                    marker_index = board_layout.index(player_choice)
                    board_layout.remove(player_choice)
                    board_layout.insert(marker_index, 'O')
                    available_positions.remove(player_choice)
                    print(''.join(board_layout))
                    player2_turn = False
                else:
                    print('')
                    print('Please use a valid input and press ENTER.')
                    print('')
                    time.sleep(1)
                    print(''.join(board_layout))
                    print('')

            # CHECK FOR PLAYER 2 WIN

            # HORIZONTALS
            if board_layout[0:11].count('O') == 3:
                print('')
                print('Player 2 wins!')
                print('Player 2 wins!')
                print('Player 2 wins!')
                player1_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[12:22].count('O') == 3:
                print('')
                print('Player 2 wins!')
                print('Player 2 wins!')
                print('Player 2 wins!')
                player1_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[23:34].count('O') == 3:
                print('')
                print('Player 2 wins!')
                print('Player 2 wins!')
                print('Player 2 wins!')
                player1_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()

            # DIAGONALS
            elif board_layout[1] == 'O' and board_layout[17] == 'O' and board_layout[33] == 'O':
                print('')
                print('Player 2 wins!')
                print('Player 2 wins!')
                print('Player 2 wins!')
                player1_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[9] == 'O' and board_layout[17] == 'O' and board_layout[25] == 'O':
                print('')
                print('Player 2 wins!')
                print('Player 2 wins!')
                print('Player 2 wins!')
                player1_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()

            # VERTICALS
            elif board_layout[1] == 'O' and board_layout[13] == 'O' and board_layout[25] == 'O':
                print('')
                print('Player 2 wins!')
                print('Player 2 wins!')
                print('Player 2 wins!')
                player1_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[5] == 'O' and board_layout[17] == 'O' and board_layout[29] == 'O':
                print('')
                print('Player 2 wins!')
                print('Player 2 wins!')
                print('Player 2 wins!')
                player1_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[9] == 'O' and board_layout[21] == 'O' and board_layout[33] == 'O':
                print('')
                print('Player 2 wins!')
                print('Player 2 wins!')
                print('Player 2 wins!')
                player1_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout.count('X') >= 5 or board_layout.count('O') >= 5:
                print('')
                print('It\'s a draw!')
                print('')
                time.sleep(2)
                main()
            else:
                player2_turn = True

    else:

        print("PLAYER 1 loses the coin toss! PLAYER 2 will go first...")
        time.sleep(2)
        print('')
        print(''.join(board_layout))

        # PLAYER TWO FIRST - EXECUTION

        while game_loop:

            # PLAYER 2 TURN
            while player2_turn:

                time.sleep(1)
                print('')
                print('PLAYER 2\'s turn!')
                print('')
                print("Choose a number that corresponds with where you wish to place your marker and press ENTER!")
                print('')

                player_choice = input(' ')
                if player_choice.isnumeric() and player_choice in board_layout:
                    marker_index = board_layout.index(player_choice)
                    board_layout.remove(player_choice)
                    board_layout.insert(marker_index, 'O')
                    available_positions.remove(player_choice)
                    print(''.join(board_layout))
                    player2_turn = False
                else:
                    print('')
                    print('Please use a valid input and press ENTER.')
                    print('')
                    time.sleep(1)
                    print(''.join(board_layout))
                    print('')

            # CHECK FOR PLAYER 2 WIN

            # HORIZONTALS
            if board_layout[0:11].count('O') == 3:
                print('')
                print('Player 2 wins!')
                print('Player 2 wins!')
                print('Player 2 wins!')
                player1_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[12:22].count('O') == 3:
                print('')
                print('Player 2 wins!')
                print('Player 2 wins!')
                print('Player 2 wins!')
                player1_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[23:34].count('O') == 3:
                print('')
                print('Player 2 wins!')
                print('Player 2 wins!')
                print('Player 2 wins!')
                player1_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()

            # DIAGONALS
            elif board_layout[1] == 'O' and board_layout[17] == 'O' and board_layout[33] == 'O':
                print('')
                print('Player 2 wins!')
                print('Player 2 wins!')
                print('Player 2 wins!')
                player1_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[9] == 'O' and board_layout[17] == 'O' and board_layout[25] == 'O':
                print('')
                print('Player 2 wins!')
                print('Player 2 wins!')
                print('Player 2 wins!')
                player1_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()

            # VERTICALS
            elif board_layout[1] == 'O' and board_layout[13] == 'O' and board_layout[25] == 'O':
                print('')
                print('Player 2 wins!')
                print('Player 2 wins!')
                print('Player 2 wins!')
                player1_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[5] == 'O' and board_layout[17] == 'O' and board_layout[29] == 'O':
                print('')
                print('Player 2 wins!')
                print('Player 2 wins!')
                print('Player 2 wins!')
                player1_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[9] == 'O' and board_layout[21] == 'O' and board_layout[33] == 'O':
                print('')
                print('Player 2 wins!')
                print('Player 2 wins!')
                print('Player 2 wins!')
                player1_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout.count('X') >= 5 or board_layout.count('O') >= 5:
                print('')
                print('It\'s a draw!')
                print('')
                time.sleep(2)
                main()
            else:
                player2_turn = True

            # PLAYER 1 TURN
            while player1_turn:

                time.sleep(1)
                print('')
                print('PLAYER 1\'s turn!')
                print('')
                print("Choose a number that corresponds with where you wish to place your marker and press ENTER!")
                print('')

                player_choice = input(' ')
                if player_choice.isnumeric() and player_choice in board_layout:
                    marker_index = board_layout.index(player_choice)
                    board_layout.remove(player_choice)
                    board_layout.insert(marker_index, 'X')
                    available_positions.remove(player_choice)
                    print(''.join(board_layout))
                    player1_turn = False
                else:
                    print('')
                    print('Please use a valid input and press ENTER.')
                    print('')
                    time.sleep(1)
                    print(''.join(board_layout))
                    print('')

            # CHECK FOR PLAYER 2 WIN

            # HORIZONTALS
            if board_layout[0:11].count('X') == 3:
                print('')
                print('Player 1 wins!')
                print('Player 1 wins!')
                print('Player 1 wins!')
                player2_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[12:22].count('X') == 3:
                print('')
                print('Player 1 wins!')
                print('Player 1 wins!')
                print('Player 1 wins!')
                player2_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[23:34].count('X') == 3:
                print('')
                print('Player 1 wins!')
                print('Player 1 wins!')
                print('Player 1 wins!')
                player2_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()

            # DIAGONALS
            elif board_layout[1] == 'X' and board_layout[17] == 'X' and board_layout[33] == 'X':
                print('')
                print('Player 1 wins!')
                print('Player 1 wins!')
                print('Player 1 wins!')
                player2_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[9] == 'X' and board_layout[17] == 'X' and board_layout[25] == 'X':
                print('')
                print('Player 1 wins!')
                print('Player 1 wins!')
                print('Player 1 wins!')
                player2_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()

            # VERTICALS
            elif board_layout[1] == 'X' and board_layout[13] == 'X' and board_layout[25] == 'X':
                print('')
                print('Player 1 wins!')
                print('Player 1 wins!')
                print('Player 1 wins!')
                player2_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[5] == 'X' and board_layout[17] == 'X' and board_layout[29] == 'X':
                print('')
                print('Player 1 wins!')
                print('Player 1 wins!')
                print('Player 1 wins!')
                player2_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout[9] == 'X' and board_layout[21] == 'X' and board_layout[33] == 'X':
                print('')
                print('Player 1 wins!')
                print('Player 1 wins!')
                print('Player 1 wins!')
                player2_turn = False
                game_loop = False
                print('')
                time.sleep(2)
                main()
            elif board_layout.count('X') >= 5 or board_layout.count('O') >= 5:
                print('')
                print('It\'s a draw!')
                print('')
                main()
            else:
                player1_turn = True



def main():

    # PRESENT WELCOME MESSAGE & ASK USER WHETHER TO PLAY WITH ONE PLAYER OR TWO

    welcome_message = "Welcome to Colby\'s Tic Tac Toe game!"
    print(welcome_message)
    player_count_message = input("One player or two players? -->: ")

    while True:

        if player_count_message == "1" or player_count_message == "One" or player_count_message == "one"\
                or player_count_message == "ONE":
            one_player()
            break

        elif player_count_message == "2" or player_count_message == "Two" or player_count_message == "two"\
                or player_count_message == 'TWO':
            two_player()
            break
        else:
            player_count_message = input("One player or two players? -->: ")


if __name__ == "__main__":
    main()

from display_board import DisplayBoard
from players_markers import PlayersMakers
from place_marker import PlaceMarker
from win_check import WinCheck
from check_position import CheckPosition

test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
position_place = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board = [' '] * 10

display_board = DisplayBoard()
players_markers = PlayersMakers()
place_marker = PlaceMarker()
win_check = WinCheck()
check_position = CheckPosition()
check_position.check_position(free_position=position_place)

game_round = 1
game_star = True
"""Game Start Here"""

print("""  _______         ______              ______              __             ____  ________  ___
 /_  __(_)____   /_  __/___ ______   /_  __/___  ___     / /_  __  __   / __ \/ ____/  |/  /
  / / / / ___/    / / / __ `/ ___/    / / / __ \/ _ \   / __ \/ / / /  / /_/ / /_  / /|_/ / 
 / / / / /__     / / / /_/ / /__     / / / /_/ /  __/  / /_/ / /_/ /  / _, _/ __/ / /  / /  
/_/ /_/\___/    /_/  \__,_/\___/    /_/  \____/\___/  /_.___/\__, /  /_/ |_/_/   /_/  /_/   
                                                            /____/                          
                                                            """)

while game_star:
    game_on = True
    player1_marker, player2_marker = players_markers.markers()


    def who_start_first():
        player_turn = True
        while player_turn:
            turn = input("Who would like to go first ('X' or 'O'): ").upper()
            if turn == 'X' or turn == 'O':
                return turn
            player_turn = False


    turn = who_start_first()

    while game_on:

        if game_round < 5:
            if turn == player1_marker:
                def player_one():
                    player_position = ''
                    display_board.display_board(board=board)
                    while player_position not in position_place:
                        player_position = int(input(f'Player {player1_marker} select a free position between (1-9): '))
                        if player_position in position_place:
                            break
                    place_marker.on_board(board, player1_marker, player_position)
                    position_place.remove(player_position)
                    display_board.display_board(board=board)


                player_one()
                turn = player2_marker
                game_round += 1
            elif turn == player2_marker:
                def player_two():
                    player_position = ''
                    display_board.display_board(board=board)
                    while player_position not in position_place:
                        player_position = int(input(f'Player {player2_marker} select a free position between (1-9): '))
                        if player_position in position_place:
                            break
                    place_marker.on_board(board, player2_marker, player_position)
                    position_place.remove(player_position)
                    display_board.display_board(board=board)


                player_two()
                turn = player1_marker
                game_round += 1
        elif game_round >= 5:
            if turn == player1_marker:
                if check_position.check_position(free_position=position_place):
                    def player_one():
                        player_position = ''
                        display_board.display_board(board=board)
                        while player_position not in position_place:
                            player_position = int(
                                input(f'Player {player1_marker} select a free position between (1-9): '))
                            if player_position in position_place:
                                break
                        place_marker.on_board(board, player1_marker, player_position)
                        position_place.remove(player_position)
                        display_board.display_board(board=board)


                    player_one()
                    if win_check.check_win(board=board, mark=player1_marker):
                        print('Game Over')
                        game_on = False
                    else:
                        turn = player2_marker
                        game_round += 1

                elif not check_position.check_position(free_position=position_place):
                    print("Tie Game 🤝")
                    game_on = False

            elif turn == player2_marker:
                if check_position.check_position(free_position=position_place):
                    def player_two():
                        player_position = ''
                        display_board.display_board(board=board)
                        while player_position not in position_place:
                            player_position = int(
                                input(f'Player {player2_marker} select a free position between (1-9): '))
                            if player_position in position_place:
                                break
                        place_marker.on_board(board, player2_marker, player_position)
                        position_place.remove(player_position)
                        display_board.display_board(board=board)


                    player_two()
                    if win_check.check_win(board=board, mark=player2_marker):
                        print('Game Over')
                        game_on = False
                    else:
                        turn = player1_marker
                        game_round += 1
                elif not check_position.check_position(free_position=position_place):
                    print("Tie Game 🤝")
                    game_on = False


    def replay_game():
        global game_star, board, position_place, game_round
        play_again = input("Would you like to replay te game ('Y'/'N'): ").upper()
        if play_again == 'Y':
            position_place = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            board = [' '] * 10
            game_round = 1
            game_star = True
        else:
            print('Thank you Good Bye!')
            game_star = False


    replay_game()

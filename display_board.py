class DisplayBoard:


    def display_board(self,board):
        """ This function is responsible for printing the board"""
        print('\n')
        print('____' * 3)
        print('|   ' * 4)
        print('| ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' |')
        print('|   ' * 4)
        print('____' * 3)
        print('|   ' * 4)
        print('| ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' |')
        print('|   ' * 4)
        print('____' * 3)
        print('|   ' * 4)
        print('| ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' |')
        print('|   ' * 4)
        print('____' * 3)

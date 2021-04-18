class WinCheck:
    def check_win(self,board, mark):
        """This function will check is teh current mark win the game"""
        if board[7] == board[8] == board[9] == mark or board[4] == board[5] == board[6] == mark or board[1] == \
                board[2] == board[3] == mark or board[1] == board[4] == board[7] == mark or board[2] == board[5] == \
                board[8] == mark or board[3] == board[6] == board[9] == mark or board[1] == board[5] == board[9] == \
                mark or board[3] == board[5] == board[7] == mark:

            print(f"player with mark '{mark}' won the game! Congratulation : ")
            return True
        else:
            return False

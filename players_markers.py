class PlayersMakers:
    def __init__(self):
        self.marker = ''

    def markers(self):
        """This function will take player input (marker) and assignee it to them """
        # self.marker = ''
        while self.marker != 'X' and self.marker != 'O':
            self.marker = input('player_1 please select a marker (X or O): ').upper()
        player_1 = self.marker
        if player_1 == 'X':
            player_2 = 'O'
            print('Player_1 marker is "X" and Player_2 marker is "O"')
        else:
            player_2 = 'X'
            print('Player1 marker is "O" and Player2 marker is "X"')
        return player_1, player_2

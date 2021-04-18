class PlaceMarker:
    #def __init__(self, board, marker, position):
    #    self.board = board
    #    self.marker = marker
    #    self.position = position
#
    def on_board(self, board, marker, position):
        """This function will accept a position and put the marker on the board """
        board[position] = marker

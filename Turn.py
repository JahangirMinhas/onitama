class Turn:
    """
    This class represents the current turn of a player.
    
    >>> print(Turn(0, 1, 3, 3, 'crab', 'player2'))
    None
    """
    row_: int
    col_o: int
    row_d: int
    col_d: int
    style_name: str
    player: str

    def __init__(self, row_o: int, col_o: int, row_d: int, col_d: int,
                 style_name: str, player: str) -> None:
        """
        This method initializes the turn of a player.
        """
        self.row_o = row_o
        self.col_o = col_o
        self.row_d = row_d
        self.col_d = col_d
        self.style_name = style_name
        self.player = player

from Player import Player
from typing import List, Union
from Style import Style
from Pieces import Pieces


class sizemustbeodd(Exception):
    """Exception raised if size is not odd.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, salary, message = "Size must be odd!"):
        self.message = message
        super().__init__(self.message)


class OnitamaBoard:
    """
    An OnitamaBoard class consisting of a game board, and keeping track of player token information and styles.
    It can set and clear the board and check if potential plays are valid through coordinate checking.

    === Attributes === 
    size : A board's width and height.
    player1 : Player object representing player who will play the G1 and M1 pieces.
    player2 : Player object representing player who will play the G2 and M2 pieces.
    styles :  A list of all possible play styles including: dragon, crab, horse, mantis, rooster.

    === Private Attributes ===
    _board : 
        A nested list representing a grid layout for the board.

    === Representation Invariants ===
    - Size is always an odd number greater or equal to 5.
    - player1 has G1 and M1 pieces.
    - player2 has G2 and M2 pieces.
    """
    size: int
    player1: Player
    player2: Player
    styles: List[Style]
    _board: List[List[str]]

    def __init__(self, size: int, player1: Player, player2: Player, board: Union[List[List[str]], None] = None) -> None:
        """
        Constructs an empty Onitama board. Places four monks and one grandmaster
        on opposite sides of the board. Creates five Styles and distributes them
        among the players.
        """
        if size % 2 == 0:
            raise sizemustbeodd()
        self.styles = []
        self.construct_styles()
        self.size = size
        self.player1 = player1
        self.player2 = player2
        if board is None:
            board = [[Pieces.EMPTY for i in range(size)] for i in range(size)]
            for i in range(size):
                for j in range(size):
                    if i == 0:
                        if j == int(size/2):
                            board[i][j] = Pieces.G1
                        else:
                            board[i][j] = Pieces.M1
                    elif i == size - 1:
                        if j == int(size/2):
                            board[i][j] = Pieces.G2
                        else:
                            board[i][j] = Pieces.M2
                    else:
                        board[i][j] = Pieces.EMPTY
            self.set_board(board)
        else:
            self.set_board(board)

    def construct_styles(self) -> None:
        """
        Constructs the 5 movement styles of Onitama for this board. Normally,
        there are 16 movement styles and they are distributed randomly, however for
        this assignment, you are only required to use 5 of them (Dragon, Crab, Horse,
        Mantis, and Rooster).

        You can find the movement patterns for these styles under assets/{style}.png,
        where {style} is one of the five styles mentioned above. Additionally, you
        can also find the images in README.md.

        IMPORTANT: Additionally, we are going to distribute the styles at the start
        of the game in a static or consistent manner. Player 1 (G1) must get the Crab
        and Horse styles. Player 2 (G2) must get the Mantis and Rooster styles. Extra
        (EMPTY) must get the Dragon style.

        Please be sure to follow the distribution of styles as mentioned above as
        this is important for testing. Failure to follow this distribution of styles
        will result in the LOSS OF A LOT OF MARKS.
        
        >>> player1 = Player('id1')
        >>> player2 = Player('id2')
        >>> board = OnitamaBoard(5, player1, player2)
        >>> board.construct_styles()

        >>> board.styles[0].owner == Pieces.G1
        True
        >>> board.styles[1].owner == Pieces.G1
        True
        >>> board.styles[2].owner == Pieces.G2
        True
        >>> board.styles[3].owner == Pieces.G2
        True
        >>> board.styles[4].owner == Pieces.EMPTY
        True
        """
        crab_move = [(-1, 0), (0, -2), (0, 2)]
        crab = Style(crab_move, 'crab', Pieces.G1)
        self.styles.append(crab)
        
        horse_move = [(-1, 0), (1, 0), (0, -1)]
        horse = Style(horse_move, 'horse', Pieces.G1)
        self.styles.append(horse)
        
        mantis_move = [(-1, -1), (-1, 1), (1, 0)]
        mantis = Style(mantis_move, 'mantis', Pieces.G2)
        self.styles.append(mantis)
        
        rooster_move = [(0, 1), (-1, 1), (0, -1), (1, -1)]
        rooster = Style(rooster_move, 'rooster', Pieces.G2)
        self.styles.append(rooster)

        dragon_move = [(-1, -2), (1, -1), (1, 1), (-1, 2)]
        dragon = Style(dragon_move, 'dragon', Pieces.EMPTY)
        self.styles.append(dragon)

    def exchange_style(self, style: Style) -> bool:
        """
        Exchange the given <style> with the empty style (the style whose owner is
        EMPTY). Hint: Exchanging will involve swapping the owners of the styles.

        Precondition: <style> cannot be the empty style.
        
        >>> player1 = Player('id1')
        >>> player2 = Player('id2')
        >>> board = OnitamaBoard(5, player1, player2)
        >>> board.construct_styles()
        >>> style = board.styles[0]
        >>> board.exchange_style(style)
        True
        >>> style.owner == Pieces.EMPTY
        True

        >>> player1 = Player('id1')
        >>> player2 = Player('id2')
        >>> board = OnitamaBoard(5, player1, player2)
        >>> board.construct_styles()
        >>> style = Style([(-3, -1)], 'new_style', Pieces.G2)
        >>> board.exchange_style(style)
        False
        
        >>> player1 = Player('id1')
        >>> player2 = Player('id2')
        >>> board = OnitamaBoard(5, player1, player2)
        >>> board.construct_styles()
        >>> style = board.styles[0]
        >>> style.owner = Pieces.EMPTY
        >>> board.exchange_style(style)
        False
        """
        if style in self.styles and style.owner != Pieces.EMPTY:
            for value in self.styles:
                if value.owner == Pieces.EMPTY:
                    value.owner, style.owner = style.owner, value.owner
                    return True
        return False

    def valid_coordinate(self, row: int, col: int) -> bool:
        """
        Returns true iff the provided coordinates are valid (exists on the board).
        
        >>> player1 = Player('id1')
        >>> player2 = Player('id2')
        >>> board = OnitamaBoard(5, player1, player2)

        >>> board.valid_coordinate(-1, -3)
        False
        
        >>> board.valid_coordinate(2, 3)
        True
        
        >>> board.valid_coordinate(5, 4)
        False
        """
        if row < self.size and col < self.size and row >= 0 and col >= 0:
            return True
        return False

    def get_token(self, row: int, col: int) -> str:
        """
        Returns the player token that is in the given <row> <col> position, or the empty
        character if no player token is there or if the position provided is invalid.
        
        >>> player1 = Player('id1')
        >>> player2 = Player('id2')
        >>> board = OnitamaBoard(5, player1, player2)

        >>> board.get_token(-1, -3)
        ' '
        
        >>> board.get_token(2, 3)
        ' '
        
        >>> board.get_token(4, 1)
        'y'
        """
        if self.valid_coordinate(row, col):
            return self._board[row][col]
        return Pieces.EMPTY

    def set_token(self, row: int, col: int, token: str) -> None:
        """
        Sets the given position on the board to be the given player (or throne/empty)
        <token>.
        
        >>> player1 = Player('id1')
        >>> player2 = Player('id2')
        >>> board = OnitamaBoard(5, player1, player2)
        >>> token = board.get_token(4, 3)
        >>> board.set_token(3, 3, token)
        >>> board.get_token(3, 3) == token
        True
        
        >>> player1 = Player('id1')
        >>> player2 = Player('id2')
        >>> board = OnitamaBoard(5, player1, player2)
        >>> token = board.get_token(0, 2)
        >>> board.set_token(1, 1, token)
        >>> board.get_token(1, 1) == token
        True
        
        >>> player1 = Player('id1')
        >>> player2 = Player('id2')
        >>> board = OnitamaBoard(5, player1, player2)
        >>> board.set_token(4, 4, Pieces.EMPTY)
        >>> board.get_token(4, 4) == Pieces.EMPTY
        True
        """
        self._board[row][col] = token

    def get_styles_deep_copy(self) -> List[Style]:
        """
        DO NOT MODIFY THIS!!!
        Returns a deep copy of the styles of this board.
        """
        return [style.__copy__() for style in self.styles]

    def deep_copy(self) -> List[List[str]]:
        """
        DO NOT MODIFY THIS!!! 
        Creates and returns a deep copy of this OnitamaBoard's
        current state.
        """
        return [row.copy() for row in self._board]

    def set_board(self, board: List[List[str]]) -> None:
        """
        DO NOT MODIFY THIS!!!
        Sets the current board's state to the state of the board which is passed in as a parameter.
        """
        self._board = [row.copy() for row in board]

    def __str__(self) -> str:
        """
        Returns a string representation of this game board.
        """
        s = '  '
        for col in range(self.size):
            s += str(col) + ' '

        s += '\n'

        s += ' +'
        for col in range(self.size):
            s += "-+"

        s += '\n'

        for row in range(self.size):
            s += str(row) + '|'
            for col in range(self.size):
                s += self._board[row][col] + '|'

            s += str(row) + '\n'

            s += ' +'
            for col in range(self.size):
                s += '-+'

            s += '\n'

        s += '  '
        for col in range(self.size):
            s += str(col) + ' '

        s += '\n'
        return s

if __name__ == '__main__': 
    import doctest
    doctest.testmod()
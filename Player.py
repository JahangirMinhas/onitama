from __future__ import annotations
from Pieces import Pieces
from Style import Style
from typing import Dict, List, Tuple, Union
from Turn import Turn
from random import randint


class Player:
    """
    This abstract class represents a player.
    This class should never be instantiated.
    """
    player_id: str

    def __init__(self, player_id: str) -> None:
        """
        This method initializes a player.
        """
        self.player_id = player_id

    def get_turn(self) -> None:
        """
        This is an abstract method which is to be implemented in the child
        class.
        """
        raise NotImplementedError

    def get_tokens(self) -> List[Tuple]:
        """
        This method returns a list of tuples in the form of (row, col) of the
        positions of all the pieces of the specified player.
        """
        board = self.onitama.get_board()
        tokens = []
        for i, row in enumerate(board):
            for j, token in enumerate(row):
                if token.lower() == self.player_id.lower():
                    tokens.append((i, j))
        return tokens

    def get_styles(self) -> List[Style]:
        """
        This method returns a list of styles for the player 'self'.
        """
        styles = []
        for sty in self.onitama.get_styles():
            if sty.owner == self.player_id:
                styles.append(sty)
        return styles

    def get_valid_turns(self) -> Dict:
        """
        This method returns a dictionary of all the legal movements that can be
        made by a player in his turn according to the style cards they currently
        have.
        """
        styles = self.get_styles()
        tokens = self.get_tokens()
        turns = {}
        for sty in styles:
            turns[sty.name] = []
            for row, col in tokens:
                for d_row, d_col in sty.get_moves():
                    # Flip move direction if player is X
                    if self.player_id == Pieces.G1:
                        d_row *= -1
                        d_col *= -1
                    # Check is_legal_move
                    if self.onitama.is_legal_move(row, col, row + d_row, col + d_col):
                        turns[sty.name].append(Turn(row, col, row + d_row,
                                                    col + d_col, sty.name, self.player_id))

        return turns

    def set_onitama(self, onitama):
        """
        This method initializes the attribute for the Onitama Game.
        """
        self.onitama = onitama


class PlayerRandom(Player):
    """
    This class is the child class for Player class.
    
    >>> player1 = PlayerRandom('X')
    >>> player1.get_styles()
    [crab, horse]
    >>> player1.get_tokens()
    [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
    """
    player_id: str

    def __init__(self, player_id) -> None:
        """
        This method initializes a PlayerRandom object.
        """
        super().__init__(player_id)

    def get_turn(self) :
        """
        This method is used in the RVR and HVR game modes where a random
        move needs to be made by the computer. Out of all the moves possible,
        this method chooses a move randomly to be made by the computer through
        a random style card available to the current player.
        """
        turns = []
        valid_turns = self.get_valid_turns()
        for style_name in valid_turns:
            turns.extend(valid_turns[style_name])

        # Return a random valid turn
        if len(turns) == 0:
            return None
        return turns[randint(0, len(turns) - 1)]

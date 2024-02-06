from __future__ import annotations
from typing import List, Tuple, Union
from Pieces import Pieces


class Style:
    """
    This class initializes a style.
    
    >>> style = Style([-2, 1]), 'style', Pieces.G1)
    >>> style.get_moves()
    [-2, 1]
    >>> style.copy()
    Style([-2, 1]), 'style', Pieces.G1)
    """
    name: str
    _moves: List[Tuple]
    owner: str

    def __init__(self, pairs: List[Tuple], name: str, owner: str = Pieces.EMPTY) -> None:
        """
        This class initializes a style object.
        """
        self.name = name
        self._moves = pairs.copy()
        self.owner = owner

    def get_moves(self) -> List[Tuple]:
        """
        This method copies and returns the movement rules for the style.
        """
        return self._moves.copy()

    def __eq__(self, other: Style) -> bool:
        """
        Checks if the name and owner of 'other' and 'self' are equal.
        """
        return self.name == other.name and self.owner == other.owner

    def __copy__(self) -> Style:
        """
        This method creates a copy of the style 'self' and returns it
        """
        return Style(self._moves.copy(), self.name, self.owner)

from typing import List
from OnitamaBoard import OnitamaBoard
from Player import Player, PlayerRandom
from Pieces import Pieces
from hypothesis import given
from hypothesis.strategies import integers

def test_construct_styles() -> None:
    """ 
    This test checks if 'construct_style' functions normally. This means that
    it must initially distribute the styles to the correct owners.
    """
    player1 = PlayerRandom('id1')
    player2 = PlayerRandom('id2')
    board = OnitamaBoard(5, player1, player2)
    board.construct_styles()

    crab = board.styles[0]
    horse = board.styles[1]
    mantis = board.styles[2]
    rooster = board.styles[3]
    dragon = board.styles[4]
    
    assert crab.owner == Pieces.G1
    assert horse.owner == Pieces.G1
    assert mantis.owner == Pieces.G2
    assert rooster.owner == Pieces.G2
    assert dragon.owner == Pieces.EMPTY
    
def test_exchange_styles() -> None:
    """
    This test checks if 'exchange_styles' functions normally.
    """
    player1 = PlayerRandom('id1')
    player2 = PlayerRandom('id2')
    board = OnitamaBoard(5, player1, player2)
    board.construct_styles()
    
    assert board.styles[0].owner == Pieces.G1
    board.exchange_style(board.styles[0])
    assert board.styles[0].owner == Pieces.EMPTY
    assert board.styles[4].owner == Pieces.G1

@given(row = integers(min_value = -1, max_value = 6), col = integers(min_value = -1, max_value = 6))
def test_valid_coordinate(row, col) -> None:
    """
    This test checks if 'valid_coordinate' works normally.
    """
    player1 = PlayerRandom('id1')
    player2 = PlayerRandom('id2')
    board = OnitamaBoard(5, player1, player2)
    board.construct_styles()
    
    if row < 0 or col < 0 or row > 4 or col > 4:
        assert board.valid_coordinate(row, col) == False
    else:
        assert board.valid_coordinate(row, col) == True

def test_get_set_token() -> None:
    """
    This test checks if 'get_token' and 'set_token' works properly.
    """
    player1 = PlayerRandom('id1')
    player2 = PlayerRandom('id2')
    board = OnitamaBoard(5, player1, player2)
    board.construct_styles()
    
    assert board.get_token(0, 2) == Pieces.G1
    board.set_token(0, 2, Pieces.M1)
    assert board.get_token(0, 2) == Pieces.M1
    
    # Out of bounds test
    assert board.get_token(-1, 2) == Pieces.EMPTY


if __name__ == '__main__':
    import pytest
    pytest.main(['OnitamaBoard_Tests.py'])
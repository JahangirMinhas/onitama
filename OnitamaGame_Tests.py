from typing import List
from OnitamaGame import OnitamaGame
from Player import Player, PlayerRandom
from Pieces import Pieces

def test_other_player() -> None:
    """ 
    This test checks if 'other_player' functions normally.
    """
    player1 = PlayerRandom('id1')
    player2 = PlayerRandom('id2')
    game = OnitamaGame(5, player1, player2)
    assert game.other_player(game.player2).player_id == 'id1'

def test_get_token() -> None:
    """
    This test checks if 'get_token' functions normally.
    """
    player1 = PlayerRandom('id1')
    player2 = PlayerRandom('id2')
    game = OnitamaGame(5, player1, player2)
    assert game.get_token(0, int(game.size / 2)) == Pieces.G1
    
def test_is_legal_move1() -> None:
    """
    This test checks if 'is_legal_move' correctly handles when a piece is trying
    to exit the board boundaries.
    """
    player1 = PlayerRandom('id1')
    player2 = PlayerRandom('id2')
    game = OnitamaGame(5, player1, player2)
    assert game.is_legal_move(0, 1, 6, -2) == False
    
def test_is_legal_move2() -> None:
    """
    This test checks if 'is_legal_move' correctly handles when a piece is trying
    to kill one of its own pieces.
    """
    player1 = PlayerRandom('id1')
    player2 = PlayerRandom('id2')
    game = OnitamaGame(5, player1, player2)
    assert game.is_legal_move(0, 1, 0, 2) == False

def test_is_legal_move3() -> None:
    """
    This test checks if 'is_legal_move' correctly handles when a player is trying
    to move the opponent's pieces.
    """
    player1 = PlayerRandom('id1')
    player2 = PlayerRandom('id2')
    game = OnitamaGame(5, player1, player2)
    assert game.is_legal_move(4, 2, 2, 3) == False

def test_move() -> None:
    """
    This test checks if the move method functions normally.
    """
    player1 = PlayerRandom('id1')
    player2 = PlayerRandom('id2')
    game = OnitamaGame(5, player1, player2)    
    token = game.get_token(0, 2)
    game.move(0, 2, 1, 2, 'crab')
    assert game.get_token(1, 2) == token

def test_player1_win_by_throne() -> None:
    """
    This test includes moving multiple pieces on the board to make player1
    win the game by taking over the opponent's throne. Therefore it tests the
    following methods:
    
    other_player: there are assert statements before and after the moves
    which check if the move method, which uses the 'other_player' method, 
    correctly switches the turns of the players.
    
    get_token: there are assert statements before and after moves which
    check if a move has been correctly made by getting the token before and
    after the move and checking if the same token is in the correct place
    after the move.
    
    move: There are multiple moves being made throughout the test. These moves
    are checked everytime with assert statements by getting the token before and
    after the move and checking if the same token is in the correct place
    after the move.
    
    get_winner: There is an assert statement during the moves which checks
    if there is a winner without any of the winning conditions being met.
    After player1 takes player2's throne, there is another assert statement
    which checks if the correct winner is returned - player1.
    """
    player1 = PlayerRandom('id1')
    player2 = PlayerRandom('id2')
    game = OnitamaGame(5, player1, player2)

    token = game.get_token(0, 2)
    # Check if correct player's turn
    assert game.whose_turn == player1
    game.move(0, 2, 1, 2, 'crab')
    # Check if move correctly made
    assert game.get_token(1, 2) == token

    token = game.get_token(4, 2)
    # Check if correct player's turn
    assert game.whose_turn == player2    
    game.move(4, 2, 3, 3, 'mantis')
    # Check if move correctly made
    assert game.get_token(3, 3) == token
    
    # Check get_winner at this point. There should be no winners.
    assert game.get_winner() == None
    
    token = game.get_token(1, 2)
    # Check if correct player's turn
    assert game.whose_turn == player1
    game.move(1, 2, 4, 2, 'horse')
    # Check if move correctly made
    assert game.get_token(4, 2) == token   
    
    # Check if player1 has won the game.
    assert game.get_winner() == player1

def test_player2_win_by_kill() -> None:
    """
    This test includes moving multiple pieces on the board to make player2
    win the game by killing the opponent's GM. Therefore it tests the
    following methods:
    
    other_player: there are assert statements before and after the moves
    which check if the move method, which uses the 'other_player' method, 
    correctly switches the turns of the players.
    
    get_token: there are assert statements before and after moves which
    check if a move has been correctly made by getting the token before and
    after the move and checking if the same token is in the correct place
    after the move.
    
    move: There are multiple moves being made throughout the test. These moves
    are checked everytime with assert statements by getting the token before and
    after the move and checking if the same token is in the correct place
    after the move.
    
    get_winner: There is an assert statement during the moves which checks
    if there is a winner without any of the winning conditions being met.
    After player1 takes player2's throne, there is another assert statement
    whiich checks if the correct winner is returned - player2.
    """
    player1 = PlayerRandom('id1')
    player2 = PlayerRandom('id2')
    game = OnitamaGame(5, player1, player2)

    token = game.get_token(0, 2)
    # Check if correct player's turn
    assert game.whose_turn == player1
    game.move(0, 2, 1, 2, 'crab')
    # Check if move correctly made
    assert game.get_token(1, 2) == token
    
    # Check get_winner at this point. There should be no winners.
    assert game.get_winner() == None    

    token = game.get_token(4, 2)
    # Check if correct player's turn
    assert game.whose_turn == player2    
    game.move(4, 2, 1, 2, 'mantis')
    # Check if move correctly made
    assert game.get_token(1, 2) == token
    
    # Check if player2 has won the game.
    assert game.get_winner() == player2

def test_undo1() -> None:
    """
    This test checks if the undo method works for a move.
    Tests the style and the move.
    """
    player1 = PlayerRandom('id1')
    player2 = PlayerRandom('id2')
    game = OnitamaGame(5, player1, player2)    
    token = game.get_token(0, 2)
    
    crab = None
    for style in game.get_styles():
        if style.name == 'crab':
            crab = style.owner

    game.move(0, 2, 1, 2, 'crab')
    assert game.get_token(1, 2) == token    

    game.undo()
    
    assert crab == Pieces.G1
    assert game.get_token(0, 2) == token

def test_undo_win() -> None:
    """
    This test checks if the undo method works for after a plyer has won the
    game.
    Tests the style and the move.
    """
    player1 = PlayerRandom('id1')
    player2 = PlayerRandom('id2')
    game = OnitamaGame(5, player1, player2)

    token = game.get_token(0, 2)
    # Check if correct player's turn
    assert game.whose_turn == player1
    game.move(0, 2, 1, 2, 'crab')
    # Check if move correctly made
    assert game.get_token(1, 2) == token
    
    # Check get_winner at this point. There should be no winners.
    assert game.get_winner() == None    

    token = game.get_token(4, 2)
    # Check if correct player's turn
    
    mantis = None
    for style in game.get_styles():
        if style.name == 'mantis':
            mantis = style.owner

    assert game.whose_turn == player2
    game.move(4, 2, 1, 2, 'mantis')
    # Check if move correctly made
    assert game.get_token(1, 2) == token
    
    # Check if player2 has won the game.
    assert game.get_winner() == player2

    game.undo()
    
    assert mantis == Pieces.G2
    assert game.get_token(4, 2) == token

def test_undo_initial_state() -> None:
    """
    This test checks if the undo button works on the initial state of the game
    and does not crash the program.
    Tests the board and the style.
    """  
    player1 = PlayerRandom('id1')
    player2 = PlayerRandom('id2')
    game = OnitamaGame(5, player1, player2)
    board = game.get_board()
    styles = game.get_styles()
    game.undo()
    assert board == game.get_board()
    assert styles == game.get_styles()

if __name__ == '__main__':
    import pytest
    pytest.main(['OnitamaGame_Tests.py'])
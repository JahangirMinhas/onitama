from typing import List, Tuple

class OnitamaStack:
    """
    A stack representing Onitama Game Boards.
    """
    _items: List

    def __init__(self) -> None:
        """
        Initializes the stack.
        """
        self._items = []

    def pop(self) -> Tuple:
        """
        Pop an item from the stack.
        """
        styles = self._items.pop()
        board = self._items.pop()
        return (board, styles)

    def push(self, board: any, styles: any) -> None:
        """
        Push an item to the stack.
        """
        self._items.append(board)
        self._items.append(styles)
    
    def empty(self) -> bool:
        """
        Check if stack is empty.
        """
        return self._items == []
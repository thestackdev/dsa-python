from typing import List

from tries.base import TrieNodeWithWord


class Solution:
    def __init__(self) -> None:
        self.result = []
        self.root = TrieNodeWithWord()

    def search_words(self, board: List[List[str]], words: List[str]) -> None:
        for word in words:
            node = self.root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNodeWithWord()

                node = node.children[c]

        for row in range(len(board)):
            for col in range(len(board[0])):
                self.dfs(board, row, col, self.root)

    def dfs(self, board: List[List[str]], row: int, col: int, node: TrieNodeWithWord):
        if node.word:
            self.result.append(node.word)

            return None

        temp = board[row][col]
        board[row][col] = "#"

        dirs = ([-1, 0], [0, 1], [-1, 0], [1, 0])

        for dir in dirs:
            next_row, next_col = row + dir[0], col + dir[1]

            if (
                self.is_within_bounds(next_row, next_col, board)
                and board[next_row][next_col] in node.children
            ):
                self.dfs(
                    board, next_row, next_col, node.children[board[next_row][next_col]]
                )

        board[row][col] = temp

    def is_within_bounds(self, row: int, col: int, board: List[List[str]]) -> bool:
        return 0 <= row < len(board) and 0 <= col < len(board[0])

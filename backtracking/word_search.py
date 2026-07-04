from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def solve(self, board: List[List[str]], word: str) -> bool:
        is_found = False

        rows, cols = len(board), len(board[0])

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if self.backtrack(
                        row,
                        col,
                        board,
                        word,
                        board[row][col],
                        set(str(row) + str(col) + board[row][col]),
                    ):
                        return True

        return is_found

    def backtrack(
        self,
        row: int,
        col: int,
        board: List[List[str]],
        word: str,
        candidate: str,
        used: set,
    ) -> bool:

        if candidate == word:
            return True

        if len(candidate) > len(word):
            return False

        dirs = ([-1, 0], [0, -1], [0, 1], [1, 0])

        for dir in dirs:
            next_row, next_col = row + dir[0], col + dir[1]

            if (
                self.is_within_bounds(next_row, next_col, board)
                and str(next_row) + str(next_col) + board[next_row][next_col]
                not in used
                and board[next_row][next_col] == word[len(candidate)]
            ):
                _key = str(next_row) + str(next_col) + board[next_row][next_col]
                candidate += board[next_row][next_col]
                used.add(_key)

                result = self.backtrack(
                    next_row, next_col, board, word, candidate, used
                )
                if result:
                    return True

                candidate = candidate[:-1]
                used.remove(_key)

        return False

    def is_within_bounds(self, row: int, col: int, board: List[List[str]]) -> bool:
        return 0 <= row < len(board) and 0 <= col < len(board[0])


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.solve(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"
        )
    )

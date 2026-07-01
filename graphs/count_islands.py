from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def count_islands(self, matrix: List[List[int]]) -> int:
        count = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 1:
                    self.dfs(row, col, matrix)
                    count += 1

        return count

    def dfs(self, row: int, col: int, matrix: List[List[int]]):
        matrix[row][col] = -1

        dirs = ([-1, 0], [1, 0], [0, -1], [0, 1])

        for dir in dirs:
            next_row, next_col = row + dir[0], col + dir[1]
            if (
                self.is_within_bounds(next_row, next_col, matrix)
                and matrix[next_col][next_col] == 1
            ):
                self.dfs(next_row, next_col, matrix)

    def is_within_bounds(self, row: int, col: int, matrix: List[List[int]]) -> bool:
        return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])

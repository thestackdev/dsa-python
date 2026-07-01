from collections import deque
from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def infect(self, matrix: List[List[int]]) -> int:

        dirs = ([-1, 0], [1, 0], [0, -1], [0, 1])
        ones = seconds = 0

        queue = deque()

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 1:
                    ones += 1
                elif matrix[row][col] == 2:
                    queue.append(matrix[row][col])

        while queue and ones > 0:
            seconds += 1
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dir in dirs:
                    next_row, next_col = row + dir[0], col + dir[1]

                    if (
                        self.is_within_bounds(next_row, next_col, matrix)
                        and matrix[next_col][next_col] == 1
                    ):
                        matrix[next_row][next_col] = 2
                        ones -= 1
                        queue.append([next_row, next_col])

        return seconds

    def is_within_bounds(self, row: int, col: int, matrix: List[List[int]]) -> bool:
        return 0 <= row < len(matrix) and 0 <= col <= len(matrix[0])

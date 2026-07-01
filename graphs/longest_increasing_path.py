from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def longest_increasing_path(self, graph: List[List[int]]) -> int:
        rows, cols = len(graph), len(graph[0])

        # null matrix
        memo = [[0] * cols for _ in range(rows)]
        max_path = 0

        for row in range(rows):
            for col in range(cols):
                max_path = max(max_path, self.dfs(row, col, graph, memo))

        return max_path

    def dfs(
        self, row: int, col: int, graph: List[List[int]], memo: List[List[int]]
    ) -> int:
        if memo[row][col] != 0:
            return memo[row][col]

        max_path = 1

        dirs = ([-1, 0], [0, -1], [0, 1], [1, 0])

        for dir in dirs:
            next_row, next_col = row + dir[0], col + dir[1]

            if (
                self.is_within_bounds(next_row, next_col, graph)
                and graph[next_row][next_col] > graph[row][col]
            ):
                max_path = max(max_path, 1 + self.dfs(next_row, next_col, graph, memo))

        memo[row][col] = max_path

        return max_path

    def is_within_bounds(self, row: int, col: int, graph: List[List[int]]) -> bool:
        return 0 <= row < len(graph) and 0 <= col < len(graph[0])

from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def solve(self, rows: int, cols: int) -> int:
        matrix = [[0] * cols for _ in range(rows)]
        return self.top_down(0, 0, matrix)

    def top_down(self, row: int, col: int, matrix: List[List[int]]) -> int:
        if row == len(matrix[0]) - 1 or col == len(matrix) - 1:
            return 1

        if matrix[row][col] != 0:
            return matrix[row][col]

        dirs = ([1, 0], [0, 1])

        result = 0

        for dir in dirs:
            next_row, next_col = row + dir[0], col + dir[1]

            if self.is_within_bounds(next_row, next_col, matrix):
                result += self.top_down(next_row, next_col, matrix)

        matrix[row][col] = result

        return result

    def is_within_bounds(self, row: int, col: int, matrix: List[List[int]]) -> bool:
        return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])

    def bottom_up(self, rows: int, cols: int) -> int:
        dp = [[1] * cols for _ in range(rows)]

        for row in range(1, rows):
            for col in range(1, cols):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[rows - 1][cols - 1]

    def bottom_up_optimised(self, m: int, n: int) -> int:
        rows = [1] * n
        cols = [1] * m

        for row in range(1, n):
            for col in range(1, m):
                result = rows[row] + cols[col]
                rows[row] = result
                cols[col] = result

        return rows[n - 1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve(3, 3))
    print(solution.bottom_up(3, 3))
    print(solution.bottom_up_optimised(3, 3))

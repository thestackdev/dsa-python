from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def solve(self, matrix: List[List[int]]):

        rows = len(matrix)
        cols = len(matrix[0])

        row_set = set()
        col_set = set()

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    row_set.add(row)
                    col_set.add(col)

        for row in row_set:
            for col in range(cols):
                matrix[row][col] = 0

        for col in col_set:
            for row in range(rows):
                matrix[row][col] = 0

        print(matrix)


if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4, 5],
        [6, 0, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 0],
    ]
    solution = Solution()
    solution.solve(matrix)

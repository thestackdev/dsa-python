class Solution:
    def __init__(self) -> None:
        self.count: int = 0

    def solve(self, n: int) -> int:

        self.dfs(n, 0, set(), set(), set())
        return self.count

    def dfs(
        self, n: int, row: int, cols: set, diagnols: set, anti_diagnols: set
    ) -> None:

        if row == n:
            self.count += 1

        for col in range(n):
            if col in cols or (row - col) in diagnols or (row + col) in anti_diagnols:
                continue

            cols.add(col)
            diagnols.add(row - col)
            anti_diagnols.add(row + col)

            self.dfs(n, row + 1, cols, diagnols, anti_diagnols)

            cols.remove(col)
            diagnols.remove(row - col)
            anti_diagnols.remove(row + col)


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve(4))


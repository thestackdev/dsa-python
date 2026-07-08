from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def solve(self, candies: List[int]) -> int:
        n = len(candies)
        dp = [1] * n

        for i in range(1, n):
            if candies[i] > candies[i - 1]:
                dp[i] = dp[i] + 1

        for i in range(n - 2, -1, -1):
            if candies[i] > candies[i + 1] and dp[i] <= dp[i + 1]:
                dp[i] = max(dp[i + 1] + 1, dp[i])

        return sum(dp)


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve([4, 3, 2, 4, 5, 1]))

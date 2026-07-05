from typing import Dict, List


class Solution:
    def __init__(self) -> None:
        pass

    def top_down(self, coins: List[int], target: int) -> int:
        result = self.min_coins(coins, target, {})
        return result if result != float("inf") else -1

    def min_coins(self, coins: List[int], target: int, memo: Dict[int, int]) -> int:
        if target == 0:
            return 0

        if target in memo:
            return memo[target]

        min_coins = float("inf")

        for coin in coins:
            if coin <= target:
                min_coins = min(
                    min_coins, 1 + self.min_coins(coins, target - coin, memo)
                )

        memo[target] = min_coins
        return min_coins

    def bottom_up(self, coins: List[int], target: int) -> int:
        dp = [float("inf")] * (target + 1)

        dp[0] = 0

        for i in range(1, target + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        return dp[target] if dp[target] != float("inf") else -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.top_down([1, 2, 3], 5))
    print(solution.bottom_up([1, 2, 3], 5))

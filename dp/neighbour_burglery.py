from typing import Dict, List


class Solution:
    def __init__(self) -> None:
        pass

    def solve(self, neighbours: List[int]) -> int:
        result = self.top_down(0, neighbours, {})
        return result

    def top_down(
        self, current_neighbour: int, neighbours: List[int], memo: Dict[int, int]
    ) -> int:
        if current_neighbour >= len(neighbours):
            return 0

        rob_it = neighbours[current_neighbour] + self.top_down(
            current_neighbour + 2, neighbours, memo
        )
        skip_it = self.top_down(current_neighbour + 1, neighbours, memo)

        memo[current_neighbour] = max(rob_it, skip_it)

        return memo[current_neighbour]

    def bottom_up(self, neighbours: List[int]) -> int:
        dp = [0] * (len(neighbours) + 2)

        for i in range(2, len(dp)):
            dp[i] = max(dp[i - 1], neighbours[i - 2] + dp[i - 2])

        return dp.pop()


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve([100, 200, 300, 400]))
    print(solution.bottom_up([100, 200, 300, 400]))

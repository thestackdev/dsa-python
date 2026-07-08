from operator import ne
from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def solve(self, stations: List[int], values: List[int]) -> int:
        start = 0
        tank = 0
        total = 0

        for i in range(len(stations)):
            net_budget = stations[i] - values[i]

            tank += net_budget
            total += tank

            if tank <= 0:
                start += 1
                tank = 0

        return 1 if total >= 0 else -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve([2, 5, 1, 3], [3, 2, 1, 4]))


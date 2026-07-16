from collections import defaultdict
from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def solve(self, nums: List[int], k: int) -> int:
        count = 0
        running_sum = 0

        prefix_sum_freqs = defaultdict(int)
        prefix_sum_freqs[0] = 1

        for num in nums:
            running_sum += num
            count += prefix_sum_freqs[running_sum - k]
            prefix_sum_freqs[running_sum] += 1

        return count


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve([1, 2, 3, -3, 1], 3))

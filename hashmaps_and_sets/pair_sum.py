from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def solve(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            if (target - num) in seen:
                return [seen[target - num], i]

            seen[num] = i

        return []


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve([-1, 3, 4, 2], 3))

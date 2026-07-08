from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def solve(self, nums: List[int]) -> List[int]:
        counts = [0] * (max(nums) + 1)
        result = []

        for num in nums:
            counts[num] += 1

        for i, val in enumerate(counts):
            result.extend([i] * val)

        return result


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.solve([3, 4, 5, 3, 234, 234, 23, 42, 2123, 234, 12, 1, 3, 5, 52, 33])
    )

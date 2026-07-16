from typing import List


class Solution:
    def __init__(self) -> None:
        self.nums = []

    def prefix_sum(self, nums: List[int]) -> None:
        self.nums.append(nums[0])
        for num in nums[1:]:
            self.nums.append(self.nums[-1] + num)

    def sum_range(self, start: int, end: int) -> int:
        if start < 0 or end > len(self.nums):
            return 0

        if start == 0:
            return self.nums[end]

        return self.nums[end] - self.nums[start - 1]


if __name__ == "__main__":
    solution = Solution()
    solution.prefix_sum([3, -7, 6, 0, -2, 5])
    print(solution.sum_range(0, 3))
    print(solution.sum_range(2, 4))
    print(solution.sum_range(2, 2))

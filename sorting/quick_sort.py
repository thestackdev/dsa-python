from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def solve(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums

    def quick_sort(self, nums: List[int], left: int, right: int) -> None:

        if left >= right:
            return

        pivot = self.partition(nums, left, right)

        self.quick_sort(nums, left, pivot - 1)
        self.quick_sort(nums, pivot + 1, right)

    def partition(self, nums: List[int], left: int, right: int) -> int:
        selected_index = right

        p1 = left

        for i in range(left, right):
            if nums[selected_index] > nums[i]:
                nums[p1], nums[i] = nums[i], nums[p1]
                p1 += 1

        nums[p1], nums[selected_index] = nums[selected_index], nums[p1]

        return p1


if __name__ == "__main__":
    solution = Solution()
    nums = [6, 8, 4, 2, 7, 3, 5, 1]
    solution.solve(nums)
    print(nums)

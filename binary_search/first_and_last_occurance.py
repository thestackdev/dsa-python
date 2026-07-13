from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def lower_bound_binary_search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                right = mid - 1

        return left if nums[left] == target else -1

    def upper_bound_binary_search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return right if nums[right] == target else -1

    def solve(self, nums: List[int], target: int) -> List[int]:
        lower_bound = self.lower_bound_binary_search(nums, target)
        upper_bound = self.upper_bound_binary_search(nums, target)

        return [lower_bound, upper_bound]


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve([1, 2, 3, 4, 4, 4, 5, 6, 7], 4))

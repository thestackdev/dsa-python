from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def solve(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return left


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve([1, 2, 4, 5, 7, 8, 9], 4))

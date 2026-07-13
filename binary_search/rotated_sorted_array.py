from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def solve(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve([8, 9, 1, 2, 3, 4, 5, 6, 7], 1))

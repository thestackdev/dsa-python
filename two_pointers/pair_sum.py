from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def solve(self, nums: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(nums) - 1

        while p1 < p2:
            current_sum = nums[p1] + nums[p2]
            if current_sum == target:
                return [p1, p2]
            elif current_sum > target:
                p2 -= 1
            else:
                p1 += 1

        return []


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve([-5, -2, 3, 4, 6], 7))
    print(solution.solve([1, 1, 1], 2))

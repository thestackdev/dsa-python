from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def solve(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        for i in range(1, n):
            result[i] = result[i - 1] * nums[i - 1]

        current_product = 1

        for j in range(n - 1, -1, -1):
            result[j] = current_product * result[j]
            current_product = nums[j] * current_product

        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve([2, 3, 1, 4, 5]))

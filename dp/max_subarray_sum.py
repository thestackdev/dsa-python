from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def solve(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        current_sum = 0

        for num in nums:
            current_sum = max(current_sum + num, num)
            max_sum = max(max_sum, current_sum)

        return max_sum

    def max_subarray_dp(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        dp = [0] * len(nums)
        dp[0] = nums[0]
        max_sum = dp[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            max_sum = max(dp[i], max_sum)

        return max_sum


if __name__ == "__main__":
    nums = [3, 1, -6, 2, -1, 4, -9]
    solution = Solution()
    print(solution.solve(nums))
    print(solution.max_subarray_dp(nums))

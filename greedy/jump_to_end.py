from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def solve(self, nums: List[int]) -> bool:
        destination = 0

        for i in range(len(nums)):
            if i > destination:
                return False

            destination = max(destination, i + nums[i])

        return True

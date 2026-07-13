from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def solve(self, heights: List[int], k: int) -> int:
        left = 0
        right = max(heights)

        while left < right:
            mid = left + (right - left) // 2

            if self.cut_wood(heights, mid, k):
                return mid
            else:
                right = mid - 1

        return right

    def cut_wood(self, heights: List[int], height: int, k: int) -> bool:
        wood_collected = 0
        for num in heights:
            if num > height:
                wood_collected += height - num

        return wood_collected >= k

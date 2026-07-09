from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def solve(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            max_area = max(max_area, area)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return max_area


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve([2, 7, 8, 3, 7, 6]))

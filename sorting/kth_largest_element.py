import heapq
from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def sovle(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)

            elif num > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, num)

        return min_heap[0]

    def solve_quick_sort(self, nums: List[int], k: int) -> int:
        n = len(nums)

        pivot_index = n - k
        pivot_ptr = 0

        for i in range(len(nums)):
            if nums[i] < nums[pivot_index]:
                nums[i], nums[pivot_ptr] = nums[pivot_ptr], nums[i]
                pivot_ptr += 1

        return nums[pivot_ptr]


if __name__ == "__main__":
    solution = Solution()
    print(solution.sovle([5, 2, 4, 3, 1, 6], 3))
    print(solution.solve_quick_sort([5, 2, 4, 3, 1, 6], 3))

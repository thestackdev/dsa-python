import heapq


class Solution:
    def __init__(self) -> None:
        self.left_half = []
        self.right_half = []

    def add(self, num: int) -> None:
        if not self.left_half or num <= -self.left_half[0]:
            heapq.heappush(self.left_half, -num)

            if len(self.left_half) > len(self.right_half) + 1:
                heapq.heappush(self.right_half, -heapq.heappop(self.left_half))

        else:
            heapq.heappush(self.right_half, num)

            if len(self.left_half) < len(self.right_half):
                heapq.heappush(self.left_half, -heapq.heappop(self.right_half))

    def get_median(self) -> int:
        if len(self.left_half) == len(self.right_half):
            return (-self.left_half[0] + self.right_half[0]) / 2.0
        else:
            return -self.left_half[0]


if __name__ == "__main__":
    solution = Solution()
    solution.add(1)
    solution.add(2)
    solution.add(3)
    solution.add(4)
    # solution.add(5)
    print(solution.get_median())

from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def solve(self, nums: List[int]) -> List[int]:
        res = []

        stack = []

        for i in range(len(nums) - 1, -1, -1):
            while stack and stack[-1] < nums[i]:
                stack.pop()

            if not stack:
                res.append(-1)
            else:
                res.append(stack[-1])

            stack.append(nums[i])

        res.reverse()

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve([5, 2, 4, 6, 1]))

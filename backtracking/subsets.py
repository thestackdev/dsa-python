from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def solve(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrack(nums, [], 0, result)
        return result

    def backtrack(
        self,
        nums: List[int],
        candidate: List[int],
        current_index: int,
        result: List[List[int]],
    ) -> None:

        if current_index == len(nums):
            result.append(candidate[:])
            return None

        candidate.append(nums[current_index])
        self.backtrack(nums, candidate, current_index + 1, result)

        candidate.pop()
        self.backtrack(nums, candidate, current_index + 1, result)


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve([4, 5, 6]))

from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def solve(self, nums: List[int]) -> List[List[int]]:
        result = []

        self.backtrack(nums, [], set(), result)

        return result

    def backtrack(
        self,
        nums: List[int],
        candidate: List[int],
        used: set,
        result: List[List[int]],
    ) -> None:

        if len(candidate) == len(nums):
            result.append(candidate[:])
            return None

        for i in range(len(nums)):
            if nums[i] not in used:
                candidate.append(nums[i])
                used.add(nums[i])

                self.backtrack(nums, candidate, used, result)

                candidate.pop()
                used.remove(nums[i])

        return None


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve([4, 5, 6]))

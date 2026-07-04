from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def combinations(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtack(nums, [], set(), result)
        return result

    def backtack(
        self,
        nums: List[int],
        candidate: List[int],
        used: set[int],
        result: List[List[int]],
    ) -> None:
        if len(nums) == len(candidate):
            result.append(candidate[:])
            return

        for i, num in enumerate(nums):
            if i in used:
                continue

            candidate.append(num)
            used.add(i)

            self.backtack(nums, candidate, used, result)

            candidate.pop()
            used.remove(i)

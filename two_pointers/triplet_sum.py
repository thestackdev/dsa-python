from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def two_sum(self, nums: List[int], start: int, target: int) -> List[List[int]]:
        left = start
        right = len(nums) - 1
        pairs = []

        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                pairs.append([nums[left], nums[right]])

                left += 1
                right -= 1

                if nums[left] == nums[left - 1]:
                    left += 1

                if nums[right] == nums[right + 1]:
                    right -= 1

            elif current_sum > target:
                right -= 1
            else:
                left += 1

        return pairs

    def triplet_sum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            pairs = self.two_sum(nums, i + 1, -nums[i])
            for pair in pairs:
                triplets.append(pair + [nums[i]])

        return triplets


if __name__ == "__main__":
    solution = Solution()
    print(solution.triplet_sum([0, -1, 2, -3, 1]))


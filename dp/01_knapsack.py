from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def solve(self, cap: int, weights: List[int], values: List[int]) -> int:
        return self.top_down(
            cap,
            weights,
            values,
            0,
        )

    def top_down(
        self, cap: int, weights: List[int], values: List[int], current_index: int
    ) -> int:
        if current_index >= len(weights):
            return 0

        skip_it = self.top_down(cap, weights, values, current_index + 1)

        if cap < weights[current_index]:
            return skip_it

        add_it = values[current_index] + self.top_down(
            cap - weights[current_index], weights, values, current_index + 1
        )

        return max(add_it, skip_it)


if __name__ == "__main__":
    solution = Solution()
    # print(solution.solve(50, [10, 20, 30], [60, 100, 120]))
    # print(solution.solve(0, [10, 20, 30], [60, 100, 120]))
    # print(solution.solve(10, [5, 4, 6], [10, 40, 30]))
    # print(solution.solve(10, [10, 1, 1, 1], [100, 1, 1, 1]))
    print(solution.solve(3, [10, 1, 1, 1], [100, 1, 1, 1]))

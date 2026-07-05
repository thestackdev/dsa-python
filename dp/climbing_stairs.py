class Solution:
    def __init__(self) -> None:
        self.memo = {}

    def solve(self, n: int) -> int:
        if n <= 2:
            return n

        one_step_before, two_steps_before = 2, 1

        for _ in range(3, n + 1):
            current = one_step_before + two_steps_before
            two_steps_before = one_step_before
            one_step_before = current

        return one_step_before


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve(4))

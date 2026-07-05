class Solution:
    def __init__(self) -> None:
        pass

    def solve(self, s1: str, s2: str) -> int:
        return self.top_down(s1, s2, 0, 0)

    def top_down(self, s1: str, s2: str, s1_index: int, s2_index: int) -> int:
        if s1_index >= len(s1) or s2_index >= len(s2):
            return 0

        if s1[s1_index] == s2[s2_index]:
            return 1 + self.top_down(s1, s2, s1_index + 1, s2_index + 1)
        else:
            return max(
                self.top_down(s1, s2, s1_index + 1, s2_index),
                self.top_down(s1, s2, s1_index, s2_index + 1),
            )

    def bottom_up(self, s1: str, s2: str) -> int:
        dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        for i in range(len(s1) - 1, -1, -1):
            for j in range(len(s2) - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve("acabac", "aebab"))
    print(solution.bottom_up("acabac", "aebab"))

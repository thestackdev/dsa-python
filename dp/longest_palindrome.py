class Solution:
    def __init__(self) -> None:
        pass

    def bottom_up(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        max_len = 1
        start_index = 0

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                max_len = 2
                start_index = i
                dp[i][i + 1] = True

        for sub_len in range(3, n + 1):
            for i in range(n - sub_len + 1):
                j = i + sub_len - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    max_len = sub_len
                    start_index = i

        return s[start_index : start_index + max_len]


if __name__ == "__main__":
    solution = Solution()
    print(solution.bottom_up("racecar"))

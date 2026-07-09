class Solution:
    def __init__(self) -> None:
        pass

    def solve(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while not s[left].isalnum():
                left += 1

            while not s[right].isalnum():
                right -= 1

            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve("a dog! a panic in a pagoda."))
    print(solution.solve("abc123"))

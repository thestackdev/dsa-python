class Solution:
    def __init__(self) -> None:
        pass

    def solve(self, s: str) -> int:
        max_len = 0
        left = right = 0

        chars_under_window = set()

        while right < len(s):
            while s[right] in chars_under_window:
                chars_under_window.remove(s[left])
                left += 1

            chars_under_window.add(s[right])
            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve("abcaabbbb"))

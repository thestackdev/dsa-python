from re import L


class Solution:
    def __init__(self) -> None:
        pass

    def solve(self, s: str, k: int) -> int:
        max_freq = max_len = 0
        left = right = 0
        freq = {}

        while right < len(s):
            freq[s[right]] = freq.get(s[right], 0) + 1
            max_freq = max(max_freq, freq[s[right]])

            if right - left + 1 - max_freq > k:
                freq[s[left]] = freq.get(s[left], 0) - 1
                left += 1

            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve("abaccc", 2))

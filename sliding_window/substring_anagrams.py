class Solution:
    def __init__(self) -> None:
        pass

    def solve(self, s1: str, s2: str) -> int:
        s1_len, s2_len = len(s1), len(s2)

        if s2_len > s1_len:
            return 0

        expected_freq, window_freq = [0] * 26, [0] * 26

        for ch in s2:
            expected_freq[ord(ch) - ord("a")] += 1

        left = right = 0
        anagrams_found = 0

        while right < s1_len:
            window_freq[ord(s1[right]) - ord("a")] += 1

            if right - left + 1 == s2_len:
                if window_freq == expected_freq:
                    anagrams_found += 1

                window_freq[ord(s1[left]) - ord("a")] -= 1
                left += 1

            right += 1

        return anagrams_found


if __name__ == "__main__":
    solution = Solution()
    s1 = "caabab"
    s2 = "aba"
    print(solution.solve(s1, s2))

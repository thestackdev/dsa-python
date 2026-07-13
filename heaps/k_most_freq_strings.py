from collections import Counter
import heapq
from typing import List


class Word:
    def __init__(self, value: str, freq: int) -> None:
        self.value = value
        self.freq = freq

    def __lt__(self, other) -> bool:
        return self.freq > other.freq


class Solution:
    def __init__(self) -> None:
        pass

    def solve(self, strs: List[str], k: int) -> List[str]:
        freqs = Counter(strs)
        freqs = [Word(value, freq) for (value, freq) in freqs.items()]

        heapq.heapify(freqs)

        return [heapq.heappop(freqs).value for _ in range(k)]


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve(["go", "coding", "byte", "byte", "go", "interview", "go"], 2))

from collections import Counter
import heapq
from typing import List, Self


class WordItem:
    def __init__(self, val: str, freq: int) -> None:
        self.val = val
        self.freq = freq

    def __lt__(self, other: Self) -> bool:
        if self.freq == other.freq:
            return self.val > other.val
        return self.freq > other.freq


class Solution:
    def __init__(self) -> None:
        pass

    def solve(self, strs: List[str], k: int) -> List[str]:
        freqs = Counter(strs)
        freqs = [WordItem(val, freq) for (val, freq) in freqs.items()]

        heapq.heapify(freqs)

        return [heapq.heappop(freqs).val for _ in range(k)]


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve(["go", "coding", "byte", "byte", "go", "interview", "go"], 2))


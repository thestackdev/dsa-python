from typing import List


class Interval:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    def __str__(self) -> str:
        return f"{self.start} {self.end}"


type Intervals = List[Interval]


class Solution:
    def __init__(self) -> None:
        pass

    def solve(self, intervals1: Intervals, intervals2: Intervals) -> Intervals:
        result: Intervals = []

        i = j = 0
        a: Interval | None = None
        b: Interval | None = None

        while i < len(intervals1) or j < len(intervals2):
            if intervals1[i].start < intervals2[j].start:
                a = intervals1[i]
                b = intervals2[j]
            else:
                a = intervals2[j]
                b = intervals1[i]

            if a.end >= b.start:
                result.append([a.start, min(a.end, b.end)])

            if a.end < b.end:
                i += 1
            else:
                j += 1

        return result

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

    def solve(self, intervals: Intervals) -> int:
        active_intervals = max_active_intervals = 0
        points = []

        for interval in intervals:
            points.append((interval.start, "S"))
            points.append((interval.end, "E"))

        for _, p_type in points:
            if p_type == "S":
                active_intervals += 1
            else:
                active_intervals -= 1

            max_active_intervals = max(max_active_intervals, active_intervals)

        return max_active_intervals


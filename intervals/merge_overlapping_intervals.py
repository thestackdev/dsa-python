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

    def solve(self, intervals: Intervals) -> Intervals:
        result: Intervals = []

        if not intervals:
            return result

        intervals.sort(key=lambda x: x.start)

        result.append(intervals[0])

        for interval in intervals[1:]:
            last_interval = result[-1]
            if last_interval.end >= interval.start:
                last_interval.end = max(last_interval.end, interval.end)
            else:
                result.append(interval)

        return result


if __name__ == "__main__":
    solution = Solution()
    intervals = [
        Interval(1, 3),
        Interval(2, 6),
        Interval(8, 10),
        Interval(15, 18),
    ]

    result = solution.solve(intervals)
    for r in result:
        print(r)

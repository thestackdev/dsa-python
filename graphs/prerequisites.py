from collections import defaultdict, deque
from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def prerequisites(self, courses: int, prerequisites: List[List[int]]) -> bool:

        in_degrees = [0] * courses
        graph = defaultdict(list)
        queue = deque()

        for prerequisite, course in prerequisites:
            graph[prerequisite].append(course)
            in_degrees[course] += 1

        for i in range(courses):
            if in_degrees[i] == 0:
                queue.append(i)

        enrolled_courses = 0

        while queue:
            node = queue.popleft()
            enrolled_courses += 1

            for neighbour in graph[node]:
                in_degrees[neighbour] -= 1

                if in_degrees[neighbour] == 0:
                    queue.append(neighbour)

        return courses == enrolled_courses

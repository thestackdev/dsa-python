from collections import deque
from typing import List


class Solution:
    def shortest_transformation_sequence(
        self, start: str, end: str, dictionary: List[str]
    ) -> int:

        if start == end:
            return 1

        dictionary_set = set(dictionary)

        if end not in dictionary_set:
            return 0

        queue = deque([start])
        visited = {start}

        dist = 1

        while queue:
            lower_case_alphabets = "abcdefghijklmnopqrstuvwxyz"

            for _ in range(len(queue)):
                node = queue.popleft()

                if node == end:
                    return dist

                for i in range(len(node)):
                    for c in lower_case_alphabets:
                        next_word = node[:i] + c + node[i + 1 :]

                        if next_word in dictionary_set and next_word not in visited:
                            visited.add(next_word)
                            queue.append(next_word)

            dist += 1

        return 0

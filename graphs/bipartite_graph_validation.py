from typing import List


class Soution:
    def __init__(self) -> None:
        pass

    def validate(self, graph: List[List[int]]) -> bool:
        colors = [0] * len(graph)

        for i in range(len(graph)):
            if colors[i] == 0 and not self.dfs(i, 1, graph, colors):
                return False

        return True

    def dfs(
        self, current_index: int, color: int, graph: List[List[int]], colors: List[int]
    ) -> bool:
        colors[current_index] = color

        for neighbour in graph[current_index]:
            if colors[neighbour] == color:
                return False

            if colors[neighbour] == 0 and not self.dfs(
                neighbour, -color, graph, colors
            ):
                return False

        return True

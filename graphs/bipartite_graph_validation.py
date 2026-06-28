from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def validate(self, graph: List[List[int]]) -> bool:
        colors = [0] * len(graph)

        for i in range(len(graph)):
            if colors[i] == 0 and not self.dfs(i, 1, colors, graph):
                return False

        return True

    def dfs(self, node: int, color: int, colors: List[int], graph: List[List[int]]):
        colors[node] = color

        for neighbour in graph[node]:
            if colors[neighbour] == color:
                return False

            if colors[neighbour] == 0 and not self.dfs(
                neighbour, -color, colors, graph
            ):
                return False

        return True

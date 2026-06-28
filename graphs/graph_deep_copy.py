from graphs.base import GraphNode


class Solution:
    def __init__(self) -> None:
        pass

    def deepcopy(self, node: GraphNode | None) -> GraphNode | None:
        if not node:
            return None

        return self.dfs(node)

    def dfs(self, node: GraphNode, cloned_map={}):
        if node in cloned_map:
            return cloned_map[node]

        cloned_node = GraphNode(node.val)
        cloned_map[node] = cloned_node

        for neighbour in node.neighbours:
            cloned_neighbour = self.dfs(neighbour, cloned_map)
            cloned_node.neighbours.append(cloned_neighbour)

        return cloned_node

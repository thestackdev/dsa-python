from collections import deque

from trees.base import TreeNode


class WidestBinaryTreeLength:
    def __init__(self) -> None:
        pass

    def bfs(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        max_width = 0

        queue = deque([(root, 0)])

        while queue:
            left_most_index = queue[0][1]
            right_most_index = queue[0][1]

            level_size = len(queue)

            for _ in range(level_size):
                node, i = queue.popleft()

                if node.left:
                    queue.append((node.left, 2 * i + 1))
                if node.right:
                    queue.append((node.right, 2 * i + 2))

                right_most_index = i

            max_width = max(max_width, right_most_index - left_most_index + 1)

        return max_width

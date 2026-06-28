from typing import List

from trees.base import TreeNode


class RightMostNode:
    def __init__(self) -> None:
        pass

    def bfs(self, root: TreeNode | None) -> List:
        rightmost_elements = []

        if not root:
            return rightmost_elements

        stack = [root]

        rightmost_elements.append(root)

        while stack:
            current_stack_len = len(stack)

            for i in range(current_stack_len):
                node = stack.pop()

                if node.left:
                    stack.append(node.left)

                if node.right:
                    stack.append(node.right)

                if i == current_stack_len - 1:
                    rightmost_elements.append(node.val)

        return rightmost_elements

from collections import deque

from trees.base import TreeNode


class InvertBinaryTree:
    def __init__(self) -> None:
        pass

    def dfs(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.dfs(root.left)
        self.dfs(root.right)

        return root

    def dfs_with_stack(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None

        stack = deque([root])

        while stack:
            node = stack.popleft()

            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root

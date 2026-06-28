from trees.base import TreeNode


class LowestCommonAncestor:
    def __init__(self) -> None:
        pass

    def dfs(self, node: TreeNode | None, p: TreeNode, q: TreeNode):
        if not node:
            return None

        if node == p or node == q:
            return node

        left = self.dfs(node.left, p, q)
        right = self.dfs(node.right, p, q)

        if left and right:
            return node

        return left or right

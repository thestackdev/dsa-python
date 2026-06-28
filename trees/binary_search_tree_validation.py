from trees.base import TreeNode


class BinarySearchTreeValidation:
    def __init__(self) -> None:
        pass

    def dfs(self, root: TreeNode) -> bool:
        return self.is_within_bounds(root, float("-inf"), float("inf"))

    def is_within_bounds(
        self, node: TreeNode | None, lower_boundary: float, upper_boundary: float
    ) -> bool:

        if not node:
            return True

        if not (lower_boundary < node.val < upper_boundary):
            return False

        return self.is_within_bounds(
            node.left, lower_boundary, node.val
        ) and self.is_within_bounds(node.right, node.val, upper_boundary)

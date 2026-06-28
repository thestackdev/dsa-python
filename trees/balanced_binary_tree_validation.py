from trees.base import TreeNode


class BalancedBinaryTreeValidation:
    def __init__(self) -> None:
        pass

    def dfs(self, root: TreeNode) -> bool:
        return self.get_height_imbalance(root) != -1

    def get_height_imbalance(self, node: TreeNode | None) -> int:
        if not node:
            return 0

        left_height = self.get_height_imbalance(node.left)
        right_heith = self.get_height_imbalance(node.right)

        if left_height == -1 or right_heith == -1:
            return -1

        if abs(left_height - right_heith) > 1:
            return -1

        return 1 + max(left_height, right_heith)

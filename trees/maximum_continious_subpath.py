from trees.base import TreeNode


class Solution:
    def __init__(self) -> None:
        self.current_max = 0

    def max_sum(self, node: TreeNode | None) -> int:
        if not node:
            return 0

        left_sum = max(self.max_sum(node.left), 0)
        right_sum = max(self.max_sum(node.left), 0)

        self.current_max = max(self.current_max, node.val + left_sum + right_sum)

        return node.val + max(left_sum, right_sum)

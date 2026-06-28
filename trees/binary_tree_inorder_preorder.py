from typing import List

from trees.base import TreeNode


class Solution:
    def __init__(self) -> None:
        self.inorder_index_map = {}
        self.preorder_index = 0

    def build(self, preorder: List[int], inorder: List[int]) -> TreeNode | None:
        for i, val in enumerate(inorder):
            self.inorder_index_map[val] = i

        return self.build_subtree(0, len(preorder) - 1, preorder, inorder)

    def build_subtree(
        self, left, right, preorder: List[int], inorder: List[int]
    ) -> TreeNode | None:
        if left > right:
            return None

        node_val = preorder[self.preorder_index]
        node = TreeNode(node_val)

        inorder_index: int = self.inorder_index_map[node_val]

        self.preorder_index += 1

        node.left = self.build_subtree(left, inorder_index - 1, preorder, inorder)
        node.right = self.build_subtree(inorder_index + 1, right, preorder, inorder)

        return node

from tries.base import TrieNode


class Solution:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str):
        current_node = self.root

        for c in word:
            if c not in current_node.children:
                current_node.children[c] = TrieNode()

            current_node = current_node.children[c]

        current_node.is_word = True

    def search(self, word: str) -> bool:
        current_node = self.root

        for c in word:
            if c not in current_node.children:
                return False

            current_node = current_node.children[c]

        return current_node.is_word

    def has_prefix(self, word: str) -> bool:
        current_node = self.root

        for c in word:
            if c not in current_node.children:
                return False

            current_node = current_node.children[c]

        return True

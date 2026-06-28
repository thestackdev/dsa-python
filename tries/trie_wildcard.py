from tries.base import TrieNode


class Solution:
    def __init__(self) -> None:
        self.root = TrieNode()

    def search(self, word: str) -> bool:
        return self.search_helper(0, word, self.root)

    def search_helper(self, start_index: int, word: str, node: TrieNode) -> bool:

        for i in range(start_index, len(word)):
            c = word[i]

            if c == ".":
                for child in node.children.values():
                    if self.search_helper(i + 1, word, child):
                        return True

                return False

            elif c in node.children:
                node = node.children[c]

            else:
                return False

        return node.is_word

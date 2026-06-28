class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_word = False


class TrieNodeWithWord:
    def __init__(self) -> None:
        self.children = {}
        self.word = None

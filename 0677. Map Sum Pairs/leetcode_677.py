class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = 0
        self.sum = 0
        self.is_word = False


class MapSum:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        curr = self.root
        for c in key:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.sum += val
        if curr.is_word:
            old_val = curr.val
            curr = self.root
            for c in key:
                curr.children[c].sum -= old_val
                curr = curr.children[c]
        curr.val = val
        curr.is_word = True

    def sum(self, prefix: str) -> int:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return 0
            curr = curr.children[c]
        return curr.sum

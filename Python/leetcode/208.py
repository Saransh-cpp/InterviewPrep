class Node:
    def __init__(self):
        self.links = [None] * 26
        self.is_end = False

    def contains(self, key):
        return self.links[ord(key) - ord('a')] is not None

    def put(self, key):
        self.links[ord(key) - ord('a')] = Node()

    def get(self, key):
        return self.links[ord(key) - ord('a')]


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word) -> None:
        node = self.root
        for ch in word:
            if not node.contains(ch):
                node.put(ch)
            node = node.get(ch)
        node.is_end = True

    def search(self, word) -> bool:
        node = self.root
        for ch in word:
            if not node.contains(ch):
                return False
            node = node.get(ch)
        return node.is_end

    def startsWith(self, prefix) -> bool:
        node = self.root
        for ch in prefix:
            if not node.contains(ch):
                return False
            node = node.get(ch)
        return True

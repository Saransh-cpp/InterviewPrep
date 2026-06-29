class Node:
    def __init__(self, val, nxt = None, prev = None):
        self.val = val
        self.nxt = nxt
        self.prev = prev


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity

        self.head = Node([-1, -1])
        self.tail = Node([-1, -1])
        self.head.nxt = self.tail
        self.tail.prev = self.head

        self.map = {}

    def delete_node(self, node):
            tmp = node.prev
            node.prev.nxt = node.nxt
            node.nxt.prev = tmp

    def insert_after_head(self, node):
            temp = self.head.nxt
            self.head.nxt = node
            node.prev = self.head
            node.nxt = temp
            temp.prev = node

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.delete_node(node)
            self.insert_after_head(node)
            return node.val[1]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val[1] = value
            self.delete_node(node)
            self.insert_after_head(node)
        else:
            if self.capacity <= 0:
                node = self.tail.prev
                del self.map[node.val[0]]
                self.delete_node(node)
            else:
                self.capacity -= 1
            node = Node([key, value])
            self.insert_after_head(node)
            self.map[key] = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

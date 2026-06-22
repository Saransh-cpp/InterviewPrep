import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(lists):
        h = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(h, (node.val, i, node))

        res = ListNode(0)
        curr = res
        while h:
            val, i, node = heapq.heappop(h)
            curr.next = node
            if node.next:
                heapq.heappush(h, (node.next.val, i, node.next))
            curr = curr.next
        return res.next

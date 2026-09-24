import heapq


class KthLargest:
    def __init__(self, k, nums):
        self.h = nums
        self.k = k
        heapq.heapify(self.h)
        while len(self.h) > self.k:
            heapq.heappop(self.h)

    def add(self, val: int) -> int:
        if len(self.h) < self.k:
            heapq.heappush(self.h, val)
        elif val >= self.h[0]:
            heapq.heappushpop(self.h, val)
        return self.h[0]

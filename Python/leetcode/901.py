from collections import deque


class StockSpanner:
    def __init__(self):
        self.st = deque()
        self.i = -1

    def next(self, price: int) -> int:
        ind = -1
        while self.st and self.st[-1][0] <= price:
            self.st.pop()
        if self.st:
            ind = self.st[-1][1]
        self.i += 1
        self.st.append([price, self.i])
        return self.i - ind


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

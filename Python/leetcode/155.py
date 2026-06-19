from collections import deque


class MinStack:

    def __init__(self):
        self.data = deque()

    def push(self, val: int) -> None:
        if len(self.data) == 0:
            self.data.append([val, val])
        else:
            self.data.append([val, min(val, self.data[-1][1])])

    def pop(self) -> None:
        self.data.pop()

    def top(self) -> int:
        return self.data[-1][0]

    def getMin(self) -> int:
        return self.data[-1][1]


class MinStack:

    def __init__(self):
        self.data = deque()
        self.min = 0

    def push(self, val: int) -> None:
        if len(self.data) == 0:
            self.data.append(val)
            self.min = val
        elif val < self.min:
            self.data.append(2*val - self.min)
            self.min = val
        else:
            self.data.append(val)

    def pop(self) -> None:
        if self.data[-1] < self.min:
            self.min = 2 * self.min - self.data[-1]
        self.data.pop()

    def top(self) -> int:
        if self.data[-1] <= self.min:
            return self.min
        return self.data[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

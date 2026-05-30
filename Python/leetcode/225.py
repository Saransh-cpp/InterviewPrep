from collections import deque


class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        for _ in range(len(self.q1) - 1):
            self.q2.append(self.q1.popleft())
        popped = self.q1.pop()
        self.q1 = self.q2
        self.q2 = deque()
        return popped

    def top(self) -> int:
        for _ in range(len(self.q1) - 1):
            self.q2.append(self.q1.popleft())
        popped = self.q1[0]
        self.q1 = self.q2
        self.q1.append(popped)
        self.q2 = deque()
        return popped

    def empty(self) -> bool:
        return len(self.q1) == 0


class MyStack:

    def __init__(self):
        self.q1 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)
        self.q1.rotate(1)

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0

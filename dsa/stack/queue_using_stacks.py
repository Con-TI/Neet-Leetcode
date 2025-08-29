class MyQueue:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        stack2 = []
        while len(self.stack) > 1:
            stack2.append(self.stack.pop())
        res = self.stack.pop()
        while stack2:
            self.stack.append(stack2.pop())
        return res

    def peek(self) -> int:
        stack2 = []
        while len(self.stack) > 1:
            stack2.append(self.stack.pop())
        res = self.stack[-1]
        while stack2:
            self.stack.append(stack2.pop())
        return res

    def empty(self) -> bool:
        return len(self.stack) == 0
class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = float('inf')
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.minimum:
            self.minimum = val
            self.minStack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.minimum:
            self.minStack.pop()
            self.minimum = self.minStack[-1] if self.minStack else float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum

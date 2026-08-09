class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        current_min = min(self.stack[-1][1], val) if self.stack else val
        self.stack.append((val, current_min))

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

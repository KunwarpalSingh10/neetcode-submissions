class MinStack:

    def __init__(self):
        self.array = []
        self.smallest = []

    def push(self, val: int) -> None:
        self.array.append(val)
        if self.smallest:
            val = min(self.smallest[-1], val)
        self.smallest.append(val)

    def pop(self) -> None:
        removed = self.array.pop()
        self.smallest.pop()

    def top(self) -> int:
        if self.array:
            return self.array[-1]
        return None

    def getMin(self) -> int:
        return self.smallest[-1]


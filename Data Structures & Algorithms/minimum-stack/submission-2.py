class MinStack:

    def __init__(self):
        self.st = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if self.minStack:
            val = min(val,self.minStack[-1])
        self.minStack.append(val)

    def pop(self) -> None:
        self.st.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

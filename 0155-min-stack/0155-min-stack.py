class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]

    def push(self, val: int) -> None:
        if len(self.minstack)==0 or val<=self.minstack[-1]: self.minstack.append(val)
        return self.stack.append(val)

    def pop(self) -> None:
        p=self.stack.pop()
        if len(self.minstack)>0 and self.minstack[-1]==p: self.minstack.pop()
        return p

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
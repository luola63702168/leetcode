class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.con_list = []

    def push(self, x: int) -> None:
        self.con_list.insert(0, x)

    def pop(self) -> None:
        self.con_list.pop(0)

    def top(self) -> int:
        return self.con_list[0]

    def getMin(self) -> int:
        return min(self.con_list)

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
param_4 = obj.getMin()
print(param_4)

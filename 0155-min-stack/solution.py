class MinStack:

    def __init__(self):
        self.st =[]
        self.minst =[]
        

    def push(self, val: int) -> None:
        self.st.append(val)

        if not self.minst:
            self.minst.append(val)
        else:
            self.minst.append(min(val,self.minst[-1]))

    def pop(self) -> None:
           if self.st:
            self.st.pop()
            self.minst.pop()


    def top(self) -> int:
        if self.st:
            return self.st[-1]

    def getMin(self) -> int:
        if self.minst:
            return self.minst[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

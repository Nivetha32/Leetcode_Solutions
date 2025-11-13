class CustomStack:

    def __init__(self, maxSize: int):
        self.st, self.n = [],maxSize
        

    def push(self, x: int) -> None:
        if len(self.st)<self.n: self.st.append(x)
        

    def pop(self) -> int:
        return -1 if not self.st else self.st.pop()
        

    def increment(self, k: int, val: int) -> None:

        self.st[:k] = [i+val for i in self.st[:k]]


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

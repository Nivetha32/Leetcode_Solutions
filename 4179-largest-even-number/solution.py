class Solution:
    def largestEven(self, s: str) -> str:
        i = s.rfind('2')
        return "" if i == -1 else s[:i+1]

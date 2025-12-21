class Solution:
    def maxDistinct(self, s: str) -> int:
        k = set(s)
        return len(k)

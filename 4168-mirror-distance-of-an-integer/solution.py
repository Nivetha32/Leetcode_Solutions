class Solution:
    def mirrorDistance(self, n: int) -> int:
        
        k = int(str(n)[::-1])
        m = abs(n-k)
        return m

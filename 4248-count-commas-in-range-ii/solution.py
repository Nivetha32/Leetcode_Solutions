class Solution:
    def countCommas(self, n: int) -> int:
        h = 0
        l = 1000
        while l<=n:
            h+=n-l+1
            l*=1000
        return h

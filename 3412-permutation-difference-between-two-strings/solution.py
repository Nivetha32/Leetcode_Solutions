class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        r=0
        for i in range(len(s)):
            k=s[i]
            r+=abs(i-t.index(k))
        return r

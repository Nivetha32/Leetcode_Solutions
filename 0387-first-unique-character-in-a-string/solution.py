class Solution:
    def firstUniqChar(self, s: str) -> int:
        k = Counter(s)
        for i,val in enumerate(s):
            if k[val]==1:
                return i
        return -1


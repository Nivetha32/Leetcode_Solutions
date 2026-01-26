class Solution:
    def minimumMoves(self, s: str) -> int:
        m = n =0
        while n<len(s):
            if s[n] == 'X':
                m+=1
                n+=3
            else:
                n+=1
        return m

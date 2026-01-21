class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        c=0
        sub=""
        for i in range(0,len(s)-2):
            sub = s[i:i+3]
            if len(set(sub))==3:
             c+=1
        return c

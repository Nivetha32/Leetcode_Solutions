class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vow = set("aeiou")
        k=0
        o=0

        for c in s:
            if c.isalpha():
                if c in vow:
                    k+=1
                else:
                    o+=1
        if o>0:
            return k//o
        else:
            return 0

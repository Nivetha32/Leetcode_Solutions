class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        le = 0
        re = len(s)-1
        while le<re:
          if le!=re:
            m = min(s[le],s[re])
            s[le]=m
            s[re]=m
          le+=1
          re-=1
        return "".join(s)

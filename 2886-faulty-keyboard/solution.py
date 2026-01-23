class Solution:
    def finalString(self, s: str) -> str:
        k=""
        for i in range(0,len(s)):
            if s[i]=='i':
                k=k[::-1]
            else:
                k+=s[i]
        return k



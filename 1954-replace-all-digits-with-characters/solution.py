class Solution:
    def replaceDigits(self, s: str) -> str:
        m=''
        for i in range(len(s)):
            if i%2!=0:
               m+=chr(ord(s[i-1])+int(s[i]))
            else:
                m+=s[i]
        return m

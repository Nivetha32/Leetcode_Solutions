class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        r = 0 
        for char in columnTitle: 
            r = r * 26 + (ord(char) - ord('A') + 1) 
        return r

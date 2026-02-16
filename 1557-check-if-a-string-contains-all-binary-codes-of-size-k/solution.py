class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        p = set()
        for i in range(len(s)-k+1):
            l = s[i:i+k]
            p.add(l)
        return len(p)==2**k
            

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        zt = set(zip(s, t))
        return len(zt) == len(set(s)) == len(set(t))
        

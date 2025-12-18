class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        k = set(allowed)
        c=0
        for wor in words:
            if all(n in k for n in wor):
                c+=1
        return c
        

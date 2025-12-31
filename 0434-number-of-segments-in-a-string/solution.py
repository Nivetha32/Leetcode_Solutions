class Solution:
    def countSegments(self, s: str) -> int:
        c=0
        for i in s.split():
            c+=1
        return c

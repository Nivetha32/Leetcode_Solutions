class Solution:
    def minimumChairs(self, s: str) -> int:
        k=0
        max=0
        for i in s:
            if i=='E':
                k+=1
                if k>max:
                    max=k
            else:
                k-=1
                
        return max

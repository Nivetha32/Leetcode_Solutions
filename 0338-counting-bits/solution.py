class Solution:
    def countBits(self, n: int) -> List[int]:
        m=[]
        for i in range(0,n+1):
           k = i.bit_count()
           m.append(k)
        return m
        

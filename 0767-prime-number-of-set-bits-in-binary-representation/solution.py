class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        l=[]
        p = {2,3,5,7,11,13,17,19}
        c=0
        for i in range(left, right+1):
            k = i.bit_count()
            if k in p:
                c+=1
        return c
            
        

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        f = set(i for i in range(1,a+1) if a%i==0)
        m = set(i for i in range(1,b+1) if b%i==0)
        
        k= set(f&m)
        return len(k)
       


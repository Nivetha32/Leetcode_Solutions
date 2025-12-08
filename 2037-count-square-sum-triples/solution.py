class Solution:
    def countTriples(self, n: int) -> int:
        squared = {i*i for i in range(1,n+1)}
        ans =0
      
        for a in range(1,n+1):
             for b in range(1,n+1):
                if a*a+b*b in squared:
                    ans+=1
        return ans

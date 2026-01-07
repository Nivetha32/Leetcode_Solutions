class Solution:
    def checkDivisibility(self, n: int) -> bool:
        k=0
        m=1
        for i in str(n):
            k+=int(i)
            m*=int(i)
        return n%(k+m)==0


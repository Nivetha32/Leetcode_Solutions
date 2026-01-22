class Solution:
    def alternateDigitSum(self, n: int) -> int:
        m = str(n)        
        p=0 
        for i in range(0,len(m)):
            if i%2==0:
                p+=int(m[i])
            else:
                p-=int(m[i])
        return p


class Solution:
    def countCommas(self, n: int) -> int:
        co=0
        for i in range(1,n+1):
           l = len(str(i))
           if l>=4:
               c=(l-1)//3
               co+=c
        return co
        

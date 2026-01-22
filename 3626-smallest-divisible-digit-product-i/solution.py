class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        if '0' in str(n):
            return n
        if t==1:
            return n
        num=n
        while True:
            temp=num
            p=1
            while temp>0:
                k = temp%10
                p*=k
                temp//=10
            if p%t==0:
                return num
            num+=1
            


        
   

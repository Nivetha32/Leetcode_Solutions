class Solution:
    def isBalanced(self, num: str) -> bool:
        c=0
        l=0
        for i in range(0,len(num)):
            if i%2==0:
                c+=int(num[i])
            else:
                l+=int(num[i])
        if c==l:
            return True
        else:
            return False



        

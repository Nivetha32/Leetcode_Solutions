class Solution:
    def averageValue(self, nums: List[int]) -> int:
        k=[]
        m=0
        for i in nums:
            if i%3==0 and i%2==0:
                k.append(i)
                m+=i
                i
        if not k:
            return 0
        else:
           return m//len(k)
        
        


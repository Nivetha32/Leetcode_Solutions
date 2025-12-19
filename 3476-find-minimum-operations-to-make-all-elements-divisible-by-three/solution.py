class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        o=0
        for i in nums:
            if i%3==1:
                o+=1
            elif i%3==2:
                o+=1
        return o
            
        

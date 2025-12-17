class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        s=0
        for index,value in enumerate(nums):
             if index%2==0:
                s+=value
             else:
                s-=value
        return s

        

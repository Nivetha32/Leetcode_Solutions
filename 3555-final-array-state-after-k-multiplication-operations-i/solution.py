class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while k:
            n = min(nums)
            for i in range(0,len(nums)):
                if nums[i]==n:
                  nums[i]*=multiplier
                  break
            k-=1
        return nums
        
            


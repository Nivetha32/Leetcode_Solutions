class Solution:
    def finalElement(self, nums: List[int]) -> int:
        g = len(nums)
        if g==1:
            return nums[0]
        return max(nums[0],nums[-1])
            

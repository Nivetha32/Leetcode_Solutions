class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ma=0
        mi=0
        for i in range(k):
            mi+=nums[i]
        for i in range(len(nums)-k,len(nums)):
            ma+=nums[i]
        return abs(ma-mi)
        
        

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        k=0
        l=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    k = nums[j]-nums[i]
                    l = max(l,k)
        if not l:
            return -1
        return l
                
                

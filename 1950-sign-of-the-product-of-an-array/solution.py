class Solution:
    def arraySign(self, nums: List[int]) -> int:
        k=1
        for i in range(len(nums)):
            if nums[i]==0:
                return 0
            k*=nums[i]
        return 1 if k>1 else -1
        

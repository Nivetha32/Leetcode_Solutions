class Solution:
    def minimumSum(self, nums: List[int]) -> int:
      
        m=float('inf')
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]>=nums[j]:
                    continue
                for k in range(j+1,len(nums)):
                    if nums[k]>=nums[j]:
                        continue
                    m = min(m,nums[i]+nums[j]+nums[k])
        
        if m == float('inf'):
            return -1
        return m

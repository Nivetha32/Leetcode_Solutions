class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        p = sum(nums)
        co =0
        m = len(nums)

        for i in range(m-1):
           p-=nums[i]
           ele = m-1-i

           if nums[i]*ele > p:
               co+=1
        return co
    

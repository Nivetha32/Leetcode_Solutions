class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p ={}
        for i in range(len(nums)):
            k = target- nums[i]
            if k in p:
                return [p[k],i]
            p[nums[i]]=i
        return p
            

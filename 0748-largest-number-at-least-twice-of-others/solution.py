class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        k = max(nums)
        ind = nums.index(k)
        for i in range(0,len(nums)):
            if nums[i]!=k and k<2*nums[i]:
                return -1
        return ind


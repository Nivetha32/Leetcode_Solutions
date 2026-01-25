class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        m = len(nums)
        j = m-1

        while j>0 and nums[j-1] < nums[j]:
            j-=1
        return j

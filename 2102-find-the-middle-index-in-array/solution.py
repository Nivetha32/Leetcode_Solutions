class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        les= 0
        ris= sum(nums)

        for i in range(len(nums)):
            if les == ris - nums[i]:

                return i
            les += nums[i]
            ris -= nums[i]
        return -1


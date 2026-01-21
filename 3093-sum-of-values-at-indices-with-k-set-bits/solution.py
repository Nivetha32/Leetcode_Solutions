class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        t=0
        for i in range(len(nums)):
            if i.bit_count()==k:
                t+=int(nums[i])
        return t


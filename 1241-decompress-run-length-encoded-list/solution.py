class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        return [val for  i, val in enumerate(nums) if i%2==1 for _ in range(nums[i-1])]

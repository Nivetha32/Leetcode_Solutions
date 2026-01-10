class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        k=nums
        lar = k[-1]*k[-2]
        sm =  k[0]*k[1]
        return lar-sm

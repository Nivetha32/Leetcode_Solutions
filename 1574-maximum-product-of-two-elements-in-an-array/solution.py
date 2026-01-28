class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ma =0
        for i in range(len(nums)):
             for j in range(i+1,len(nums)):
                  k =((nums[i]-1)*(nums[j]-1))
                  ma = max(k,ma)
        return ma

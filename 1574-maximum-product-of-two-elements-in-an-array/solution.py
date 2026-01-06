class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max =0
        for i in range(len(nums)):
             for j in range(i+1,len(nums)):
                  k =((nums[i]-1)*(nums[j]-1))
                  
                  if k>max:
                      max=k
        return max

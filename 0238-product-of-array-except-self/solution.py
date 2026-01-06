class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        right = 1
        k = [1]*len(nums)
        for i in range(len(nums)):
            k[i]*=left
            left*=nums[i]
        for j in range(len(nums)-1,-1,-1):
            k[j]*=right
            right*=nums[j]
        return k
             
            


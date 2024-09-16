class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        x = n * (n + 1) // 2
        a= sum(nums)
        return x - a
        

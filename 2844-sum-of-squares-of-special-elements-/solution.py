class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        s=0
        m = len(nums)
        for i in range(1,m+1):
            if m%i == 0:
                s+=nums[i-1]**2
        return s

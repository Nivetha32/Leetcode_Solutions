class Solution:
    def minOperations(self, nums: List[int]) -> int:
        k = nums[0]
        for i in nums:
            k&=i
        return 0 if all(j==k for j in nums) else 1

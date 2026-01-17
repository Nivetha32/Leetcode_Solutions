class Solution:
    def minOperations(self, nums: List[int], target: List[int]) -> int:
        y = set()
        for p in range(len(nums)):
            if nums[p]!=target[p]:
                y.add(nums[p])
        return len(y)

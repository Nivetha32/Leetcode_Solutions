class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        k = set(nums[0]).intersection(*nums)
        return sorted(list(k))

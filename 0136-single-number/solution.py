class Solution:
    def singleNumber(self, nums: List[int]) -> int:
      freq = Counter(nums)
      return next(key for key,value in freq.items() if value<2)

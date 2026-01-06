class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = set()
        return next(i for i in nums if i in s or s.add(i))
      

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        k = set(nums)
        while original in k:
              original*=2
        return original
              

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
           return sorted(l*l for l in nums)
        

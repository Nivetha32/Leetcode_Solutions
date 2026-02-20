class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        l = []
        for i in nums:
            if i and (-i) in nums:
                l.append(i)
        if not l:
            return -1
        return max(l)
        

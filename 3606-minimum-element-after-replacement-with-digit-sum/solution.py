class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_v = float('inf')
        for i in nums:
            s=0
            while i > 0:
                s+=i%10
                i//=10
            min_v = min(min_v,s)
        return min_v
        



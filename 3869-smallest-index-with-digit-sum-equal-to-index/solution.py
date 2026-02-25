class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            t = abs(nums[i])
            s=0
            while t:
                  m =t%10
                  s+=m
                  t//=10
            if s==i:
                return i
        return -1




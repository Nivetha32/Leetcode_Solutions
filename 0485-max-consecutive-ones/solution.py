class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur = best=0
        for i in nums:
            if i == 1:
             cur+=1
             best = max(best,cur)
            else:
             cur=0
        return best


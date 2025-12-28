class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        p = len(nums)
        d = [0]*p
        d[p-1]= nums[p-1]
        for j in range(p-2,-1,-1):
            d[j]=min(nums[j], d[j+1])
        k =0
        s=float('-inf')
        for j in range(p-1) :
              k+=nums[j]
              l = k-d[j+1]
              s=max(s,l)
        return s

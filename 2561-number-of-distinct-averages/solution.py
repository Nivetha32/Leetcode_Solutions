class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        k = set()
        while nums:
           l = min(nums)
           p = max(nums)
           o = (l+p)/2
           k.add(o)
           nums.remove(l)
           nums.remove(p)
        return len(k)





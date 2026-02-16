class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        m = Counter(nums)
        n = Counter(m.values())
        for i in nums:
            if n[m[i]]==1:
                return i
        return -1
        

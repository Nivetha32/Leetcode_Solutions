class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        m = Counter(nums)
        u = Counter(m.values())
        for i in nums:
            if u[m[i]]==1:
                return i
        return -1

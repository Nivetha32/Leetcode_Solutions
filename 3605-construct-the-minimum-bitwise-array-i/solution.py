class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        a = []
        for i in nums:
            if not i%2:
                a.append(-1)
                continue
            l = 1
            while (i& l):
                l<<=1
            l>>=1
            a.append(i- l)
        return a

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted([x for x in nums if x > 0])
        m = 1

        for i in nums:
            if i == m:
                m += 1

        return m


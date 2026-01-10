class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        k=0
        for i in nums:
            k^=i
        return k


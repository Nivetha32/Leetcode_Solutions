class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
       
        m = set(nums[0])

        for li in nums[1:]:
            m&=set(li)
        return sorted(list(m))


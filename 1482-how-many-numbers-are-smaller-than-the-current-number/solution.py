class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
       return [sum(n < x for n in nums) for x in nums]


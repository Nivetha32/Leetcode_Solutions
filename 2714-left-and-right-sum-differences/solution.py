class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        le = 0
        su = sum(nums)
        ree = [0] * len(nums)

        for i in range(len(nums)):
            su -= nums[i]
            ree[i] = abs(le- su)
            le+= nums[i]
        
        return ree

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        
        avg = []
        nums = nums[:]
        while nums:
            k = max(nums)
            y = min(nums)
            avg.append((k+y)/2)
            nums.remove(k)
            nums.remove(y)
           
        return min(avg)

        

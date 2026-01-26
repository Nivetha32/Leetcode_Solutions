class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        p = len(nums)
        while p > 1:
            for i in range(p // 2):
                if i % 2 == 0:
                    nums[i] = min(nums[2*i], nums[2*i+1])
                else:
                    nums[i] = max(nums[2*i], nums[2*i+1])
            p //= 2
        return nums[0]

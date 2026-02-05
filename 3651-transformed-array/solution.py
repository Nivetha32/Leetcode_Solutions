class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        p = len(nums)
        res = [0]*p
        for i in range(p):
            if nums[i]==0:
                res[i]=0
            else:
                ta = (i + nums[i]) % p
                res[i]=nums[ta]
        return res

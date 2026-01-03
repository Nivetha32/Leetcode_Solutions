class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max=cur_min = nums[0]
        lar = nums[0]
        for i in nums[1:]:
            t = cur_max
            cur_max = max(i, cur_max*i,cur_min*i)
            cur_min = min(i, t*i,cur_min*i)

            lar = max(cur_max,lar)
        return lar

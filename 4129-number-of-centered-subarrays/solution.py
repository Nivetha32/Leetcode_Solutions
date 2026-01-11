class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        k = len(nums)
        l=0

        for i in range(k):
            cur = 0
            m = set()
            for j in range(i,k):
                cur+=nums[j]
                m.add(nums[j])
                if cur in  m:
                    l+=1
        return l
            

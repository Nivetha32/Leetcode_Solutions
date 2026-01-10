class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        m = float('-inf')
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    m = max(m,(nums[i]-nums[j])*nums[k])
        if m<0:
            return 0
        return m


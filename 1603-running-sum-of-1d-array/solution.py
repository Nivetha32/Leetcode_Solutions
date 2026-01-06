class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        k =[]
        m=0
        for i in nums:
           m+=i 
           k.append(m)
        return k


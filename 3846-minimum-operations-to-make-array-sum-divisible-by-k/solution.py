class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        m=0
        n=0
        for i in nums:
            m+=i
        if m%k==0:
            return 0
        else:
           n =m%k
        return n
        
        
        

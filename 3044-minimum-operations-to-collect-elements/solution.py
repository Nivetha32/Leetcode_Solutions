class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        n = set(range(1,k+1))
        op = 0
        for i in reversed(nums):
            op+=1
            if i in n:
               n.remove(i)
            if not n:
              break
        return op




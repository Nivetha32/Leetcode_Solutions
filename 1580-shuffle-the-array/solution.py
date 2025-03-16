class Solution(object):
  def shuffle(self, nums, n):
    return [nums[i//2] if i % 2 == 0 else nums[n + i//2] for i in range(2*n)]

        

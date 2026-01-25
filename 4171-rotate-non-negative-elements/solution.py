class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
         gen = [y for y in nums if y>=0]

         if not gen:
             return nums
         m = len(gen)
         k = k%m

         rot = gen[k:]+ gen[:k]

         l = 0
         for j in range(len(nums)):
             if nums[j]>=0:
                  nums[j] = rot[l]
                  l+=1
         return nums

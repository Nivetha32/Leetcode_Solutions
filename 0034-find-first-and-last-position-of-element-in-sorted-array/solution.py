class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        fir = las = -1
        for i, val in enumerate(nums):
            if val == target:
              if fir == -1:
                fir=i
              las= i
        return [fir,las]
        

      
